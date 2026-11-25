# Tugas Pertemuan 6 — RESTful API Manajemen Matakuliah

## Identitas

| Keterangan | Data |
| --- | --- |
| Nama Lengkap | Yowen Daniel |
| NIM | 124140120 |
| Kelas Praktikum | RA |
| Mata Kuliah | Praktikum Pengembangan Aplikasi Web |
| Tahun Ajaran | 2026/2027 — Ganjil |

## Deskripsi Aplikasi

Aplikasi ini adalah RESTful API sederhana berbasis **Pyramid Framework**,
**SQLAlchemy**, dan **PostgreSQL** untuk mengelola data **mahasiswa** dan
**mata kuliah**. Seluruh respons dikirim dalam format JSON. Aplikasi
mendukung operasi CRUD lengkap, validasi input, serta migrasi skema
database menggunakan **Alembic**.

Fitur utama:

- CRUD data mahasiswa: `GET`, `POST`, `PUT`, `DELETE`.
- CRUD data mata kuliah: `GET`, `POST`, `PUT`, `DELETE`.
- Validasi field wajib dan tipe data (HTTP `400 Bad Request`).
- Respons `404 Not Found` ketika data dengan ID tertentu tidak ada.
- `kode_mk` dan `nim` bersifat unik.
- `sks` dan `semester` wajib berupa bilangan bulat lebih besar dari nol.
- Migrasi tabel `mahasiswa` dan `matakuliah` dengan Alembic.
- Seeding data awal yang idempoten (aman dijalankan berulang).

## Teknologi

- Python 3.12
- Pyramid 2.1
- SQLAlchemy 2.x
- Alembic
- PostgreSQL 18
- Waitress
- psycopg2-binary

## Struktur Proyek

```text
Yowen_Daniel_124140120_pertemuan6/
├── development.ini
├── production.ini
├── setup.py
├── MANIFEST.in
├── README.md
├── .gitignore
├── pyramid_mahasiswa/
│   ├── __init__.py
│   ├── routes.py
│   ├── alembic/
│   │   ├── env.py
│   │   ├── script.py.mako
│   │   └── versions/
│   │       ├── 20261112_create_mahasiswa_table.py
│   │       └── 20261112_create_matakuliah_table.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── meta.py
│   │   ├── mahasiswa.py
│   │   └── matakuliah.py
│   ├── scripts/
│   │   ├── __init__.py
│   │   └── initialize_db.py
│   └── views/
│       ├── __init__.py
│       ├── default.py
│       ├── mahasiswa.py
│       ├── matakuliah.py
│       └── notfound.py
├── tests/
│   └── payloads/
│       ├── mahasiswa_create.json
│       ├── mahasiswa_update.json
│       ├── mahasiswa_invalid.json
│       ├── matakuliah_create.json
│       ├── matakuliah_update.json
│       ├── matakuliah_invalid.json
│       └── matakuliah_missing.json
└── screenshots/
```

## Prasyarat

1. Python 3.10 atau lebih baru (disarankan 3.12).
2. PostgreSQL yang sudah berjalan di `localhost:5432`.
3. Terminal PowerShell, Command Prompt, atau terminal Linux/macOS.

> Pada Windows, pastikan folder `bin` PostgreSQL sudah masuk `PATH`, atau
> gunakan path lengkap seperti
> `"C:\Program Files\PostgreSQL\18\bin\psql.exe"`.

## 1. Instalasi

Masuk ke folder proyek, lalu buat virtual environment dan pasang
dependensi.

**Windows (PowerShell):**

```powershell
cd Yowen_Daniel_124140120_pertemuan6
python -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -e .
```

**Linux/macOS:**

```bash
cd Yowen_Daniel_124140120_pertemuan6
python3 -m venv venv
source venv/bin/activate
python -m pip install --upgrade pip
pip install -e .
```

## 2. Menyiapkan Database PostgreSQL

