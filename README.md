# Visual3_2310010459 — Aplikasi Manajemen Admin, Anggota, Usaha & Resiko (PySide6 + MySQL)

> Aplikasi desktop **PySide6 (Qt for Python)** dengan database **MySQL** untuk mengelola **Admin**, **Anggota**, **Usaha**, dan **Resiko**. Antarmuka dibuat memakai **Qt Designer** (`.ui`) sehingga mudah diubah tanpa menyentuh kode.

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](#)
[![PySide6](https://img.shields.io/badge/PySide6-Qt%20for%20Python-41b883.svg)](#)
[![MySQL](https://img.shields.io/badge/DB-MySQL-orange.svg)](#)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](#)

---

## ✨ Fitur Utama
- **CRUD**: Admin, Anggota, Usaha, Resiko  
- **Tabel interaktif** dengan `QTableWidget`  
- **Notifikasi** via `QMessageBox` (simpan/ubah/hapus/galat)  
- **Desain UI terpisah** (`.ui`) → mudah di-maintain  
- **Arsitektur modular**: logika CRUD (`crudDB.py`) terpisah dari UI (`*.ui`/`*.py`)  

---

## 📸 Tampilan Aplikasi

> 

| Halaman | Cuplikan |
|---|---|
| **Menu Utama** | ![Menu Utama](<img width="236" height="326" alt="image" src="https://github.com/user-attachments/assets/538b10c1-d74c-4dc5-9b57-1b28ee9d1e3a" />
) |
| **Data Admin** | ![Data Admin](<img width="584" height="614" alt="image" src="https://github.com/user-attachments/assets/c7cedfc2-c561-4606-abf5-55ef1f277ae0" />
) |
| **Data Usaha** | ![Data Usaha](<img width="690" height="569" alt="image" src="https://github.com/user-attachments/assets/b7f2caff-fd3b-4c3f-b136-fe8d08c3814b" />
) |



---

## 🗂️ Struktur Proyek (contoh)

Visual3_2310010459/
├─ main.py
├─ crudDB.py
├─ DataAdmin.py
├─ Anggota.py
├─ Usaha.py
├─ Resiko.py
├─ ui/
│ ├─ MainWindow.ui
│ ├─ DataAdmin.ui
│ ├─ Anggota.ui
│ ├─ Usaha.ui
│ └─ Resiko.ui
├─ docs/
│ └─ screenshots/
│ ├─ 01-menu.png
│ ├─ 02-admin.png
│ └─ 03-usaha.png
├─ requirements.txt
├─ .env.example
└─ README.md



---

## 🧰 Prasyarat
- **Python 3.10+**  
- **MySQL Server** (lokal/remote)  
- **Qt Designer** (opsional, untuk edit `.ui`)  

---

## 🚀 Instalasi & Menjalankan

```bash
# 1) (opsional) buat & aktifkan virtual environment
python -m venv .venv
# Windows
. .venv/Scripts/activate
# macOS/Linux
# source .venv/bin/activate

# 2) install dependensi
pip install -r requirements.txt
# jika belum ada requirements.txt:
# pip install PySide6 mysql-connector-python python-dotenv

# 3) siapkan environment database
# salin .env.example menjadi .env lalu isi kredensial (lihat contoh di bawah)

# 4) jalankan aplikasi
python main.py

Contoh .env

DB_HOST=localhost
DB_USER=root
DB_PASS=
DB_NAME=visual3_2310010459

🗄️ Skema Database (contoh)
CREATE DATABASE IF NOT EXISTS visual3_2310010459;
USE visual3_2310010459;

CREATE TABLE admin (
  id_admin INT AUTO_INCREMENT PRIMARY KEY,
  username VARCHAR(50) UNIQUE NOT NULL,
  password VARCHAR(255) NOT NULL,
  nama_lengkap VARCHAR(100),
  email VARCHAR(100),
  role ENUM('admin','user') DEFAULT 'admin',
  tanggal_dibuat DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE anggota (
  id_anggota INT AUTO_INCREMENT PRIMARY KEY,
  nim VARCHAR(30) UNIQUE,
  nama_lengkap VARCHAR(100) NOT NULL,
  prodi VARCHAR(100),
  no_hp VARCHAR(20),
  alamat TEXT,
  tanggal_dibuat DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE usaha (
  id_usaha INT AUTO_INCREMENT PRIMARY KEY,
  nama_usaha VARCHAR(120) NOT NULL,
  lokasi VARCHAR(120),
  tahun_berdiri INT,
  jumlah_buruh INT DEFAULT 0,
  pendapatan BIGINT DEFAULT 0
);

CREATE TABLE resiko (
  id_resiko INT AUTO_INCREMENT PRIMARY KEY,
  id_pekerja INT,
  id_admin INT,
  kategori VARCHAR(100),
  level VARCHAR(50),
  deskripsi TEXT,
  tanggal_dibuat DATETIME DEFAULT CURRENT_TIMESTAMP
);

🧩 Catatan Implementasi (PySide6)

Memuat UI dari file:

from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader

ui_file = QFile("ui/DataAdmin.ui")  # sesuaikan path
ui_file.open(QFile.ReadOnly)
form = QUiLoader().load(ui_file)
ui_file.close()


Pesan sukses:

from PySide6.QtWidgets import QMessageBox
QMessageBox.information(self, "Berhasil", "Data berhasil disimpan.")

🧪 Troubleshooting

ModuleNotFoundError: No module named 'mysql'
Pastikan venv aktif → pip install mysql-connector-python.

Data tidak tampil di tabel
Panggil setupTable() satu kali saat init, set setRowCount() & setItem(), cocokan objectName di .ui dengan yang dipanggil di kode (mis. tableWidget).

Path .ui salah
Sesuaikan QFile("ui/NamaFile.ui") jika file dipindah.

📦 Build ke .exe (opsional, Windows)
pip install pyinstaller
pyinstaller --noconfirm --onefile --windowed --name Visual3_2310010459 main.py
# output: dist/Visual3_2310010459.exe
