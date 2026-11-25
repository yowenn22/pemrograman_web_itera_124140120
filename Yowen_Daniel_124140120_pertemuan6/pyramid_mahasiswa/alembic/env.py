"""Konfigurasi environment Alembic untuk aplikasi Pyramid."""

from logging.config import fileConfig

from alembic import context
from pyramid.paster import get_appsettings
from sqlalchemy import engine_from_config, pool

from pyramid_mahasiswa.models.meta import Base
import pyramid_mahasiswa.models  # noqa: F401

config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

settings = get_appsettings(config.config_file_name)
target_metadata = Base.metadata


def run_migrations_offline():
    """Menjalankan migrasi dalam mode offline (tanpa koneksi DB).

    Return:
        None
    """
    url = settings["sqlalchemy.url"]
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Menjalankan migrasi dengan koneksi database aktif.

    Return:
        None
    """
    section = config.get_section(config.config_ini_section)
    section["sqlalchemy.url"] = settings["sqlalchemy.url"]
    connectable = engine_from_config(
        section,
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
