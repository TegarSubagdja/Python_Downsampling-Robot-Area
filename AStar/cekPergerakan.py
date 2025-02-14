import math

def is_one_point_move(awal, akhir):
    x1, y1 = awal
    x2, y2 = akhir
    if (math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2) <= 1.5):
        return True
    else:
        return False
    
def is_45_degree(awal, akhir):
    x1, y1 = awal
    x2, y2 = akhir
    
    if x2 - x1 == 0:  # Menghindari pembagian dengan nol (garis vertikal)
        return False
    slope = (y2 - y1) / (x2 - x1)
    return slope == 1 or slope == -1
    
awal = (5,4)
akhir = (15,14)

print(is_45_degree(awal, akhir))