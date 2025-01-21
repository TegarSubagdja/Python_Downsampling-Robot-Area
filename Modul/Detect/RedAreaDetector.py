# red_area_detector.py
import cv2
import numpy as np

def create_red_mask(image):
    """Membuat masker untuk mendeteksi area merah dalam gambar"""
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    # Rentang bawah dan atas untuk warna merah
    lower_red1 = np.array([0, 50, 50])  # Rentang pertama
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([170, 50, 50])  # Rentang kedua
    upper_red2 = np.array([180, 255, 255])
    
    # Membuat masker untuk kedua rentang
    mask1 = cv2.inRange(hsv_image, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv_image, lower_red2, upper_red2)
    
    # Menggabungkan kedua masker
    return cv2.bitwise_or(mask1, mask2)

def extract_red_area(image, mask):
    """Mengekstrak area merah berdasarkan masker"""
    return cv2.bitwise_and(image, image, mask=mask)
