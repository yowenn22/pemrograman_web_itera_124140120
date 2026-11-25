"""Penanganan respons untuk endpoint yang tidak ditemukan."""

from pyramid.httpexceptions import HTTPNotFound
from pyramid.view import notfound_view_config


@notfound_view_config(renderer="json")
def notfound(request):
    """Mengembalikan respons JSON 404 untuk URL yang tidak terdaftar.

    Parameter:
        request (Request): Objek request Pyramid.

    Return:
        HTTPNotFound: Respons 404 dengan body JSON.
    """
    return HTTPNotFound(
        json_body={"error": "Endpoint tidak ditemukan."}
    )
