"""
Latihan 06: Abstract Class dan Interface.

Abstract class tidak dapat diinstansiasi langsung. Setiap subclass
wajib mengimplementasikan seluruh method yang ditandai
@abstractmethod.
"""

from abc import ABC, abstractmethod


class BangunDatar(ABC):
    """Abstract class untuk bangun datar."""

    def __init__(self, nama: str):
        """Menginisialisasi nama bangun datar.

        Parameter:
            nama (str): Nama bangun datar.
        """
        self.nama = nama

    @abstractmethod
    def luas(self) -> float:
        """Menghitung luas bangun (wajib diimplementasikan).

        Return:
            float: Luas bangun datar.
        """
        raise NotImplementedError

    @abstractmethod
    def keliling(self) -> float:
        """Menghitung keliling bangun (wajib diimplementasikan).

        Return:
            float: Keliling bangun datar.
        """
        raise NotImplementedError

    def laporan(self) -> str:
        """Membuat laporan luas dan keliling bangun.

        Return:
            str: Ringkasan hasil perhitungan.
        """
        return (
            f"{self.nama:<12} luas = {self.luas():>8.2f} | "
            f"keliling = {self.keliling():>8.2f}"
        )


class Persegi(BangunDatar):
    """Bangun datar persegi."""

    def __init__(self, sisi: float):
        """Menginisialisasi panjang sisi persegi.

        Parameter:
            sisi (float): Panjang sisi persegi.
        """
        super().__init__("Persegi")
        self.sisi = sisi

    def luas(self) -> float:
        """Menghitung luas persegi.

        Return:
            float: Hasil sisi * sisi.
        """
        return self.sisi ** 2

    def keliling(self) -> float:
        """Menghitung keliling persegi.

        Return:
            float: Hasil 4 * sisi.
        """
        return 4 * self.sisi


class Lingkaran(BangunDatar):
    """Bangun datar lingkaran."""

    def __init__(self, jari_jari: float):
        """Menginisialisasi jari-jari lingkaran.

        Parameter:
            jari_jari (float): Panjang jari-jari lingkaran.
        """
        super().__init__("Lingkaran")
        self.jari_jari = jari_jari

    def luas(self) -> float:
        """Menghitung luas lingkaran.

        Return:
            float: Hasil pi * r^2.
        """
        return 3.14159 * self.jari_jari ** 2

    def keliling(self) -> float:
        """Menghitung keliling lingkaran.

        Return:
            float: Hasil 2 * pi * r.
        """
        return 2 * 3.14159 * self.jari_jari


def main() -> None:
    """Menguji abstract class dan implementasinya.

    Return:
        None
    """
    print("=" * 60)
    print("LATIHAN 06: ABSTRACT CLASS".center(60))
    print("=" * 60)

    daftar = [Persegi(5), Lingkaran(7)]

    for bangun in daftar:
        print(f"- {bangun.laporan()}")

    print("-" * 60)
    print("Mencoba membuat object dari abstract class:")
    try:
        gagal = BangunDatar("Tidak Bisa")
        print(gagal)
    except TypeError as error:
        print(f"TypeError: {error}")


if __name__ == "__main__":
    main()