Buka PostgreSQL sebagai superuser:

```powershell
psql -U postgres
```

Jalankan perintah SQL berikut:

```sql
CREATE USER pyramid_user WITH ENCRYPTED PASSWORD 'pyramid_pass';
CREATE DATABASE pyramid_mahasiswa OWNER pyramid_user;
GRANT ALL PRIVILEGES ON DATABASE pyramid_mahasiswa TO pyramid_user;
```

Masuk ke database yang baru dibuat, lalu beri akses skema `public`
(diperlukan pada PostgreSQL 15 ke atas):

```sql
\c pyramid_mahasiswa
GRANT ALL ON SCHEMA public TO pyramid_user;
\q
```

Connection string bawaan proyek ada di `development.ini` dan
`production.ini`:

```ini
sqlalchemy.url = postgresql+psycopg2://pyramid_user:pyramid_pass@localhost:5432/pyramid_mahasiswa
```

Jika username, password, host, atau nama database berbeda, sesuaikan nilai
tersebut pada kedua file INI.

## 3. Menjalankan Migrasi Alembic

```powershell
alembic -c development.ini upgrade head
```

Periksa versi migrasi yang aktif:

```powershell
alembic -c development.ini current
```

Keluaran yang diharapkan:

```text
202611120002 (head)
```

Migrasi yang tersedia:

| Revisi | Deskripsi |
| --- | --- |
| `202611120001` | create mahasiswa table |
| `202611120002` | create matakuliah table |

Untuk membatalkan satu migrasi terakhir:

```powershell
alembic -c development.ini downgrade -1
```

## 4. Seeding Data Awal

```powershell
python -m pyramid_mahasiswa.scripts.initialize_db development.ini
```

Keluaran yang diharapkan:

```text
Seeding mahasiswa: 2 data ditambahkan.
Seeding matakuliah: 3 data ditambahkan.
Seeding database selesai.
```

Data mata kuliah awal yang disisipkan:

| kode_mk | nama_mk | sks | semester |
| --- | --- | --- | --- |
| IF2110 | Pemrograman Web | 3 | 3 |
| IF3140 | Basis Data | 3 | 4 |
| IF2230 | Sistem Operasi | 4 | 4 |

## 5. Menjalankan Server

```powershell
pserve development.ini --reload
```

Server berjalan di <http://localhost:6543>. Halaman utama menampilkan
informasi aplikasi dan daftar endpoint yang tersedia.

## Ringkasan Endpoint

| No | Method | Endpoint | Fungsi | Status Sukses |
| --- | --- | --- | --- | --- |
| 1 | GET | `/api/mahasiswa` | Menampilkan seluruh mahasiswa | 200 |
| 2 | GET | `/api/mahasiswa/{id}` | Menampilkan satu mahasiswa | 200 |
| 3 | POST | `/api/mahasiswa` | Menambahkan mahasiswa | 200 |
| 4 | PUT | `/api/mahasiswa/{id}` | Memperbarui mahasiswa | 200 |
| 5 | DELETE | `/api/mahasiswa/{id}` | Menghapus mahasiswa | 200 |
| 6 | GET | `/api/matakuliah` | Menampilkan seluruh mata kuliah | 200 |
| 7 | GET | `/api/matakuliah/{id}` | Menampilkan satu mata kuliah | 200 |
| 8 | POST | `/api/matakuliah` | Menambahkan mata kuliah | 200 |
| 9 | PUT | `/api/matakuliah/{id}` | Memperbarui mata kuliah | 200 |
| 10 | DELETE | `/api/matakuliah/{id}` | Menghapus mata kuliah | 200 |

Kode status tambahan:

- `400 Bad Request` — body bukan JSON objek, field wajib kosong, tipe
  `sks`/`semester` bukan bilangan bulat, nilai `sks`/`semester` kurang dari
  atau sama dengan nol, atau `nim`/`kode_mk` sudah terdaftar.
