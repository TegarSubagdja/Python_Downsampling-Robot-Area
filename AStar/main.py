import cv2
import numpy as np
from Astar import astar
import pandas as pd
from ShapeDetector import DetektorBentuk  # Sesuaikan dengan nama class yang sudah diubah

def utama():
    # Muat dan proses gambar
    gambar = cv2.imread('image2.png')

    detektor = DetektorBentuk(gambar)
    tengah_hijau = detektor.deteksi_tengah_hijau()
    tengah_merah = detektor.deteksi_tengah_merah()
    print("Titik tengah area hijau:", tengah_hijau)
    print("Titik tengah area merah:", tengah_merah)

    gambar_abu = cv2.cvtColor(gambar, cv2.COLOR_BGR2GRAY)
    _, gambar_biner = cv2.threshold(gambar_abu, 180, 255, cv2.THRESH_BINARY_INV)

    # Konversi gambar biner ke peta yang dapat dilalui
    peta_array = np.array(gambar_biner) // 255

    # Cari jalur menggunakan algoritma A*
    jalur = astar(peta_array, tengah_hijau, tengah_merah)

    # Cetak jalur
    if jalur:
        print("Jalur ditemukan:", jalur)

        # Tandai jalur pada peta_array (tandai jalur dengan nilai 2)
        for titik in jalur:
            peta_array[titik[1], titik[0]] = 7  # Tandai jalur (bisa menggunakan nilai apa pun, misalnya 2)

        # Konversi peta_array ke pandas DataFrame untuk visualisasi yang lebih baik
        df = pd.DataFrame(peta_array)
        print("Peta dengan Jalur (direpresentasikan oleh 2):")
        print(df)

    else:
        print("Tidak ada jalur yang ditemukan")

if __name__ == "__main__":
    utama()