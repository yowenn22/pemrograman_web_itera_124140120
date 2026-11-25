"""
Program Pengelolaan Data Nilai Mahasiswa.

Nama : Yowen Daniel
NIM  : 124140120

Program ini menyimpan data mahasiswa dalam list berisi dictionary,
menghitung nilai akhir dengan bobot 30% UTS + 40% UAS + 30% tugas,
menentukan grade A sampai E, menampilkan tabel, serta mencari nilai
akhir tertinggi dan terendah.
"""


def hitung_nilai_akhir(
    nilai_uts: float, nilai_uas: float, nilai_tugas: float
) -> float:
    """Menghitung nilai akhir mahasiswa sesuai bobot persentase.

    Parameter:
        nilai_uts (float): Nilai Ujian Tengah Semester (bobot 30%).
        nilai_uas (float): Nilai Ujian Akhir Semester (bobot 40%).
        nilai_tugas (float): Nilai tugas (bobot 30%).

    Return:
        float: Nilai akhir hasil perhitungan bobot.
    """
    return (0.30 * nilai_uts) + (0.40 * nilai_uas) + (0.30 * nilai_tugas)


def tentukan_grade(nilai_akhir: float) -> str:
    """Menentukan grade mahasiswa berdasarkan nilai akhir.

    Parameter:
        nilai_akhir (float): Nilai akhir mahasiswa.

    Return:
        str: Grade A, B, C, D, atau E.
    """
    if nilai_akhir >= 80:
        return "A"
    elif nilai_akhir >= 70:
        return "B"
    elif nilai_akhir >= 60:
        return "C"
    elif nilai_akhir >= 50:
        return "D"
    else:
        return "E"


def olah_data_mahasiswa(daftar_mahasiswa: list) -> list:
    """Menambahkan nilai akhir dan grade pada setiap data mahasiswa.

    Parameter:
        daftar_mahasiswa (list): List berisi dictionary data mahasiswa.

    Return:
        list: List baru berisi data mahasiswa lengkap dengan nilai akhir
            dan grade. Data asli tidak diubah.
    """
    hasil = []
    for mahasiswa in daftar_mahasiswa:
        data = mahasiswa.copy()
        data["nilai_akhir"] = hitung_nilai_akhir(
            data["nilai_uts"], data["nilai_uas"], data["nilai_tugas"]
        )
        data["grade"] = tentukan_grade(data["nilai_akhir"])
        hasil.append(data)
    return hasil


def tampilkan_tabel(daftar_mahasiswa: list) -> None:
    """Menampilkan seluruh data mahasiswa dalam bentuk tabel.

    Parameter:
        daftar_mahasiswa (list): List data mahasiswa yang sudah diolah.

    Return:
        None: Fungsi hanya mencetak tabel ke terminal.
    """
    lebar = 70
    print("=" * lebar)
    print("DAFTAR NILAI MAHASISWA".center(lebar))
    print("=" * lebar)
    print(
        f"{'No':<4}{'Nama':<20}{'NIM':<12}"
        f"{'UTS':>6}{'UAS':>6}{'Tugas':>7}{'Akhir':>8}{'Grade':>7}"
    )
    print("-" * lebar)

    for nomor, mahasiswa in enumerate(daftar_mahasiswa, start=1):
        print(
            f"{nomor:<4}{mahasiswa['nama']:<20}{mahasiswa['nim']:<12}"
            f"{mahasiswa['nilai_uts']:>6.1f}"
            f"{mahasiswa['nilai_uas']:>6.1f}"
            f"{mahasiswa['nilai_tugas']:>7.1f}"
            f"{mahasiswa['nilai_akhir']:>8.2f}"
            f"{mahasiswa['grade']:>7}"
        )

    print("-" * lebar)


def cari_nilai_tertinggi(daftar_mahasiswa: list) -> dict:
    """Mencari mahasiswa dengan nilai akhir tertinggi.

    Parameter:
        daftar_mahasiswa (list): List data mahasiswa yang sudah diolah.

    Return:
        dict: Dictionary milik mahasiswa dengan nilai akhir tertinggi.
    """
    return max(
        daftar_mahasiswa, key=lambda mahasiswa: mahasiswa["nilai_akhir"]
    )


def cari_nilai_terendah(daftar_mahasiswa: list) -> dict:
    """Mencari mahasiswa dengan nilai akhir terendah.

    Parameter:
        daftar_mahasiswa (list): List data mahasiswa yang sudah diolah.

    Return:
        dict: Dictionary milik mahasiswa dengan nilai akhir terendah.
    """
    return min(
        daftar_mahasiswa, key=lambda mahasiswa: mahasiswa["nilai_akhir"]
    )


def main() -> None:
    """Menjalankan seluruh alur program pengelolaan nilai mahasiswa.

    Return:
        None: Fungsi utama tidak mengembalikan nilai.
    """
    data_mahasiswa = [
        {
            "nama": "Andi Pratama",
            "nim": "124140101",
            "nilai_uts": 85.0,
            "nilai_uas": 90.0,
            "nilai_tugas": 88.0,
        },
        {
            "nama": "Budi Santoso",
            "nim": "124140102",
            "nilai_uts": 75.0,
            "nilai_uas": 80.0,
            "nilai_tugas": 78.0,
        },
        {
            "nama": "Citra Lestari",
            "nim": "124140103",
            "nilai_uts": 65.0,
            "nilai_uas": 70.0,
            "nilai_tugas": 68.0,
        },
        {
            "nama": "Dewi Anggraini",
            "nim": "124140104",
            "nilai_uts": 55.0,
            "nilai_uas": 58.0,
            "nilai_tugas": 60.0,
        },
        {
            "nama": "Eko Nugroho",
            "nim": "124140105",
            "nilai_uts": 40.0,
            "nilai_uas": 45.0,
            "nilai_tugas": 50.0,
        },
    ]

    data_terolah = olah_data_mahasiswa(data_mahasiswa)
    tampilkan_tabel(data_terolah)

    tertinggi = cari_nilai_tertinggi(data_terolah)
    terendah = cari_nilai_terendah(data_terolah)

    print("\nRINGKASAN NILAI EKSTREM")
    print("-" * 70)
    print(
        f"Nilai akhir tertinggi : {tertinggi['nama']} "
        f"({tertinggi['nim']}) = {tertinggi['nilai_akhir']:.2f} "
        f"(Grade {tertinggi['grade']})"
    )
    print(
        f"Nilai akhir terendah  : {terendah['nama']} "
        f"({terendah['nim']}) = {terendah['nilai_akhir']:.2f} "
        f"(Grade {terendah['grade']})"
    )
    print("-" * 70)


if __name__ == "__main__":
    main()