- `404 Not Found` — ID data tidak ditemukan atau URL tidak terdaftar.

## Struktur Tabel `matakuliah`

| Kolom | Tipe | Aturan |
| --- | --- | --- |
| `id` | Integer | Primary key, auto increment |
| `kode_mk` | Text | Unique, not null |
| `nama_mk` | Text | Not null |
| `sks` | Integer | Not null, harus > 0 |
| `semester` | Integer | Not null, harus > 0 |

Model juga menyediakan method `to_dict()` untuk mengubah objek ORM menjadi
dictionary yang siap dikirim sebagai JSON.

## Pengujian dengan cURL

Jalankan perintah dari **root folder proyek** agar path payload relatif
`tests/payloads/...` dapat ditemukan.

> **Windows PowerShell:** gunakan `curl.exe`, bukan alias `curl`. Alias
> `curl` di PowerShell 5.1 dapat merusak tanda kutip pada body JSON. Karena
> itu contoh di bawah mengirim payload melalui file dengan opsi
> `--data-binary "@namafile"`. Opsi `-i` menampilkan status line dan header
> agar hasil pengujian mudah dibuktikan saat screenshot.

### Mahasiswa

**1) GET seluruh mahasiswa**

```powershell
curl.exe -i http://localhost:6543/api/mahasiswa
```

**2) GET detail mahasiswa**

```powershell
curl.exe -i http://localhost:6543/api/mahasiswa/1
```

ID yang tidak ada akan menghasilkan `404`:

```powershell
curl.exe -i http://localhost:6543/api/mahasiswa/9999
```

**3) POST mahasiswa**

```powershell
curl.exe -i -X POST http://localhost:6543/api/mahasiswa -H "Content-Type: application/json" --data-binary "@tests/payloads/mahasiswa_create.json"
```

Contoh payload tidak lengkap (menghasilkan `400`):

```powershell
curl.exe -i -X POST http://localhost:6543/api/mahasiswa -H "Content-Type: application/json" --data-binary "@tests/payloads/mahasiswa_invalid.json"
```

**4) PUT mahasiswa**

Ganti angka `3` dengan ID mahasiswa yang baru dibuat.

```powershell
curl.exe -i -X PUT http://localhost:6543/api/mahasiswa/3 -H "Content-Type: application/json" --data-binary "@tests/payloads/mahasiswa_update.json"
```

**5) DELETE mahasiswa**

```powershell
curl.exe -i -X DELETE http://localhost:6543/api/mahasiswa/3
```

### Matakuliah

**1) GET seluruh mata kuliah**

```powershell
curl.exe -i http://localhost:6543/api/matakuliah
```

**2) GET detail mata kuliah**

```powershell
curl.exe -i http://localhost:6543/api/matakuliah/1
```

ID yang tidak ada akan menghasilkan `404`:

```powershell
curl.exe -i http://localhost:6543/api/matakuliah/9999
```

**3) POST mata kuliah**

```powershell
curl.exe -i -X POST http://localhost:6543/api/matakuliah -H "Content-Type: application/json" --data-binary "@tests/payloads/matakuliah_create.json"
```

Contoh `sks = 0` (menghasilkan `400`):

```powershell
curl.exe -i -X POST http://localhost:6543/api/matakuliah -H "Content-Type: application/json" --data-binary "@tests/payloads/matakuliah_invalid.json"
```

Contoh field `semester` tidak dikirim (menghasilkan `400`):

```powershell
curl.exe -i -X POST http://localhost:6543/api/matakuliah -H "Content-Type: application/json" --data-binary "@tests/payloads/matakuliah_missing.json"
```

**4) PUT mata kuliah**

Ganti angka `4` dengan ID mata kuliah yang baru dibuat.

```powershell
curl.exe -i -X PUT http://localhost:6543/api/matakuliah/4 -H "Content-Type: application/json" --data-binary "@tests/payloads/matakuliah_update.json"
```

