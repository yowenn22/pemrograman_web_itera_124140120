"""Peta URL Dispatch untuk seluruh endpoint RESTful API."""


def includeme(config):
    """Mendaftarkan seluruh rute aplikasi ke konfigurasi Pyramid.

    Parameter:
        config (Configurator): Objek konfigurasi Pyramid.

    Return:
        None
    """
    config.add_static_view("static", "static", cache_max_age=3600)

    # Halaman utama sebagai informasi daftar endpoint.
    config.add_route("home", "/")

    # Endpoint RESTful API untuk data mahasiswa.
    config.add_route(
        "mahasiswa_list", "/api/mahasiswa", request_method="GET"
    )
    config.add_route(
        "mahasiswa_detail", "/api/mahasiswa/{id}", request_method="GET"
    )
    config.add_route(
        "mahasiswa_add", "/api/mahasiswa", request_method="POST"
    )
    config.add_route(
        "mahasiswa_update", "/api/mahasiswa/{id}", request_method="PUT"
    )
    config.add_route(
        "mahasiswa_delete", "/api/mahasiswa/{id}", request_method="DELETE"
    )

    # Endpoint RESTful API untuk data mata kuliah.
    config.add_route(
        "matakuliah_list", "/api/matakuliah", request_method="GET"
    )
    config.add_route(
        "matakuliah_detail", "/api/matakuliah/{id}", request_method="GET"
    )
    config.add_route(
        "matakuliah_add", "/api/matakuliah", request_method="POST"
    )
    config.add_route(
        "matakuliah_update", "/api/matakuliah/{id}", request_method="PUT"
    )
    config.add_route(
        "matakuliah_delete", "/api/matakuliah/{id}",
        request_method="DELETE"
    )
