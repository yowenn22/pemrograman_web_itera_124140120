"""
Latihan 05: Polymorphism dan Method Overriding.

Beberapa subclass dapat memiliki method dengan nama sama tetapi
perilaku berbeda. Pemanggilan method yang sama akan menghasilkan
output yang menyesuaikan tipe object.
"""


class Hewan:
    """Class dasar untuk semua hewan."""

    def __init__(self, nama: str):
        """Menginisialisasi nama hewan.

        Parameter:
            nama (str): Nama hewan.
        """
        self.nama = nama

    def suara(self) -> str:
        """Mengembalikan suara hewan (akan di-override subclass).

        Return:
            str: Suara hewan.
        """
        return "..."

    def intro(self) -> str:
        """Membuat kalimat perkenalan hewan.

        Return:
            str: Kalimat berisi nama dan suara hewan.
        """
        return f"{self.nama} bersuara '{self.suara()}'"


class Kucing(Hewan):
    """Hewan kucing."""

    def suara(self) -> str:
        """Mengembalikan suara kucing.

        Return:
            str: Suara kucing.
        """
        return "Meong"


class Anjing(Hewan):
    """Hewan anjing."""

    def suara(self) -> str:
        """Mengembalikan suara anjing.

        Return:
            str: Suara anjing.
        """
        return "Guk guk"


class Sapi(Hewan):
    """Hewan sapi."""

    def suara(self) -> str:
        """Mengembalikan suara sapi.

        Return:
            str: Suara sapi.
        """
        return "Mooo"


def main() -> None:
    """Memanggil method yang sama pada object berbeda.

    Return:
        None
    """
    print("=" * 60)
    print("LATIHAN 05: POLYMORPHISM".center(60))
    print("=" * 60)

    daftar_hewan = [
        Kucing("Kitty"),
        Anjing("Buddy"),
        Sapi("Molly"),
    ]

    for hewan in daftar_hewan:
        print(f"- {hewan.intro()}")

    print("-" * 60)
    print("Method suara() dipanggil dengan cara yang sama, tetapi")
    print("hasilnya berbeda sesuai tipe object (polymorphism).")


if __name__ == "__main__":
    main()
