import cv2
import numpy as np
from Modul.Detect import GreenAreaDetector as gad
from Modul.Detect import RedAreaDetector as rad
from Modul.Detect import BoundingBoxCalculator as bbc
from Modul.PathFinding.AStarAlgorithm import AStar

def process_image(image_path):
    """Proses utama untuk mendeteksi area hijau dan merah dan menggambar bounding box"""
    # Baca gambar
    image = cv2.imread(image_path)

    # Membuat masker hijau dan merah menggunakan fungsi dari GreenAreaDetector dan RedAreaDetector
    green_mask = gad.create_green_mask(image)
    red_mask = rad.create_red_mask(image)

    # Mencari kontur hijau dan merah
    green_contours, _ = cv2.findContours(green_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    red_contours, _ = cv2.findContours(red_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Menyaring kontur kecil
    green_contours = bbc.filter_small_contours(green_contours)
    red_contours = bbc.filter_small_contours(red_contours)

    # Menggambar bounding box untuk area hijau dan merah
    bbc.draw_bounding_boxes(image, green_contours)
    bbc.draw_bounding_boxes(image, red_contours)

    # Pastikan ada kontur yang valid
    if len(green_contours) == 0 or len(red_contours) == 0:
        raise ValueError("Tidak ada kontur yang valid ditemukan untuk area hijau atau merah.")

    # Menentukan titik tengah dari area hijau dan merah
    green_center = bbc.get_center_of_bounding_box(green_contours[0])  # Pilih kontur pertama
    red_center = bbc.get_center_of_bounding_box(red_contours[0])      # Pilih kontur pertama
    print(green_center, red_center)

    # Menyusun grid untuk A* (menganggap gambar menjadi grid 2D)
    grid = np.zeros((image.shape[0], image.shape[1]), dtype=int)
    print(grid)

    # Menandai area hijau dan merah sebagai penghalang (nilai 1)
    grid[green_mask == 255] = 0.1
    grid[red_mask == 255] = 0.1

    # Menjalankan A* untuk mencari jalur dari titik tengah area hijau ke merah
    astar = AStar(grid)
    path = astar.find_path(green_center, red_center)
    print(path)

    # Menggambar jalur A* pada gambar menggunakan metode dari AStar
    image = astar.draw_path(image, path, color=(0, 0, 0), thickness=10)

    return image, green_center, red_center

if __name__ == "__main__":
    image_path = "Assets/image.png"  # Ganti dengan path gambar Anda
    result_image, green_center, red_center = process_image(image_path)

    # Menampilkan gambar dengan jalur A*
    cv2.imshow("Path from Green to Red", result_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
