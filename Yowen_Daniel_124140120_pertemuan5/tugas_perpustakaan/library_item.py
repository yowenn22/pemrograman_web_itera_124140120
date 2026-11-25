"""
Modul item perpustakaan.

Berisi abstract class LibraryItem serta subclass Book dan Magazine.
"""

from abc import ABC, abstractmethod


class LibraryItem(ABC):
    """Abstract base class untuk seluruh item perpustakaan.

    Kelas ini tidak dapat diinstansiasi langsung karena memiliki
    method abstract get_detail() dan hitung_denda().
    """

    JENIS = "Item"

    def __init__(self, item_id: str, judul: str, tahun: int):
        """Menginisialisasi atribut dasar item.

        Parameter:
            item_id (str): ID unik item, misalnya "B001".
            judul (str): Judul buku atau majalah.
            tahun (int): Tahun terbit item.

        Raises:
            ValueError: Jika ID atau judul kosong.
        """
        if not str(item_id).strip():
            raise ValueError("ID item tidak boleh kosong.")
        if not str(judul).strip():
            raise ValueError("Judul item tidak boleh kosong.")

        # Atribut private (name mangling) untuk encapsulation.
        self.__item_id = str(item_id).strip()
        self.__judul = str(judul).strip()
        self.__tahun = int(tahun)
        self.__dipinjam = False

    @property
    def item_id(self) -> str:
        """Mengembalikan ID item."""
        return self.__item_id

    @property
    def judul(self) -> str:
        """Mengembalikan judul item."""
        return self.__judul

    @property
    def tahun(self) -> int:
        """Mengembalikan tahun terbit item."""
        return self.__tahun

    @property
    def jenis(self) -> str:
        """Mengembalikan jenis item (Buku atau Majalah)."""
        return self.JENIS

    @property
    def is_dipinjam(self) -> bool:
        """Mengembalikan status apakah item sedang dipinjam."""
        return self.__dipinjam

    def pinjam(self) -> bool:
        """Menandai item sebagai dipinjam.

        Return:
            bool: True jika berhasil, False jika item sudah dipinjam.
        """
        if self.__dipinjam:
            return False
        self.__dipinjam = True
        return True

    def kembalikan(self) -> bool:
        """Menandai item sebagai tersedia kembali.

        Return:
            bool: True jika berhasil, False jika item tidak dipinjam.
        """
        if not self.__dipinjam:
            return False
        self.__dipinjam = False
        return True

    @abstractmethod
    def get_detail(self) -> str:
        """Mengembalikan detail item dalam bentuk teks.

        Method ini wajib diimplementasikan oleh setiap subclass.

        Return:
            str: Detail item beserta status ketersediaannya.
        """
        raise NotImplementedError

    @abstractmethod
    def hitung_denda(self, hari_terlambat: int) -> float:
        """Menghitung denda keterlambatan pengembalian.

        Parameter:
            hari_terlambat (int): Jumlah hari keterlambatan.

        Return:
            float: Nominal denda sesuai jenis item.
        """
        raise NotImplementedError

    def __str__(self) -> str:
        """Mengembalikan representasi singkat item."""
        return f"{self.jenis} {self.item_id} - {self.judul}"


class Book(LibraryItem):
    """Item perpustakaan berupa buku."""

    JENIS = "Buku"

    def __init__(
        self,
        item_id: str,
        judul: str,
        tahun: int,
        penulis: str,
        jumlah_halaman: int,
    ):
        """Menginisialisasi data buku.

        Parameter:
            item_id (str): ID unik buku.
            judul (str): Judul buku.
            tahun (int): Tahun terbit buku.
            penulis (str): Nama penulis buku.
            jumlah_halaman (int): Jumlah halaman buku.
        """
        super().__init__(item_id, judul, tahun)
        self.__penulis = penulis
        self.__jumlah_halaman = jumlah_halaman

    @property
    def penulis(self) -> str:
        """Mengembalikan nama penulis buku."""
        return self.__penulis

    @property
    def jumlah_halaman(self) -> int:
        """Mengembalikan jumlah halaman buku."""
        return self.__jumlah_halaman

    def get_detail(self) -> str:
        """Mengembalikan detail buku beserta statusnya."""
        status = "Dipinjam" if self.is_dipinjam else "Tersedia"
        return (
            f"[Buku] {self.item_id} | {self.judul} ({self.tahun}) | "
            f"Penulis: {self.penulis} | {self.jumlah_halaman} hlm | "
            f"{status}"
        )

    def hitung_denda(self, hari_terlambat: int) -> float:
        """Menghitung denda buku sebesar Rp1.000 per hari."""
        return max(0, hari_terlambat) * 1000


class Magazine(LibraryItem):
    """Item perpustakaan berupa majalah."""

    JENIS = "Majalah"

    def __init__(
        self,
        item_id: str,
        judul: str,
        tahun: int,
        edisi: str,
        penerbit: str,
    ):
        """Menginisialisasi data majalah.

        Parameter:
            item_id (str): ID unik majalah.
            judul (str): Judul majalah.
            tahun (int): Tahun terbit majalah.
            edisi (str): Edisi majalah, misalnya "Januari 2024".
            penerbit (str): Nama penerbit majalah.
        """
        super().__init__(item_id, judul, tahun)
        self.__edisi = edisi
        self.__penerbit = penerbit

    @property
    def edisi(self) -> str:
        """Mengembalikan edisi majalah."""
        return self.__edisi

    @property
    def penerbit(self) -> str:
        """Mengembalikan nama penerbit majalah."""
        return self.__penerbit

    def get_detail(self) -> str:
        """Mengembalikan detail majalah beserta statusnya."""
        status = "Dipinjam" if self.is_dipinjam else "Tersedia"
        return (
            f"[Majalah] {self.item_id} | {self.judul} ({self.tahun}) | "
            f"Edisi: {self.edisi} | Penerbit: {self.penerbit} | "
            f"{status}"
        )

    def hitung_denda(self, hari_terlambat: int) -> float:
        """Menghitung denda majalah sebesar Rp500 per hari."""
        return max(0, hari_terlambat) * 500
