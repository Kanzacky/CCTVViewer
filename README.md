# Jogja CCTV Viewer 🎥

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)
![OpenCV Version](https://img.shields.io/badge/OpenCV-5.0%2B-green.svg)

**Jogja CCTV Viewer** adalah sebuah skrip Python sederhana namun kuat yang digunakan untuk menampilkan *live streaming* CCTV publik milik Pemerintah Kota Yogyakarta (dari portal [https://cctv.jogjakota.go.id](https://cctv.jogjakota.go.id)). Skrip ini menggunakan pustaka **OpenCV** untuk menangkap dan merender *stream* berformat `.m3u8` langsung ke dalam sebuah jendela aplikasi (*window*).

---

## Fitur

- **Real-time Streaming**: Menonton kondisi lalu lintas dan titik vital Kota Jogja secara *live* dengan latensi minimal.
- **Ringan dan Cepat**: Menggunakan modul inti OpenCV tanpa membebani memori (GUI minimal).
- **Mudah Dimodifikasi**: Anda dapat dengan mudah mengganti URL *stream* dengan titik CCTV publik lainnya.

---

## Prasyarat

Sebelum memulai, pastikan sistem Anda sudah terpasang:

- **Python 3.8** atau yang lebih baru.
- Koneksi internet yang stabil untuk kelancaran *streaming*.

---

## Instalasi

Karena kebijakan pengelolaan lingkungan (*externally-managed-environment* - **PEP 668**) pada sistem operasi modern (seperti Ubuntu terbaru, Arch Linux, macOS, dll), disarankan untuk menggunakan **Virtual Environment**.

### 1. Kloning Repositori
```bash
git clone <URL_REPOSITORI_ANDA>
cd cctv
```

### 2. Buat & Aktifkan Virtual Environment
```bash
# Membuat environment bernama .venv
python3 -m venv .venv

# Mengaktifkan environment (Linux/macOS)
source .venv/bin/activate

# Mengaktifkan environment (Windows)
# .venv\Scripts\activate
```

### 3. Instalasi Dependensi
```bash
pip install -r requirements.txt
# Atau jika Anda belum memiliki requirements.txt:
# pip install opencv-python
```

---

## Penggunaan

Pastikan *virtual environment* masih aktif, lalu jalankan perintah berikut:

```bash
python cctv_viewer.py
```
* **KONTROL:** Tekan tombol `q` pada keyboard saat jendela CCTV aktif untuk menutup aplikasi.

---

## Pemecahan Masalah (Troubleshooting)

### 1. Error: "Frame tidak terbaca, stream mungkin terputus" atau "Gagal membuka stream"
URL *stream* dari server pemerintah kota terkadang bersifat dinamis (nama *chunklist*-nya berubah-ubah). Jika *stream* tiba-tiba tidak dapat diputar, lakukan langkah berikut untuk memperbarui URL:

1. Buka browser dan kunjungi [https://cctv.jogjakota.go.id](https://cctv.jogjakota.go.id)
2. Klik titik CCTV yang Anda inginkan dari peta.
3. Buka **Developer Tools** (Tekan `F12` atau `Ctrl+Shift+I`).
4. Pindah ke tab **Network** dan ketik `m3u8` di kolom *Filter*.
5. Salin URL terbaru (contoh: `chunklist_w...m3u8`) dan *paste* ke dalam variabel `STREAM_URL` di *file* `cctv_viewer.py`.

### 2. Peringatan Font (Qt)
Bila melihat *warning* di terminal: `QFontDatabase: Cannot find font directory...`, hal ini adalah *bug* minor internal dari integrasi Qt pada paket OpenCV versi terbaru dan sama sekali **tidak mempengaruhi berjalannya video**.

---

## Disclaimer

Aplikasi ini dikembangkan untuk tujuan edukasi dan kemudahan akses data publik. Segala bentuk penyalahgunaan di luar kewenangan dan privasi publik adalah tanggung jawab pengguna. **Live stream CCTV yang diakses adalah fasilitas publik milik Pemerintah Kota Yogyakarta.** 

---
