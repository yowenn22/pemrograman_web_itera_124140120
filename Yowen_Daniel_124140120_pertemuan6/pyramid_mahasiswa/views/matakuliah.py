"""View CRUD RESTful API untuk data mata kuliah."""

from pyramid.httpexceptions import HTTPBadRequest, HTTPNotFound
from pyramid.view import view_config

from ..models import Matakuliah

FIELD_WAJIB = ("kode_mk", "nama_mk", "sks", "semester")


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


def _ke_int_positif(nilai, nama_field):
    """Mengubah nilai menjadi integer yang lebih besar dari nol.

    Parameter:
        nilai: Nilai yang akan dikonversi.
        nama_field (str): Nama field untuk pesan kesalahan.

    Return:
        int: Nilai integer positif.

    Raises:
        ValueError: Jika nilai bukan bilangan bulat atau tidak positif.
    """
    try:
        angka = int(nilai)
    except (TypeError, ValueError):
        raise ValueError(
            f"Field {nama_field} harus berupa bilangan bulat."
        )
    if angka <= 0:
        raise ValueError(
            f"Field {nama_field} harus lebih besar dari 0."
        )
    return angka


def _cari_matakuliah(request, matakuliah_id):
    """Mencari objek mata kuliah berdasarkan ID.

    Parameter:
        request (Request): Objek request Pyramid.
        matakuliah_id: Nilai ID dari matchdict (bisa berupa string).

    Return:
        Matakuliah | None: Objek mata kuliah atau None jika tidak ada.
    """
    try:
        matakuliah_id = int(matakuliah_id)
    except (TypeError, ValueError):
        return None
    return (
        request.dbsession.query(Matakuliah)
        .filter_by(id=matakuliah_id)
        .first()
    )


def _tidak_ditemukan(matakuliah_id):
    """Membuat respons 404 untuk mata kuliah yang tidak ditemukan.

    Parameter:
        matakuliah_id: ID mata kuliah yang dicari.

    Return:
        HTTPNotFound: Respons 404 berisi pesan kesalahan.
    """
    return HTTPNotFound(
        json_body={
            "error": (
                "Matakuliah dengan ID "
                f"{matakuliah_id} tidak ditemukan"
            )
        }
    )


@view_config(route_name="matakuliah_list", renderer="json")
def matakuliah_list(request):
    """Menampilkan seluruh data mata kuliah.

    Parameter:
        request (Request): Objek request Pyramid.

    Return:
        dict: Daftar mata kuliah dalam bentuk JSON.
    """
    daftar = (
        request.dbsession.query(Matakuliah)
        .order_by(Matakuliah.id.asc())
        .all()
    )
    return {"matakuliah": [mk.to_dict() for mk in daftar]}


@view_config(route_name="matakuliah_detail", renderer="json")
def matakuliah_detail(request):
    """Menampilkan detail satu mata kuliah berdasarkan ID.

    Parameter:
        request (Request): Objek request Pyramid.

    Return:
        dict: Detail mata kuliah, atau respons 404.
    """
    matakuliah_id = request.matchdict["id"]
    matakuliah = _cari_matakuliah(request, matakuliah_id)
    if matakuliah is None:
        return _tidak_ditemukan(matakuliah_id)
    return {"matakuliah": matakuliah.to_dict()}


