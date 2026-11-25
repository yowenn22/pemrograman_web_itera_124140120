"""
Program Utama Penggunaan Modul math_operations.

Nama : Yowen Daniel
NIM  : 124140120

Berkas ini mengimpor modul math_operations dengan dua cara berbeda:
1. `import math_operations` untuk memanggil fungsi geometri.
2. `from math_operations import ...` untuk memanggil fungsi konversi suhu.
Seluruh fungsi pada modul diuji dan hasilnya ditampilkan di terminal.
"""

import math_operations
from math_operations import celsius_ke_fahrenheit, celsius_ke_kelvin


def tampilkan_judul(judul: str) -> None:
    """Mencetak judul bagian agar keluaran terminal lebih rapi.

    Parameter:
        judul (str): Teks judul yang akan ditampilkan.

    Return:
        None: Fungsi hanya mencetak teks ke terminal.
    """
    print("\n" + "=" * 60)
    print(judul.center(60))
    print("=" * 60)


def tampilkan_identitas() -> None:
    """Menampilkan identitas mahasiswa dan konstanta modul.

    Return:
        None: Fungsi hanya mencetak teks ke terminal.
    """
    print("=" * 60)
    print("PROGRAM MATEMATIKA - PERTEMUAN 4".center(60))
    print("=" * 60)
    print("Nama         : Yowen Daniel")
    print("NIM          : 124140120")
    print(f"Konstanta PI : {math_operations.PI}")


def tampilkan_hasil_geometri() -> None:
    """Menguji fungsi luas dan keliling bangun datar dari modul.

    Fungsi geometri dipanggil melalui `import math_operations`.

    Return:
        None: Fungsi hanya mencetak hasil perhitungan ke terminal.
    """
    tampilkan_judul("BANGUN DATAR")

    sisi_persegi = 5.0
    print(f"--- Persegi (sisi = {sisi_persegi:.1f}) ---")
    print(
        f"Luas persegi     : "
        f"{math_operations.luas_persegi(sisi_persegi):.2f}"
    )
    print(
        f"Keliling persegi : "
        f"{math_operations.keliling_persegi(sisi_persegi):.2f}"
    )

    panjang = 8.0
    lebar = 4.0
    print(f"\n--- Persegi panjang (panjang = {panjang:.1f}, "
          f"lebar = {lebar:.1f}) ---")
    print(
        f"Luas persegi panjang     : "
        f"{math_operations.luas_persegi_panjang(panjang, lebar):.2f}"
    )
    print(
        f"Keliling persegi panjang : "
        f"{math_operations.keliling_persegi_panjang(panjang, lebar):.2f}"
    )

    jari_jari = 7.0
    print(f"\n--- Lingkaran (jari-jari = {jari_jari:.1f}) ---")
    print(
        f"Luas lingkaran     : "
        f"{math_operations.luas_lingkaran(jari_jari):.2f}"
    )
    print(
        f"Keliling lingkaran : "
        f"{math_operations.keliling_lingkaran(jari_jari):.2f}"
    )


def tampilkan_hasil_suhu() -> None:
    """Menguji fungsi konversi suhu dari modul.

    Fungsi konversi dipanggil melalui `from math_operations import ...`.

    Return:
        None: Fungsi hanya mencetak hasil perhitungan ke terminal.
    """
    tampilkan_judul("KONVERSI SUHU")
    print(f"{'Celsius':>10}{'Fahrenheit':>15}{'Kelvin':>12}")
    print("-" * 37)

    daftar_celsius = [0.0, 25.0, 100.0]
    for celsius in daftar_celsius:
        fahrenheit = celsius_ke_fahrenheit(celsius)
        kelvin = celsius_ke_kelvin(celsius)
        print(f"{celsius:>10.1f}{fahrenheit:>15.2f}{kelvin:>12.2f}")


def main() -> None:
    """Menjalankan seluruh demonstrasi penggunaan modul matematika.

    Return:
        None: Fungsi utama tidak mengembalikan nilai.
    """
    tampilkan_identitas()
    tampilkan_hasil_geometri()
    tampilkan_hasil_suhu()
    print("\n" + "=" * 60)
    pesan_selesai = (
        "SELESAI: seluruh fungsi math_operations berhasil dipanggil."
    )
    print(pesan_selesai.center(60))
    print("=" * 60)


if __name__ == "__main__":
    main()
