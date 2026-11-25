"""Skrip inisialisasi dan seeding data awal database."""

import argparse
import sys
from datetime import date

from pyramid.paster import bootstrap, setup_logging
from sqlalchemy.exc import OperationalError

from .. import models


def setup_models(dbsession):
    """Menyisipkan data awal mahasiswa dan mata kuliah.

    Seeding hanya dijalankan jika tabel terkait masih kosong, sehingga
    skrip aman dijalankan berulang kali tanpa membuat data duplikat.

    Parameter:
        dbsession (Session): Session database SQLAlchemy.

    Return:
        None
    """
    if dbsession.query(models.Mahasiswa).count() == 0:
        dbsession.add_all(
            [
                models.Mahasiswa(
                    nim="12345",
                    nama="Budi Santoso",
                    jurusan="Teknik Informatika",
                    tanggal_lahir=date(2000, 5, 15),
                    alamat="Jl. Merdeka No. 123, Bandung",
                ),
                models.Mahasiswa(
                    nim="54321",
                    nama="Siti Aminah",
                    jurusan="Sistem Informasi",
                    tanggal_lahir=date(2001, 8, 22),
                    alamat="Jl. Mawar No. 45, Jakarta",
                ),
            ]
        )
        print("Seeding mahasiswa: 2 data ditambahkan.")
    else:
        print("Seeding mahasiswa dilewati (data sudah ada).")

    if dbsession.query(models.Matakuliah).count() == 0:
        dbsession.add_all(
            [
                models.Matakuliah(
                    kode_mk="IF2110",
                    nama_mk="Pemrograman Web",
                    sks=3,
                    semester=3,
                ),
                models.Matakuliah(
                    kode_mk="IF3140",
                    nama_mk="Basis Data",
                    sks=3,
                    semester=4,
                ),
                models.Matakuliah(
                    kode_mk="IF2230",
                    nama_mk="Sistem Operasi",
                    sks=4,
                    semester=4,
                ),
            ]
        )
        print("Seeding matakuliah: 3 data ditambahkan.")
    else:
        print("Seeding matakuliah dilewati (data sudah ada).")


def parse_args(argv):
    """Membaca argumen baris perintah.

    Parameter:
        argv (list): Daftar argumen dari sys.argv.

    Return:
        argparse.Namespace: Argumen yang sudah diparsing.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "config_uri",
        help="Configuration file, e.g., development.ini",
    )
    return parser.parse_args(argv[1:])


def main(argv=sys.argv):
    """Menjalankan proses seeding data awal.

    Parameter:
        argv (list): Daftar argumen baris perintah.

    Return:
        None
    """
    args = parse_args(argv)
    setup_logging(args.config_uri)
    env = bootstrap(args.config_uri)

    try:
        with env["request"].tm:
            dbsession = env["request"].dbsession
            setup_models(dbsession)
        print("Seeding database selesai.")
    except OperationalError:
        print("Pyramid gagal terhubung ke database SQL.")
        print(
            "Pastikan service PostgreSQL berjalan dan connection string "
            "di development.ini sudah benar."
        )


if __name__ == "__main__":
    main()
