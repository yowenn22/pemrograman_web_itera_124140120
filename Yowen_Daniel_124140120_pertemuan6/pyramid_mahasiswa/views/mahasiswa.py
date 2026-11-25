"""View CRUD RESTful API untuk data mahasiswa."""

import datetime

from pyramid.httpexceptions import HTTPBadRequest, HTTPNotFound
from pyramid.view import view_config

from ..models import Mahasiswa


def _ambil_json(request):
    """Mengambil payload JSON dari request.

    Parameter:
        request (Request): Objek request Pyramid.

    Return:
        dict | None: Dictionary payload, atau None jika tidak valid.
    """
    try:
        data = request.json_body
    except ValueError:
        return None
    if not isinstance(data, dict):
        return None
    return data


def _cari_mahasiswa(request, mahasiswa_id):
    """Mencari objek mahasiswa berdasarkan ID.

    Parameter:
        request (Request): Objek request Pyramid.
        mahasiswa_id: Nilai ID dari matchdict (bisa berupa string).

    Return:
        Mahasiswa | None: Objek mahasiswa atau None jika tidak ada.
    """
    try:
        mahasiswa_id = int(mahasiswa_id)
    except (TypeError, ValueError):
        return None
    return (
        request.dbsession.query(Mahasiswa)
        .filter_by(id=mahasiswa_id)
        .first()
    )


def _tidak_ditemukan(mahasiswa_id):
    """Membuat respons 404 untuk mahasiswa yang tidak ditemukan.

    Parameter:
        mahasiswa_id: ID mahasiswa yang dicari.

    Return:
        HTTPNotFound: Respons 404 berisi pesan kesalahan.
    """
    return HTTPNotFound(
        json_body={
            "error": (
                f"Mahasiswa dengan ID {mahasiswa_id} tidak ditemukan"
            )
        }
    )


@view_config(route_name="mahasiswa_list", renderer="json")
def mahasiswa_list(request):
    """Menampilkan seluruh data mahasiswa.

    Parameter:
        request (Request): Objek request Pyramid.

    Return:
        dict: Daftar mahasiswa dalam bentuk JSON.
    """
    mahasiswas = (
        request.dbsession.query(Mahasiswa)
        .order_by(Mahasiswa.id.asc())
        .all()
    )
    return {"mahasiswas": [m.to_dict() for m in mahasiswas]}


@view_config(route_name="mahasiswa_detail", renderer="json")
def mahasiswa_detail(request):
    """Menampilkan detail satu mahasiswa berdasarkan ID.

    Parameter:
        request (Request): Objek request Pyramid.

    Return:
        dict: Detail mahasiswa, atau respons 404 jika tidak ditemukan.
    """
    mahasiswa_id = request.matchdict["id"]
    mahasiswa = _cari_mahasiswa(request, mahasiswa_id)
    if mahasiswa is None:
        return _tidak_ditemukan(mahasiswa_id)
    return {"mahasiswa": mahasiswa.to_dict()}


@view_config(
    route_name="mahasiswa_add",
    request_method="POST",
    renderer="json",
)
def mahasiswa_add(request):
    """Menambahkan data mahasiswa baru.

    Parameter:
        request (Request): Objek request Pyramid.

    Return:
        dict: Data mahasiswa yang berhasil dibuat, atau respons 400.
    """
    data = _ambil_json(request)
    if data is None:
        return HTTPBadRequest(
            json_body={"error": "Body harus berupa JSON objek."}
        )

    for field in ("nim", "nama", "jurusan"):
        if not str(data.get(field, "")).strip():
            return HTTPBadRequest(
                json_body={"error": f"Field {field} wajib diisi!"}
            )

    tanggal_lahir = None
    if data.get("tanggal_lahir"):
        try:
            tanggal_lahir = datetime.datetime.fromisoformat(
                str(data["tanggal_lahir"])
            ).date()
        except ValueError:
            return HTTPBadRequest(
                json_body={
                    "error": (
                        "Format tanggal lahir tidak valid. "
                        "Gunakan format YYYY-MM-DD."
                    )
                }
            )

    dbsession = request.dbsession
    nim = str(data["nim"]).strip()
    duplikat = dbsession.query(Mahasiswa).filter_by(nim=nim).first()
    if duplikat is not None:
        return HTTPBadRequest(
            json_body={"error": f"NIM {nim} sudah terdaftar."}
        )

    mahasiswa = Mahasiswa(
        nim=nim,
        nama=str(data["nama"]).strip(),
        jurusan=str(data["jurusan"]).strip(),
        tanggal_lahir=tanggal_lahir,
        alamat=data.get("alamat"),
    )
    dbsession.add(mahasiswa)
    dbsession.flush()
    return {"success": True, "mahasiswa": mahasiswa.to_dict()}


