import cv2
import numpy as np

def detect_green_area(image_path):
    # Baca gambar
    image = cv2.imread(image_path)

    # Konversi gambar ke format HSV untuk mendeteksi warna hijau
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Tentukan rentang warna hijau dalam HSV
    lower_green = np.array([40, 40, 40])  # Rentang bawah untuk warna hijau
    upper_green = np.array([80, 255, 255])  # Rentang atas untuk warna hijau

    # Membuat masker untuk mendeteksi area hijau
    mask = cv2.inRange(hsv_image, lower_green, upper_green)

    # Menggunakan masker untuk mengekstrak area hijau
    green_area = cv2.bitwise_and(image, image, mask=mask)

    # Mencari kontur untuk area hijau yang terdeteksi
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Gambar bounding box untuk setiap kontur yang ditemukan
    for contour in contours:
        if cv2.contourArea(contour) > 500:  # Hanya kontur dengan area cukup besar
            x, y, w, h = cv2.boundingRect(contour)  # Dapatkan bounding box
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 3)  # Gambar kotak pembatas hijau

    # Tampilkan gambar dengan bounding box
    cv2.imshow("Green Area with Bounding Box", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Path gambar
image_path = "image.png"  # Ganti dengan path gambar Anda

# Panggil fungsi untuk mendeteksi area hijau dan memberi bounding box
detect_green_area(image_path)
