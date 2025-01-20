# Main.py
import cv2

# Mengimpor modul dari folder 'Modul'
from Modul.Detect import GreenAreaDetector as gad
from Modul.Detect import BoundingBoxCalculator as bbc

def process_image(image_path):
    """Proses utama untuk mendeteksi area hijau dan menggambar bounding box"""
    # Baca gambar
    image = cv2.imread(image_path)

    # Membuat masker hijau menggunakan fungsi dari GreenAreaDetector
    mask = gad.create_green_mask(image)

    # Mengekstrak area hijau menggunakan fungsi dari GreenAreaDetector
    green_area = gad.extract_green_area(image, mask)

    # Mencari kontur
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Menyaring kontur kecil menggunakan fungsi dari BoundingBoxCalculator
    contours = bbc.filter_small_contours(contours)

    # Menggambar bounding box menggunakan fungsi dari BoundingBoxCalculator
    bbc.draw_bounding_boxes(image, contours)

    return image

if __name__ == "__main__":
    # Path gambar
    image_path = "Assets/image.png"  # Ganti dengan path gambar Anda

    # Proses gambar dan menggambar bounding box
    result_image = process_image(image_path)

    # Menampilkan gambar dengan bounding box
    cv2.imshow("Green Area with Bounding Boxes", result_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
