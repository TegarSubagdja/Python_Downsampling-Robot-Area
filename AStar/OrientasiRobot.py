import cv2
import numpy as np
from cv2 import aruco

def detect_aruco_realtime():
    # Inisialisasi kamera
    cap = cv2.VideoCapture(0)
    
    # Membuat dictionary ArUco
    # Menggunakan 6x6 bits dengan 250 marker unik
    aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_6X6_250)
    detector = aruco.ArucoDetector(aruco_dict)
    
    while True:
        # Membaca frame dari kamera
        ret, frame = cap.read()
        if not ret:
            break
            
        # Mengubah frame ke grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Deteksi ArUco marker
        corners, ids, rejected = detector.detectMarkers(gray)
        
        # Jika marker terdeteksi
        if ids is not None:
            # Gambar marker yang terdeteksi
            aruco.drawDetectedMarkers(frame, corners, ids)
            
            # Tampilkan ID dan koordinat tengah setiap marker
            for i, marker_id in enumerate(ids):
                # Hitung koordinat tengah marker
                corner = corners[i][0]
                center_x = int(np.mean(corner[:, 0]))
                center_y = int(np.mean(corner[:, 1]))
                
                # Tampilkan ID marker
                cv2.putText(frame, f"ID: {marker_id[0]}", (center_x, center_y), 
                          cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                
                # Tampilkan koordinat
                coord_text = f"({center_x}, {center_y})"
                cv2.putText(frame, coord_text, (center_x, center_y + 20),
                          cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        
        # Tampilkan jumlah marker yang terdeteksi
        marker_count = 0 if ids is None else len(ids)
        cv2.putText(frame, f"Markers detected: {marker_count}", (10, 30),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        
        # Tampilkan frame
        cv2.imshow('ArUco Marker Detection', frame)
        
        # Tekan 'q' untuk keluar
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # Bersihkan
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    detect_aruco_realtime()