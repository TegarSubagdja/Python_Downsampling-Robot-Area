# bounding_box_calculator.py
import cv2

def calculate_bounding_box(contour):
    """Menghitung bounding box dari kontur"""
    x, y, w, h = cv2.boundingRect(contour)
    return x, y, w, h

def filter_small_contours(contours, min_area=500):
    """Menyaring kontur kecil berdasarkan area minimum"""
    return [contour for contour in contours if cv2.contourArea(contour) > min_area]

def draw_bounding_boxes(image, contours):
    """Menggambar bounding box untuk setiap kontur"""
    for contour in contours:
        x, y, w, h = calculate_bounding_box(contour)
        print(f"Bounding Box - Lebar: {w}, Tinggi: {h}")
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 3)