@view_config(
    route_name="matakuliah_add",
    request_method="POST",
    renderer="json",
)
def matakuliah_add(request):
    """Menambahkan data mata kuliah baru.

    Parameter:
        request (Request): Objek request Pyramid.

    Return:
        dict: Data mata kuliah yang dibuat, atau respons 400.
    """
    data = _ambil_json(request)
    if data is None:
        return HTTPBadRequest(
            json_body={"error": "Body harus berupa JSON objek."}
        )

    for field in FIELD_WAJIB:
        if field not in data or data[field] in (None, ""):
            return HTTPBadRequest(
                json_body={"error": f"Field {field} wajib diisi!"}
            )

    kode_mk = str(data["kode_mk"]).strip()
    nama_mk = str(data["nama_mk"]).strip()
    if not kode_mk:
        return HTTPBadRequest(
            json_body={"error": "Field kode_mk wajib diisi!"}
        )
    if not nama_mk:
        return HTTPBadRequest(
            json_body={"error": "Field nama_mk wajib diisi!"}
        )

    try:
        sks = _ke_int_positif(data["sks"], "sks")
        semester = _ke_int_positif(data["semester"], "semester")
    except ValueError as error:
        return HTTPBadRequest(json_body={"error": str(error)})

    dbsession = request.dbsession
    duplikat = (
        dbsession.query(Matakuliah).filter_by(kode_mk=kode_mk).first()
    )
    if duplikat is not None:
        return HTTPBadRequest(
            json_body={
                "error": f"Kode mata kuliah {kode_mk} sudah terdaftar."
            }
        )

    matakuliah = Matakuliah(
        kode_mk=kode_mk,
        nama_mk=nama_mk,
        sks=sks,
        semester=semester,
    )
    dbsession.add(matakuliah)
    dbsession.flush()
    return {"success": True, "matakuliah": matakuliah.to_dict()}


@view_config(
    route_name="matakuliah_update",
    request_method="PUT",
    renderer="json",
)
def matakuliah_update(request):
    """Memperbarui data mata kuliah berdasarkan ID.

    Parameter:
        request (Request): Objek request Pyramid.

    Return:
        dict: Data mata kuliah terbaru, respons 400, atau respons 404.
    """
    matakuliah_id = request.matchdict["id"]
    matakuliah = _cari_matakuliah(request, matakuliah_id)
    if matakuliah is None:
        return _tidak_ditemukan(matakuliah_id)

    data = _ambil_json(request)
    if data is None:
        return HTTPBadRequest(
            json_body={"error": "Body harus berupa JSON objek."}
        )

    dbsession = request.dbsession

    if "kode_mk" in data:
        kode_mk = str(data["kode_mk"]).strip()
        if not kode_mk:
            return HTTPBadRequest(
                json_body={"error": "Field kode_mk wajib diisi!"}
            )
        duplikat = (
            dbsession.query(Matakuliah)
            .filter(
                Matakuliah.kode_mk == kode_mk,
                Matakuliah.id != matakuliah.id,
            )
            .first()
        )
        if duplikat is not None:
            return HTTPBadRequest(
                json_body={
                    "error": (
                        f"Kode mata kuliah {kode_mk} sudah terdaftar."
                    )
                }
            )
        matakuliah.kode_mk = kode_mk

    if "nama_mk" in data:
        nama_mk = str(data["nama_mk"]).strip()
        if not nama_mk:
            return HTTPBadRequest(
                json_body={"error": "Field nama_mk wajib diisi!"}
            )
        matakuliah.nama_mk = nama_mk

    for field in ("sks", "semester"):
        if field in data:
            try:
                nilai = _ke_int_positif(data[field], field)
            except ValueError as error:
                return HTTPBadRequest(json_body={"error": str(error)})
            setattr(matakuliah, field, nilai)

    return {"success": True, "matakuliah": matakuliah.to_dict()}


@view_config(
    route_name="matakuliah_delete",
    request_method="DELETE",
    renderer="json",
)
def matakuliah_delete(request):
    """Menghapus data mata kuliah berdasarkan ID.

    Parameter:
        request (Request): Objek request Pyramid.

    Return:
        dict: Pesan keberhasilan, atau respons 404.
    """
    matakuliah_id = request.matchdict["id"]
    matakuliah = _cari_matakuliah(request, matakuliah_id)
    if matakuliah is None:
        return _tidak_ditemukan(matakuliah_id)

    request.dbsession.delete(matakuliah)
    return {
        "success": True,
        "message": (
            f"Matakuliah dengan ID {matakuliah_id} berhasil dihapus"
        ),
    }
