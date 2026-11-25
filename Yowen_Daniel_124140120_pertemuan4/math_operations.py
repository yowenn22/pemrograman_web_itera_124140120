"""
Modul Matematika Python.

Nama : Yowen Daniel
NIM  : 124140120

Modul ini menyediakan fungsi luas dan keliling bangun datar
(persegi, persegi panjang, lingkaran) serta fungsi konversi suhu.
Seluruh fungsi di dalam modul ini dipanggil oleh berkas main.py.
"""

# Konstanta nilai PI yang dipakai untuk perhitungan lingkaran.
PI = 3.14159


def luas_persegi(sisi: float) -> float:
    """Menghitung luas persegi.

    Parameter:
        sisi (float): Panjang sisi persegi.

    Return:
        float: Luas persegi dengan rumus sisi * sisi.
    """
    return sisi * sisi


def keliling_persegi(sisi: float) -> float:
    """Menghitung keliling persegi.

    Parameter:
        sisi (float): Panjang sisi persegi.

    Return:
        float: Keliling persegi dengan rumus 4 * sisi.
    """
    return 4 * sisi


def luas_persegi_panjang(panjang: float, lebar: float) -> float:
    """Menghitung luas persegi panjang.

    Parameter:
        panjang (float): Panjang persegi panjang.
        lebar (float): Lebar persegi panjang.

    Return:
        float: Luas persegi panjang dengan rumus panjang * lebar.
    """
    return panjang * lebar


def keliling_persegi_panjang(panjang: float, lebar: float) -> float:
    """Menghitung keliling persegi panjang.

    Parameter:
        panjang (float): Panjang persegi panjang.
        lebar (float): Lebar persegi panjang.

    Return:
        float: Keliling dengan rumus 2 * (panjang + lebar).
    """
    return 2 * (panjang + lebar)


def luas_lingkaran(jari_jari: float) -> float:
    """Menghitung luas lingkaran menggunakan konstanta PI.

    Parameter:
        jari_jari (float): Panjang jari-jari lingkaran.

    Return:
        float: Luas lingkaran dengan rumus PI * jari_jari ** 2.
    """
    return PI * (jari_jari ** 2)


def keliling_lingkaran(jari_jari: float) -> float:
    """Menghitung keliling lingkaran menggunakan konstanta PI.

    Parameter:
        jari_jari (float): Panjang jari-jari lingkaran.

    Return:
        float: Keliling lingkaran dengan rumus 2 * PI * jari_jari.
    """
    return 2 * PI * jari_jari


def celsius_ke_fahrenheit(celsius: float) -> float:
    """Mengonversi suhu dari Celsius ke Fahrenheit.

    Parameter:
        celsius (float): Suhu dalam derajat Celsius.

    Return:
        float: Suhu dalam derajat Fahrenheit.
    """
    return (celsius * 9 / 5) + 32


def celsius_ke_kelvin(celsius: float) -> float:
    """Mengonversi suhu dari Celsius ke Kelvin.

    Parameter:
        celsius (float): Suhu dalam derajat Celsius.

    Return:
        float: Suhu dalam Kelvin.
    """
    return celsius + 273.15
