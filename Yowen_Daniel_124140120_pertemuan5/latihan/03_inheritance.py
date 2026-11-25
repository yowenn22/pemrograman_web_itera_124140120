"""
Latihan 03: Inheritance (Pewarisan).

Subclass mewarisi atribut dan method dari superclass, lalu dapat
menambahkan atau mengubah perilakunya sendiri.
"""


class Kendaraan:
    """Superclass untuk semua jenis kendaraan."""

    def __init__(self, merk: str, tahun: int):
        """Menginisialisasi data kendaraan.

        Parameter:
            merk (str): Merek kendaraan.
            tahun (int): Tahun pembuatan kendaraan.
        """
        self.merk = merk
        self.tahun = tahun

    def info(self) -> str:
        """Mengembalikan informasi dasar kendaraan.

        Return:
            str: Informasi kendaraan.
        """
        return f"{self.merk} ({self.tahun})"


class Mobil(Kendaraan):
    """Kendaraan roda empat yang mewarisi class Kendaraan."""

    def __init__(self, merk: str, tahun: int, jumlah_pintu: int):
        """Menginisialisasi data mobil.

        Parameter:
            merk (str): Merek mobil.
            tahun (int): Tahun pembuatan mobil.
            jumlah_pintu (int): Jumlah pintu mobil.
        """
        super().__init__(merk, tahun)
        self.jumlah_pintu = jumlah_pintu

    def info(self) -> str:
        """Menambahkan jumlah pintu pada informasi mobil.

        Return:
            str: Informasi mobil lengkap.
        """
        return f"Mobil {super().info()} - {self.jumlah_pintu} pintu"


class Motor(Kendaraan):
    """Kendaraan roda dua yang mewarisi class Kendaraan."""

    def __init__(self, merk: str, tahun: int, jenis: str):
        """Menginisialisasi data motor.

        Parameter:
            merk (str): Merek motor.
            tahun (int): Tahun pembuatan motor.
            jenis (str): Jenis motor, misalnya matic atau bebek.
        """
        super().__init__(merk, tahun)
        self.jenis = jenis

    def info(self) -> str:
        """Menambahkan jenis pada informasi motor.

        Return:
            str: Informasi motor lengkap.
        """
        return f"Motor {super().info()} - jenis {self.jenis}"


def main() -> None:
    """Menampilkan informasi setiap kendaraan.

    Return:
        None
    """
    print("=" * 60)
    print("LATIHAN 03: INHERITANCE".center(60))
    print("=" * 60)

    daftar = [
        Mobil("Toyota Avanza", 2020, 4),
        Motor("Honda Vario", 2022, "matic"),
    ]

    for kendaraan in daftar:
        print(f"- {kendaraan.info()}")

    print("-" * 60)
    print(f"Mobil subclass dari Kendaraan: {issubclass(Mobil, Kendaraan)}")
    print(f"Motor subclass dari Kendaraan: {issubclass(Motor, Kendaraan)}")


if __name__ == "__main__":
    main()
