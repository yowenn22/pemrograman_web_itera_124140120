"""
Latihan 01: Procedural vs Object-Oriented Programming.

Program procedural menyimpan data dan fungsi secara terpisah,
sedangkan OOP membungkus keduanya di dalam class.
"""


# ---------- Pendekatan procedural ----------
def hitung_luas_procedural(panjang: float, lebar: float) -> float:
    """Menghitung luas persegi panjang secara procedural.

    Parameter:
        panjang (float): Panjang persegi panjang.
        lebar (float): Lebar persegi panjang.

    Return:
        float: Luas persegi panjang.
    """
    return panjang * lebar


# ---------- Pendekatan OOP ----------
class PersegiPanjang:
    """Persegi panjang dengan data dan perilaku di dalam satu class."""

    def __init__(self, panjang: float, lebar: float):
        """Menginisialisasi ukuran persegi panjang.

        Parameter:
            panjang (float): Panjang persegi panjang.
            lebar (float): Lebar persegi panjang.
        """
        self.panjang = panjang
        self.lebar = lebar

    def luas(self) -> float:
        """Menghitung luas persegi panjang.

        Return:
            float: Hasil perkalian panjang dan lebar.
        """
        return self.panjang * self.lebar


def main() -> None:
    """Membandingkan kedua pendekatan.

    Return:
        None
    """
    print("=" * 60)
    print("LATIHAN 01: PROCEDURAL VS OOP".center(60))
    print("=" * 60)

    panjang, lebar = 8.0, 4.0
    print("Procedural:")
    print(f"  Luas = {hitung_luas_procedural(panjang, lebar):.2f}")

    kotak = PersegiPanjang(panjang, lebar)
    print("\nOOP:")
    print(f"  Objek      : {kotak}")
    print(f"  Panjang    : {kotak.panjang}")
    print(f"  Lebar      : {kotak.lebar}")
    print(f"  Luas       : {kotak.luas():.2f}")
    print("\nData dan fungsi pada OOP berada dalam satu kesatuan.")


if __name__ == "__main__":
    main()
