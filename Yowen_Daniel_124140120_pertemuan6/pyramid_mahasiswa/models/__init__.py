"""Konfigurasi engine, session, dan transaksi database aplikasi."""

import zope.sqlalchemy
from sqlalchemy import engine_from_config
from sqlalchemy.orm import configure_mappers, sessionmaker

from .mahasiswa import Mahasiswa  # noqa: F401
from .matakuliah import Matakuliah  # noqa: F401

# Pastikan seluruh model sudah terdaftar sebelum mapper dikonfigurasi.
configure_mappers()


def get_engine(settings, prefix="sqlalchemy."):
    """Membuat engine SQLAlchemy dari pengaturan aplikasi.

    Parameter:
        settings (dict): Pengaturan aplikasi dari berkas INI.
        prefix (str): Prefix kunci pengaturan SQLAlchemy.

    Return:
        Engine: Engine SQLAlchemy yang terhubung ke database.
    """
    return engine_from_config(settings, prefix)


def get_session_factory(engine):
    """Membuat session factory SQLAlchemy untuk engine tertentu.

    Parameter:
        engine (Engine): Engine database yang sudah dibuat.

    Return:
        sessionmaker: Factory pembuat session database.
    """
    factory = sessionmaker()
    factory.configure(bind=engine)
    return factory


def get_tm_session(session_factory, transaction_manager):
    """Membuat session yang terikat dengan transaction manager Pyramid.

    Parameter:
        session_factory (sessionmaker): Factory pembuat session.
        transaction_manager: Transaction manager dari pyramid_tm.

    Return:
        Session: Session database yang siap dipakai pada request.
    """
    dbsession = session_factory()
    zope.sqlalchemy.register(
        dbsession, transaction_manager=transaction_manager
    )
    return dbsession


def includeme(config):
    """Mendaftarkan database session ke dalam konfigurasi Pyramid.

    Parameter:
        config (Configurator): Objek konfigurasi Pyramid.

    Return:
        None
    """
    settings = config.get_settings()
    settings["tm.manager_hook"] = "pyramid_tm.explicit_manager"

    engine = get_engine(settings)
    session_factory = get_session_factory(engine)
    config.registry["dbsession_factory"] = session_factory

    config.add_request_method(
        lambda request: get_tm_session(
            session_factory, request.tm
        ),
        "dbsession",
        reify=True,
    )
