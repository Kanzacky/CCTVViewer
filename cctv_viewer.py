"""
CCTV Viewer - Pemkot Yogyakarta
=================================
Menampilkan live stream CCTV publik milik Pemkot Yogyakarta
(https://cctv.jogjakota.go.id) langsung di jendela Python.

CATATAN PENTING:
- CCTV ini bersifat publik, disediakan untuk pemantauan lalu lintas & keamanan kota.
- URL stream (.m3u8) di bawah bisa berubah sewaktu-waktu karena nama file
  chunklist-nya dinamis. Kalau stream tidak muncul / error, cari ulang URL
  terbaru dengan cara:
    1. Buka https://cctv.jogjakota.go.id/ di browser
    2. Klik salah satu titik CCTV di peta
    3. Buka DevTools (F12) -> tab Network -> filter "m3u8"
    4. Copy URL yang muncul, ganti STREAM_URL di bawah

Cara pakai:
    pip install opencv-python
    python cctv_viewer.py
"""

import cv2
import sys

# Contoh titik CCTV: Nol Kilometer Malioboro
STREAM_URL = "https://cctvjss.jogjakota.go.id/malioboro/NolKm_Timur.stream/chunklist_w221624478.m3u8"


def show_stream(url):
    print(f"Menyambungkan ke stream: {url}")
    cap = cv2.VideoCapture(url)

    if not cap.isOpened():
        print("Gagal membuka stream. Kemungkinan penyebab:")
        print("  - URL sudah tidak valid/berubah (lihat catatan di atas)")
        print("  - Koneksi internet bermasalah")
        print("  - OpenCV tidak terhubung dengan FFmpeg backend")
        sys.exit(1)

    print("Berhasil terhubung! Tekan 'q' untuk keluar.")

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Frame tidak terbaca, stream mungkin terputus.")
            break

        cv2.imshow("CCTV Jogja - Nol Kilometer", frame)

        # Tekan 'q' untuk keluar
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    show_stream(STREAM_URL)