@view_config(
    route_name="mahasiswa_update",
    request_method="PUT",
    renderer="json",
)
def mahasiswa_update(request):
    """Memperbarui data mahasiswa berdasarkan ID.

    Parameter:
        request (Request): Objek request Pyramid.

    Return:
        dict: Data mahasiswa terbaru, respons 400, atau respons 404.
    """
    mahasiswa_id = request.matchdict["id"]
    mahasiswa = _cari_mahasiswa(request, mahasiswa_id)
    if mahasiswa is None:
        return _tidak_ditemukan(mahasiswa_id)

    data = _ambil_json(request)
    if data is None:
        return HTTPBadRequest(
            json_body={"error": "Body harus berupa JSON objek."}
        )

    dbsession = request.dbsession

    if "nim" in data:
        nim = str(data["nim"]).strip()
        if not nim:
            return HTTPBadRequest(
                json_body={"error": "Field nim wajib diisi!"}
            )
        duplikat = (
            dbsession.query(Mahasiswa)
            .filter(Mahasiswa.nim == nim, Mahasiswa.id != mahasiswa.id)
            .first()
        )
        if duplikat is not None:
            return HTTPBadRequest(
                json_body={"error": f"NIM {nim} sudah terdaftar."}
            )
        mahasiswa.nim = nim

    for field in ("nama", "jurusan"):
        if field in data:
            nilai = str(data[field]).strip()
            if not nilai:
                return HTTPBadRequest(
                    json_body={"error": f"Field {field} wajib diisi!"}
                )
            setattr(mahasiswa, field, nilai)

    if "alamat" in data:
        mahasiswa.alamat = data["alamat"]

    if "tanggal_lahir" in data:
        if data["tanggal_lahir"]:
            try:
                mahasiswa.tanggal_lahir = (
                    datetime.datetime.fromisoformat(
                        str(data["tanggal_lahir"])
                    ).date()
                )
            except ValueError:
                return HTTPBadRequest(
                    json_body={
                        "error": (
                            "Format tanggal lahir tidak valid. "
                            "Gunakan format YYYY-MM-DD."
                        )
                    }
                )
        else:
            mahasiswa.tanggal_lahir = None

    return {"success": True, "mahasiswa": mahasiswa.to_dict()}


@view_config(
    route_name="mahasiswa_delete",
    request_method="DELETE",
    renderer="json",
)
def mahasiswa_delete(request):
    """Menghapus data mahasiswa berdasarkan ID.

    Parameter:
        request (Request): Objek request Pyramid.

    Return:
        dict: Pesan keberhasilan, atau respons 404.
    """
    mahasiswa_id = request.matchdict["id"]
    mahasiswa = _cari_mahasiswa(request, mahasiswa_id)
    if mahasiswa is None:
        return _tidak_ditemukan(mahasiswa_id)

    request.dbsession.delete(mahasiswa)
    return {
        "success": True,
        "message": (
            f"Mahasiswa dengan ID {mahasiswa_id} berhasil dihapus"
        ),
    }
