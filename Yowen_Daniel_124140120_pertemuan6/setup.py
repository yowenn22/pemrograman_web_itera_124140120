"""Konfigurasi packaging aplikasi RESTful API Manajemen Matakuliah."""

from setuptools import find_packages, setup

requires = [
    "pyramid>=2.0",
    "pyramid_tm",
    "transaction",
    "zope.sqlalchemy",
    "SQLAlchemy>=2.0",
    "alembic",
    "psycopg2-binary",
    "waitress",
]

tests_require = [
    "pytest",
    "webtest",
    "pycodestyle",
]

EXCLUDED_PACKAGES = [
    "pyramid_mahasiswa.alembic",
    "pyramid_mahasiswa.alembic.versions",
    "pyramid_mahasiswa.static",
    "pyramid_mahasiswa.templates",
]

setup(
    name="pyramid_mahasiswa",
    version="0.0",
    description="RESTful API Manajemen Mahasiswa dan Matakuliah",
    author="Yowen Daniel",
    author_email="yowendaniel22@gmail.com",
    packages=find_packages(exclude=EXCLUDED_PACKAGES),
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
    extras_require={
        "testing": tests_require,
    },
    entry_points={
        "paste.app_factory": [
            "main = pyramid_mahasiswa:main",
        ],
    },
)
