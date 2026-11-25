"""Modul pengelola koleksi perpustakaan."""

from library_item import LibraryItem
from member import Member


class Library:
    """Mengelola koleksi item dan anggota perpustakaan."""

    def __init__(self, nama: str):
        """Menginisialisasi perpustakaan.

        Parameter:
            nama (str): Nama perpustakaan.
        """
        self.__nama = nama
        self.__koleksi = []
        self.__anggota = []

    @property
    def nama(self) -> str:
        """Mengembalikan nama perpustakaan."""
        return self.__nama

    @property
    def jumlah_item(self) -> int:
        """Mengembalikan jumlah item dalam koleksi."""
        return len(self.__koleksi)

    @property
    def koleksi(self) -> tuple:
        """Mengembalikan salinan read-only koleksi."""
        return tuple(self.__koleksi)

    def tambah_anggota(self, member: Member) -> bool:
        """Mendaftarkan anggota baru ke perpustakaan.

        Parameter:
            member (Member): Objek anggota yang akan didaftarkan.

        Return:
            bool: True jika berhasil, False jika anggota tidak valid
                atau ID-nya sudah terdaftar.
        """
        if not isinstance(member, Member):
            print("Gagal: objek anggota tidak valid.")
            return False
        if any(a.member_id == member.member_id for a in self.__anggota):
            print(f"Gagal: anggota {member.member_id} sudah terdaftar.")
            return False
        self.__anggota.append(member)
        print(
            f"[OK] Anggota '{member.nama}' "
            f"({member.member_id}) terdaftar."
        )
        return True

    def tambah_item(self, item: LibraryItem) -> bool:
        """Menambahkan item baru ke koleksi perpustakaan.

        Parameter:
            item (LibraryItem): Objek buku atau majalah.

        Return:
            bool: True jika berhasil, False jika item tidak valid
                atau ID-nya sudah digunakan.
        """
        if not isinstance(item, LibraryItem):
            print("Gagal: item harus berasal dari class LibraryItem.")
            return False
        if any(i.item_id == item.item_id for i in self.__koleksi):
            print(f"Gagal: ID item {item.item_id} sudah terdaftar.")
            return False
        self.__koleksi.append(item)
        print(f"[OK] Item '{item.judul}' ({item.item_id}) ditambahkan.")
        return True

    def tampilkan_katalog(self) -> None:
        """Menampilkan seluruh item koleksi beserta statusnya.

        Return:
            None
        """
        if not self.__koleksi:
            print("Koleksi perpustakaan masih kosong.")
            return
        for nomor, item in enumerate(self.__koleksi, start=1):
            print(f"{nomor}. {item.get_detail()}")

    def tampilkan_item_tersedia(self) -> None:
        """Menampilkan item yang belum dipinjam.

        Return:
            None
        """
        tersedia = [item for item in self.__koleksi if not item.is_dipinjam]
        if not tersedia:
            print("Tidak ada item yang tersedia saat ini.")
            return
        for nomor, item in enumerate(tersedia, start=1):
            print(f"{nomor}. {item.get_detail()}")

    def cari_item(self, kata_kunci: str) -> list:
        """Mencari item berdasarkan judul atau ID.

        Pencarian tidak membedakan huruf besar dan kecil.

        Parameter:
            kata_kunci (str): Judul atau ID yang dicari.

        Return:
            list: Daftar item yang cocok (bisa kosong).
        """
        kata_kunci = kata_kunci.strip().lower()
        if not kata_kunci:
            return []
        return [
            item
            for item in self.__koleksi
            if kata_kunci in item.judul.lower()
            or kata_kunci in item.item_id.lower()
        ]

    def pinjam_item(self, item_id: str, member: Member) -> bool:
        """Meminjamkan item kepada anggota terdaftar.

        Parameter:
            item_id (str): ID item yang akan dipinjam.
            member (Member): Anggota yang meminjam.

        Return:
            bool: True jika peminjaman berhasil, False jika gagal.
        """
        if member not in self.__anggota:
            print("Gagal: anggota belum terdaftar di perpustakaan.")
            return False

        item = self.__cari_item_by_id(item_id)
        if item is None:
            print(f"Gagal: item dengan ID {item_id} tidak ditemukan.")
            return False
        if item.is_dipinjam:
            print(f"Gagal: '{item.judul}' sedang dipinjam.")
            return False

        if item.pinjam():
            member.tambah_pinjaman(item.item_id)
            print(f"[OK] '{item.judul}' dipinjam oleh {member.nama}.")
            return True
        return False

    def kembalikan_item(self, item_id: str, member: Member) -> bool:
        """Mengembalikan item yang dipinjam anggota.

        Parameter:
            item_id (str): ID item yang dikembalikan.
            member (Member): Anggota yang mengembalikan.

        Return:
            bool: True jika pengembalian berhasil, False jika gagal.
        """
        if member not in self.__anggota:
            print("Gagal: anggota belum terdaftar di perpustakaan.")
            return False

        item = self.__cari_item_by_id(item_id)
        if item is None:
            print(f"Gagal: item dengan ID {item_id} tidak ditemukan.")
            return False
        if not item.is_dipinjam:
            print(f"Gagal: '{item.judul}' tidak sedang dipinjam.")
            return False
        if item.item_id not in member.pinjaman:
            print(
                f"Gagal: '{item.judul}' tidak tercatat sebagai "
                f"pinjaman {member.nama}."
            )
            return False

        if item.kembalikan():
            member.hapus_pinjaman(item.item_id)
            print(f"[OK] '{item.judul}' dikembalikan oleh {member.nama}.")
            return True
        return False

    def __cari_item_by_id(self, item_id: str):
        """Mencari item berdasarkan ID (method internal).

        Parameter:
            item_id (str): ID item yang dicari.

        Return:
            LibraryItem | None: Item yang ditemukan atau None.
        """
        for item in self.__koleksi:
            if item.item_id.lower() == item_id.strip().lower():
                return item
        return None
