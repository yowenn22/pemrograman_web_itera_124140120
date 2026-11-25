"""View halaman utama berisi daftar endpoint API."""

from pyramid.view import view_config


@view_config(route_name="home", renderer="json")
def home(request):
    """Menampilkan informasi singkat aplikasi dan daftar endpoint.

    Parameter:
        request (Request): Objek request Pyramid.

    Return:
        dict: Informasi aplikasi beserta daftar endpoint.
    """
    return {
        "message": "RESTful API Manajemen Mahasiswa dan Matakuliah",
        "endpoints": {
            "mahasiswa": [
                "GET /api/mahasiswa",
                "GET /api/mahasiswa/{id}",
                "POST /api/mahasiswa",
                "PUT /api/mahasiswa/{id}",
                "DELETE /api/mahasiswa/{id}",
            ],
            "matakuliah": [
                "GET /api/matakuliah",
                "GET /api/matakuliah/{id}",
                "POST /api/matakuliah",
                "PUT /api/matakuliah/{id}",
                "DELETE /api/matakuliah/{id}",
            ],
        },
    }
