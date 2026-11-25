"""
Latihan 02: Class dan Object.

Class adalah blueprint, sedangkan object adalah instance nyata
yang dibuat dari class tersebut.
"""


class Mahasiswa:
    """Merepresentasikan data seorang mahasiswa."""

    # Atribut class: dimiliki bersama oleh semua object.
    kampus = "Institut Teknologi Sumatera"

    def __init__(self, nama: str, nim: str, prodi: str):
        """Menginisialisasi atribut instance mahasiswa.

        Parameter:
            nama (str): Nama lengkap mahasiswa.
            nim (str): Nomor Induk Mahasiswa.
            prodi (str): Program studi mahasiswa.
        """
        self.nama = nama
        self.nim = nim
        self.prodi = prodi

    def perkenalan(self) -> str:
        """Membuat teks perkenalan mahasiswa.

        Return:
            str: Kalimat perkenalan.
        """
        return (
            f"Halo, saya {self.nama} ({self.nim}) "
            f"dari {self.prodi}, {self.kampus}."
        )


def main() -> None:
    """Membuat beberapa object Mahasiswa dan menampilkan datanya.

    Return:
        None
    """
    print("=" * 60)
    print("LATIHAN 02: CLASS DAN OBJECT".center(60))
    print("=" * 60)

    mhs_1 = Mahasiswa("Yowen Daniel", "124140120", "Informatika")
    mhs_2 = Mahasiswa("Siti Rahma", "124140121", "Sistem Informasi")

    for mahasiswa in (mhs_1, mhs_2):
        print(mahasiswa.perkenalan())

    print("-" * 60)
    print(f"Atribut class kampus : {Mahasiswa.kampus}")
    print(f"Jumlah object dibuat : 2")


if __name__ == "__main__":
    main()
