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

def bresenham(awal, akhir):
    x1, y1 = awal
    x2, y2 = akhir
    points = []
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1
    err = dx - dy
    
    while True:
        points.append((x1, y1))
        if x1 == x2 and y1 == y2:
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x1 += sx
        if e2 < dx:
            err += dx
            y1 += sy
    
    return points
    
awal = (5,4)
akhir = (8,1)

print(is_45_degree(awal, akhir))
print(bresenham(awal, akhir))