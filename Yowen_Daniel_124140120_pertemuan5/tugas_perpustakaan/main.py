"""
Program utama Sistem Manajemen Perpustakaan Sederhana.

Nama  : Yowen Daniel
NIM   : 124140120
Kelas : RA
"""

from library import Library
from library_item import Book, Magazine
from member import Member


def cetak_judul(judul: str) -> None:
    """Mencetak judul bagian agar output terminal lebih rapi.

    Parameter:
        judul (str): Teks judul bagian.

    Return:
        None
    """
    print("\n" + "=" * 70)
    print(judul.center(70))
    print("=" * 70)


def main() -> None:
    """Menjalankan seluruh demonstrasi fitur perpustakaan.

    Return:
        None
    """
    perpustakaan = Library("Perpustakaan ITERA")

    print("=" * 70)
    print("SISTEM MANAJEMEN PERPUSTAKAAN SEDERHANA".center(70))
    print("=" * 70)
    print("Nama  : Yowen Daniel")
    print("NIM   : 124140120")
    print("Kelas : RA")

    cetak_judul("1. MENDAFTARKAN ANGGOTA DAN MENAMBAHKAN ITEM")
    anggota_1 = Member("AGT001", "Yowen Daniel")
    anggota_2 = Member("AGT002", "Siti Rahma")
    perpustakaan.tambah_anggota(anggota_1)
    perpustakaan.tambah_anggota(anggota_2)

    daftar_item = [
        Book(
            "B001",
            "Laskar Pelangi",
            2005,
            "Andrea Hirata",
            529,
        ),
        Book(
            "B002",
            "Bumi Manusia",
            1980,
            "Pramoedya Ananta Toer",
            535,
        ),
        Book(
            "B003",
            "Atomic Habits",
            2018,
            "James Clear",
            320,
        ),
        Magazine(
            "M001",
            "National Geographic Indonesia",
            2024,
            "Januari 2024",
            "National Geographic",
        ),
        Magazine(
            "M002",
            "Tempo",
            2024,
            "12/2024",
            "Tempo",
        ),
        Magazine(
            "M003",
            "Bobo",
            2024,
            "45/2024",
            "Kompas Gramedia",
        ),
    ]
    for item in daftar_item:
        perpustakaan.tambah_item(item)
    print(f"\nTotal item terdaftar: {perpustakaan.jumlah_item}")

    cetak_judul("2. KATALOG SELURUH ITEM")
    perpustakaan.tampilkan_katalog()

    cetak_judul("3. PENCARIAN ITEM")
    print("Pencarian berdasarkan judul: 'bumi'")
    hasil_judul = perpustakaan.cari_item("bumi")
    if hasil_judul:
        for item in hasil_judul:
            print(f"  -> {item.get_detail()}")
    else:
        print("  -> Tidak ada item yang cocok.")

    print("\nPencarian berdasarkan ID: 'M002'")
    hasil_id = perpustakaan.cari_item("M002")
    if hasil_id:
        for item in hasil_id:
            print(f"  -> {item.get_detail()}")
    else:
        print("  -> Tidak ada item yang cocok.")

    print("\nPencarian judul yang tidak ada: 'ensiklopedia'")
    hasil_kosong = perpustakaan.cari_item("ensiklopedia")
    if hasil_kosong:
        for item in hasil_kosong:
            print(f"  -> {item.get_detail()}")
    else:
        print("  -> Tidak ada item yang cocok.")

    cetak_judul("4. STATUS KETERSEDIAAN ITEM")
    print(f"Meminjam B001 oleh {anggota_1.nama}:")
    perpustakaan.pinjam_item("B001", anggota_1)
    print(f"\nMeminjam M002 oleh {anggota_2.nama}:")
    perpustakaan.pinjam_item("M002", anggota_2)

    print("\nItem yang masih tersedia:")
    perpustakaan.tampilkan_item_tersedia()

    print(f"\nMengembalikan M002 oleh {anggota_2.nama}:")
    perpustakaan.kembalikan_item("M002", anggota_2)
    hasil_m002 = perpustakaan.cari_item("M002")
    if hasil_m002:
        print(f"Status M002 sekarang: {hasil_m002[0].get_detail()}")

    print(f"\nMencoba meminjam B001 lagi oleh {anggota_2.nama}:")
    perpustakaan.pinjam_item("B001", anggota_2)

    cetak_judul("5. POLYMORPHISM: PERHITUNGAN DENDA")
    print("Denda untuk keterlambatan 3 hari:")
    for item in perpustakaan.koleksi:
        denda = item.hitung_denda(3)
        print(
            f"  - {item.jenis:<8} {item.judul:<32} : "
            f"Rp {denda:,.0f}"
        )

    cetak_judul("6. RINGKASAN")
    total = perpustakaan.jumlah_item
    dipinjam = sum(1 for item in perpustakaan.koleksi if item.is_dipinjam)
    tersedia = total - dipinjam
    print(f"Total item      : {total}")
    print(f"Item tersedia   : {tersedia}")
    print(f"Item dipinjam   : {dipinjam}")
    pinjaman_1 = ", ".join(anggota_1.pinjaman) or "Tidak ada"
    pinjaman_2 = ", ".join(anggota_2.pinjaman) or "Tidak ada"
    print(f"Pinjaman {anggota_1.nama:<14}: {pinjaman_1}")
    print(f"Pinjaman {anggota_2.nama:<14}: {pinjaman_2}")


if __name__ == "__main__":
    main()
