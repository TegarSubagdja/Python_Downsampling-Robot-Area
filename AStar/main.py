import cv2
import numpy as np
import pandas as pd
from astar import astar
from ShapeDetector import DetektorBentuk  # Sesuaikan dengan nama class yang sudah diubah
from BarrierRasterCoefficient import BRC as br
from Guideline import Guideline as gl

def utama():
    # Muat dan proses gambar
    gambar = cv2.imread('image.png')

    detektor = DetektorBentuk(gambar)
    tengah_hijau = detektor.deteksi_tengah_hijau()
    tengah_merah = detektor.deteksi_tengah_merah()
    # print("Titik tengah area hijau:", tengah_hijau)
    # print("Titik tengah area merah:", tengah_merah)

    gambar_abu = cv2.cvtColor(gambar, cv2.COLOR_BGR2GRAY)
    _, gambar_biner = cv2.threshold(gambar_abu, 180, 255, cv2.THRESH_BINARY_INV)

    # Konversi gambar biner ke peta yang dapat dilalui
    peta_array = np.array(gambar_biner) // 255

    # titik_sekarang = (12, 8)

    # print(gl.guidline(tengah_hijau, tengah_merah, titik_sekarang))
    # print(br.barrierRaster(tengah_hijau, tengah_merah, peta_array))

    # Cari jalur menggunakan algoritma A*
    jalur = astar(peta_array, tengah_hijau, tengah_merah)

    return peta_array, jalur
    # Cetak jalur
    if jalur:
        print("Jalur ditemukan:", jalur)

        for titik in jalur:
            peta_array[titik[1], titik[0]] = 7  # Tandai jalur dengan nilai 7
        
        peta_array[titik_sekarang[1], titik_sekarang[0]] = 3

        # Ubah nilai dalam array sesuai permintaan
        peta_array = np.where(peta_array == 0, '.', peta_array)  # 0 menjadi titik (.)
        peta_array = np.where(peta_array == '1', '#', peta_array)  # 1 menjadi halangan (#)
        peta_array = np.where(peta_array == '2', '#', peta_array)  # 2 menjadi halangan (#)
        peta_array = np.where(peta_array == '7', '@', peta_array)  # 7 menjadi jalur (*)

        # Konversi peta_array ke pandas DataFrame untuk visualisasi yang lebih baik
        df = pd.DataFrame(peta_array)
        print("Peta dengan Jalur (direpresentasikan oleh 2):")
        print(df)
    else:
        print("Tidak ada jalur yang ditemukan")

if __name__ == "__main__":
    utama()