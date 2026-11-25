"""
Program Penghitung BMI (Body Mass Index) Sederhana.

Nama : Yowen Daniel
NIM  : 124140120

Program ini menghitung nilai BMI berdasarkan berat badan (kg) dan
tinggi badan (m), lalu menampilkan kategori status berat badan
menggunakan struktur percabangan if-elif-else.
"""


def hitung_bmi(berat_kg: float, tinggi_m: float) -> float:
    """Menghitung nilai BMI berdasarkan berat dan tinggi badan.

    Parameter:
        berat_kg (float): Berat badan dalam satuan kilogram (kg).
        tinggi_m (float): Tinggi badan dalam satuan meter (m).

    Return:
        float: Nilai BMI dengan rumus berat / (tinggi * tinggi).

    Raises:
        ValueError: Jika tinggi_m bernilai nol atau negatif.
    """
    if tinggi_m <= 0:
        raise ValueError("Tinggi badan harus lebih dari 0 meter.")
    return berat_kg / (tinggi_m * tinggi_m)


def kategori_bmi(bmi: float) -> str:
    """Menentukan kategori status berat badan dari nilai BMI.

    Parameter:
        bmi (float): Nilai BMI yang sudah dihitung.

    Return:
        str: Kategori berat badan sesuai rentang nilai BMI.
    """
    if bmi < 18.5:
        return "Berat badan kurang"
    elif bmi < 25:
        return "Berat badan normal"
    elif bmi < 30:
        return "Berat badan berlebih"
    else:
        return "Obesitas"


def tampilkan_hasil(nama: str, berat_kg: float, tinggi_m: float) -> None:
    """Menghitung BMI lalu mencetak hasil dan kategorinya ke terminal.

    Parameter:
        nama (str): Nama pemilik data yang ditampilkan.
        berat_kg (float): Berat badan dalam satuan kilogram (kg).
        tinggi_m (float): Tinggi badan dalam satuan meter (m).

    Return:
        None: Fungsi hanya menampilkan hasil, tidak mengembalikan nilai.
    """
    bmi = hitung_bmi(berat_kg, tinggi_m)
    kategori = kategori_bmi(bmi)

    print("=" * 50)
    print("PROGRAM PENGHITUNG BMI".center(50))
    print("=" * 50)
    print(f"Nama         : {nama}")
    print(f"Berat badan  : {berat_kg:.1f} kg")
    print(f"Tinggi badan : {tinggi_m:.2f} m")
    print("-" * 50)
    print(f"Nilai BMI    : {bmi:.2f}")
    print(f"Kategori     : {kategori}")
    print("=" * 50)


def main() -> None:
    """Menyiapkan data uji dan menjalankan program penghitung BMI.

    Return:
        None: Fungsi utama tidak mengembalikan nilai.
    """
    nama = "Yowen Daniel"

    # Data dapat diisi langsung seperti di bawah ini.
    berat_badan_kg = 68.0
    tinggi_badan_m = 1.72

    # Alternatif: mengambil data dari pengguna melalui input().
    # berat_badan_kg = float(input("Masukkan berat badan (kg): "))
    # tinggi_badan_m = float(input("Masukkan tinggi badan (m): "))

    tampilkan_hasil(nama, berat_badan_kg, tinggi_badan_m)


if __name__ == "__main__":
    main()
