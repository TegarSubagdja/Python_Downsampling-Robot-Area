import cv2
import numpy as np

class DetektorBentuk:
    def __init__(self, gambar):
        self.gambar = gambar
        self.hsv = cv2.cvtColor(self.gambar, cv2.COLOR_BGR2HSV)
        
    def deteksi_tengah_merah(self):
        return self._deteksi_tengah(
            np.array([0, 120, 70], dtype=np.uint8), np.array([10, 255, 255], dtype=np.uint8),
            np.array([170, 120, 70], dtype=np.uint8), np.array([180, 255, 255], dtype=np.uint8)
        )
    
    def deteksi_tengah_hijau(self):
        return self._deteksi_tengah(
            np.array([35, 100, 70], dtype=np.uint8), np.array([85, 255, 255], dtype=np.uint8)
        )
    
    def _deteksi_tengah(self, batas_bawah1, batas_atas1, batas_bawah2=None, batas_atas2=None):
        mask = cv2.inRange(self.hsv, batas_bawah1, batas_atas1)
        if batas_bawah2 is not None:
            mask |= cv2.inRange(self.hsv, batas_bawah2, batas_atas2)  # Gunakan bitwise OR untuk menggabungkan mask
        
        kontur, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        kontur_terbesar = max(kontur, key=cv2.contourArea, default=None)
        if kontur_terbesar is not None:
            x, y, w, h = cv2.boundingRect(kontur_terbesar)
            return (x + w // 2, y + h // 2)
        
        return None