**5) DELETE mata kuliah**

```powershell
curl.exe -i -X DELETE http://localhost:6543/api/matakuliah/4
```

## Screenshot Pengujian

Simpan screenshot ke folder `screenshots/` dengan nama file berikut. Setiap
gambar harus memperlihatkan **perintah cURL dan respons server** (status
line, header, dan body JSON) dalam satu tangkapan layar.

| File | Bagian yang harus terlihat |
| --- | --- |
| `00_migrasi_seeding.png` | `alembic upgrade head`, `alembic current`, dan output seeding |
| `01_get_mahasiswa_list.png` | `GET /api/mahasiswa` → `200 OK` dan daftar mahasiswa |
| `02_get_mahasiswa_detail.png` | `GET /api/mahasiswa/1` → `200 OK` dan `GET /api/mahasiswa/9999` → `404 Not Found` |
| `03_post_mahasiswa.png` | `POST` valid → `200 OK`, lalu `POST` tanpa `nim` → `400 Bad Request` |
| `04_put_mahasiswa.png` | `PUT /api/mahasiswa/{id}` → `200 OK` dengan data terbaru |
| `05_delete_mahasiswa.png` | `DELETE` → `200 OK`, lalu `GET` ID yang sama → `404 Not Found` |
| `06_get_matakuliah_list.png` | `GET /api/matakuliah` → `200 OK` dan daftar mata kuliah |
| `07_get_matakuliah_detail.png` | `GET /api/matakuliah/1` → `200 OK` dan `GET /api/matakuliah/9999` → `404 Not Found` |
| `08_post_matakuliah.png` | `POST` valid → `200 OK`, `sks = 0` → `400`, dan tanpa `semester` → `400` |
| `09_put_matakuliah.png` | `PUT /api/matakuliah/{id}` → `200 OK` dengan data terbaru |
| `10_delete_matakuliah.png` | `DELETE` → `200 OK`, lalu `GET` ID yang sama → `404 Not Found` |

### 00 — Migrasi dan Seeding

![Migrasi Alembic dan seeding](screenshots/00_migrasi_seeding.png)

**Keterangan:** Menjalankan `alembic -c development.ini upgrade head` untuk
menerapkan dua migrasi (`create mahasiswa table` → `202611120001` dan
`create matakuliah table` → `202611120002`), diikuti
`python -m pyramid_mahasiswa.scripts.initialize_db development.ini`
yang menyisipkan 2 data mahasiswa dan 3 data mata kuliah awal
(IF2110, IF3140, IF2230) ke PostgreSQL.

### 01 — GET seluruh mahasiswa

![GET seluruh mahasiswa](screenshots/01_get_mahasiswa_list.png)

**Keterangan:** `curl.exe -i http://localhost:6543/api/mahasiswa` —
mengembalikan **200 OK** berisi seluruh data mahasiswa dari tabel
`mahasiswa` dalam format JSON.

### 02 — GET detail mahasiswa dan 404

![GET detail mahasiswa](screenshots/02_get_mahasiswa_detail.png)

**Keterangan:** `curl.exe -i http://localhost:6543/api/mahasiswa/1`
mengembalikan **200 OK** dengan detail mahasiswa ID 1, sedangkan
`curl.exe -i http://localhost:6543/api/mahasiswa/9999` mengembalikan
**404 Not Found** karena ID 9999 tidak terdaftar.

### 03 — POST mahasiswa valid dan 400

![POST mahasiswa](screenshots/03_post_mahasiswa.png)

**Keterangan:** `POST /api/mahasiswa` dengan payload
`tests/payloads/mahasiswa_create.json` mengembalikan **200 OK** dan data
baru berhasil dibuat. Permintaan kedua dengan payload
`tests/payloads/mahasiswa_invalid.json` (tanpa field `nim`) ditolak dengan
**400 Bad Request** berisi pesan validasi.

