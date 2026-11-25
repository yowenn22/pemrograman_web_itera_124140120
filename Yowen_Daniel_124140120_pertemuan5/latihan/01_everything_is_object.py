"""
Latihan 1: Everything is Object.

Di Python, semua nilai (angka, teks, list, bahkan fungsi) adalah
object. Setiap object memiliki tipe (type) dan identitas (id).
"""


def main() -> None:
    """Menampilkan tipe dan identitas beberapa object Python.

    Return:
        None
    """
    nilai = [100, 3.14, "Python", True, [1, 2, 3]]

    print("=" * 60)
    print("LATIHAN 01: EVERYTHING IS OBJECT".center(60))
    print("=" * 60)
    print(f"{'Nilai':<20}{'Tipe':<15}{'id()'}")
    print("-" * 60)

    for data in nilai:
        print(f"{str(data):<20}{type(data).__name__:<15}{id(data)}")

    print("-" * 60)
    print("Semua nilai di atas adalah object dari sebuah class.")


if __name__ == "__main__":
    main()
