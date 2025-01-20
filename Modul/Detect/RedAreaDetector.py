# green_area_detector.py
import cv2
import numpy as np

def create_green_mask(image):
    """Membuat masker untuk mendeteksi area hijau dalam gambar"""
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower_green = np.array([40, 40, 40])  # Rentang bawah untuk warna hijau
    upper_green = np.array([80, 255, 255])  # Rentang atas untuk warna hijau
    return cv2.inRange(hsv_image, lower_green, upper_green)

def extract_green_area(image, mask):
    """Mengekstrak area hijau berdasarkan masker"""
    return cv2.bitwise_and(image, image, mask=mask)