### 04 — PUT mahasiswa

![PUT mahasiswa](screenshots/04_put_mahasiswa.png)

**Keterangan:** `curl.exe -i -X PUT http://localhost:6543/api/mahasiswa/3`
dengan payload `tests/payloads/mahasiswa_update.json` mengembalikan
**200 OK** dan menampilkan data mahasiswa ID 3 yang sudah diperbarui
(nama, jurusan, dan alamat berganti sesuai payload).

### 05 — DELETE mahasiswa dan 404

![DELETE mahasiswa](screenshots/05_delete_mahasiswa.png)

**Keterangan:** `curl.exe -i -X DELETE http://localhost:6543/api/mahasiswa/3`
mengembalikan **200 OK** (data terhapus), dan pemanggilan
`GET /api/mahasiswa/3` setelahnya mengembalikan **404 Not Found** —
membuktikan data benar-benar dihapus dari database.

### 06 — GET seluruh mata kuliah

![GET seluruh mata kuliah](screenshots/06_get_matakuliah_list.png)

**Keterangan:** `curl.exe -i http://localhost:6543/api/matakuliah` —
mengembalikan **200 OK** berisi daftar mata kuliah hasil seeding
(IF2110 Pemrograman Web, IF3140 Basis Data, IF2230 Sistem Operasi)
dari tabel `matakuliah`.

### 07 — GET detail mata kuliah dan 404

![GET detail mata kuliah](screenshots/07_get_matakuliah_detail.png)

**Keterangan:** `curl.exe -i http://localhost:6543/api/matakuliah/1`
mengembalikan **200 OK** dengan detail mata kuliah ID 1 (IF2110), sedangkan
`curl.exe -i http://localhost:6543/api/matakuliah/9999` mengembalikan
**404 Not Found** karena ID 9999 tidak terdaftar.

### 08 — POST mata kuliah valid dan 400

![POST mata kuliah](screenshots/08_post_matakuliah.png)

**Keterangan:** Tiga pengujian pada `POST /api/matakuliah`: (1) payload
`matakuliah_create.json` yang valid → **200 OK** dengan data baru; (2)
payload `matakuliah_invalid.json` dengan `sks = 0` → **400 Bad Request**
karena SKS harus lebih besar dari 0; (3) payload `matakuliah_missing.json`
tanpa field `semester` → **400 Bad Request** karena field wajib tidak
lengkap.

### 09 — PUT mata kuliah

![PUT mata kuliah](screenshots/09_put_matakuliah.png)

**Keterangan:** `curl.exe -i -X PUT http://localhost:6543/api/matakuliah/4`
dengan payload `tests/payloads/matakuliah_update.json` mengembalikan
**200 OK** dan menampilkan data mata kuliah ID 4 yang sudah diperbarui
(nama_mk, sks, dan semester berganti sesuai payload).

### 10 — DELETE mata kuliah dan 404

![DELETE mata kuliah](screenshots/10_delete_matakuliah.png)

**Keterangan:** `curl.exe -i -X DELETE http://localhost:6543/api/matakuliah/4`
mengembalikan **200 OK** (data terhapus), dan pemanggilan
`GET /api/matakuliah/4` setelahnya mengembalikan **404 Not Found** —
membuktikan data benar-benar dihapus dari database.

## Pemeriksaan Gaya Kode (PEP 8)

```powershell
pycodestyle pyramid_mahasiswa setup.py
```

Perintah tersebut tidak menampilkan apa pun jika seluruh berkas sudah
memenuhi PEP 8.

## Catatan

- `.gitignore` sudah mengabaikan `venv/`, `*.sqlite`, `__pycache__/`, dan
  `*.pyc`.
- Folder `venv/` tidak boleh ikut di-commit.
- Gunakan `development.ini` untuk pengembangan lokal dan `production.ini`
  untuk deployment.
- Semua respons, termasuk pesan kesalahan, dikirim dalam format JSON.
