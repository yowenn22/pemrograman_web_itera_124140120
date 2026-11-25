"""Entry point aplikasi Pyramid RESTful API Manajemen Matakuliah."""

from pyramid.config import Configurator


def main(global_config, **settings):
    """Membuat dan mengembalikan aplikasi WSGI Pyramid.

    Parameter:
        global_config (dict): Konfigurasi global dari PasteDeploy.
        **settings: Pengaturan aplikasi dari berkas INI.

    Return:
        WSGIApplication: Aplikasi Pyramid yang siap dijalankan server.
    """
    config = Configurator(settings=settings)
    config.include("pyramid_tm")
    config.include(".models")
    config.include(".routes")
    config.scan()
    return config.make_wsgi_app()
