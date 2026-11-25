"""Modul anggota perpustakaan."""


class Member:
    """Anggota perpustakaan yang dapat meminjam item."""

    def __init__(self, member_id: str, nama: str):
        """Menginisialisasi data anggota.

        Parameter:
            member_id (str): ID unik anggota.
            nama (str): Nama lengkap anggota.
        """
        self.__member_id = member_id
        self.__nama = nama
        self.__pinjaman = []

    @property
    def member_id(self) -> str:
        """Mengembalikan ID anggota."""
        return self.__member_id

    @property
    def nama(self) -> str:
        """Mengembalikan nama anggota."""
        return self.__nama

    @property
    def pinjaman(self) -> tuple:
        """Mengembalikan salinan daftar item yang dipinjam."""
        return tuple(self.__pinjaman)

    def tambah_pinjaman(self, item_id: str) -> None:
        """Mencatat item yang dipinjam anggota.

        Parameter:
            item_id (str): ID item yang dipinjam.

        Return:
            None
        """
        self.__pinjaman.append(item_id)

    def hapus_pinjaman(self, item_id: str) -> None:
        """Menghapus catatan item yang telah dikembalikan.

        Parameter:
            item_id (str): ID item yang dikembalikan.

        Return:
            None
        """
        if item_id in self.__pinjaman:
            self.__pinjaman.remove(item_id)

    def __str__(self) -> str:
        """Mengembalikan representasi anggota."""
        return f"{self.member_id} - {self.nama}"
