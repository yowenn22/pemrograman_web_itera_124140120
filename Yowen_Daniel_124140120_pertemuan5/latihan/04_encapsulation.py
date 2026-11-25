"""
Latihan 04: Encapsulation dan Property.

Atribut private ditandai dengan dua garis bawah di depan nama
(__saldo). Akses dilakukan melalui method atau @property agar
data tetap terkontrol.
"""


class RekeningBank:
    """Rekening bank sederhana dengan saldo private."""

    def __init__(self, nomor: str, pemilik: str, saldo_awal: float = 0):
        """Menginisialisasi rekening.

        Parameter:
            nomor (str): Nomor rekening.
            pemilik (str): Nama pemilik rekening.
            saldo_awal (float): Saldo awal, default 0.
        """
        self.__nomor = nomor
        self.__pemilik = pemilik
        self.__saldo = max(0.0, saldo_awal)

    @property
    def nomor(self) -> str:
        """Mengembalikan nomor rekening."""
        return self.__nomor

    @property
    def pemilik(self) -> str:
        """Mengembalikan nama pemilik rekening."""
        return self.__pemilik

    @property
    def saldo(self) -> float:
        """Mengembalikan saldo terkini (read-only dari luar)."""
        return self.__saldo

    def setor(self, jumlah: float) -> bool:
        """Menambah saldo rekening.

        Parameter:
            jumlah (float): Nominal uang yang disetor.

        Return:
            bool: True jika berhasil, False jika nominal tidak valid.
        """
        if jumlah <= 0:
            print("Gagal: nominal setor harus lebih dari 0.")
            return False
        self.__saldo += jumlah
        print(f"[OK] Setor Rp {jumlah:,.0f}. Saldo: Rp {self.__saldo:,.0f}")
        return True

    def tarik(self, jumlah: float) -> bool:
        """Mengurangi saldo rekening.

        Parameter:
            jumlah (float): Nominal uang yang ditarik.

        Return:
            bool: True jika berhasil, False jika saldo tidak cukup.
        """
        if jumlah <= 0:
            print("Gagal: nominal tarik harus lebih dari 0.")
            return False
        if jumlah > self.__saldo:
            print("Gagal: saldo tidak mencukupi.")
            return False
        self.__saldo -= jumlah
        print(f"[OK] Tarik Rp {jumlah:,.0f}. Saldo: Rp {self.__saldo:,.0f}")
        return True


def main() -> None:
    """Mendemonstrasikan akses saldo melalui property.

    Return:
        None
    """
    print("=" * 60)
    print("LATIHAN 04: ENCAPSULATION DAN PROPERTY".center(60))
    print("=" * 60)

    rekening = RekeningBank("123456789", "Yowen Daniel", 500000)
    print(f"Pemilik : {rekening.pemilik}")
    print(f"Nomor   : {rekening.nomor}")
    print(f"Saldo   : Rp {rekening.saldo:,.0f}")

    print("\nTransaksi:")
    rekening.setor(250000)
    rekening.tarik(100000)
    rekening.tarik(5000000)

    print("\nAkses langsung atribut private:")
    try:
        print(rekening.__saldo)
    except AttributeError as error:
        print(f"AttributeError: {error}")
    print(f"Saldo aman tetap terbaca via property: "
          f"Rp {rekening.saldo:,.0f}")


if __name__ == "__main__":
    main()
