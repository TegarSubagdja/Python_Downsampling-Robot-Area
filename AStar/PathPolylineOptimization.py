import numpy as np
import pandas as pd

class NodeCut:
    @staticmethod
    def supercover_line(awal, akhir):
        x1, y1 = awal
        x2, y2 = akhir

        points = []
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        x, y = x1, y1
        xstep = 1 if x2 > x1 else -1
        ystep = 1 if y2 > y1 else -1

        ddy = 2 * dy
        ddx = 2 * dx

        points.append((x, y))

        if ddx >= ddy:  # First octant (0 <= slope <= 1)
            errorprev = error = dx  
            for _ in range(dx):
                x += xstep
                error += ddy
                if error > ddx:
                    y += ystep
                    error -= ddx
                    if error + errorprev < ddx:
                        points.append((x, y - ystep))
                    elif error + errorprev > ddx:
                        points.append((x - xstep, y))
                    else:
                        points.append((x, y - ystep))
                        points.append((x - xstep, y))
                points.append((x, y))
                errorprev = error
        else:  # Second octant (1 < slope)
            errorprev = error = dy
            for _ in range(dy):
                y += ystep
                error += ddx
                if error > ddy:
                    x += xstep
                    error -= ddy
                    if error + errorprev < ddy:
                        points.append((x - xstep, y))
                    elif error + errorprev > ddy:
                        points.append((x, y - ystep))
                    else:
                        points.append((x - xstep, y))
                        points.append((x, y - ystep))
                points.append((x, y))
                errorprev = error

        return points
    
    @staticmethod
    def has_obstacle(nodes, peta):
        """Check if any node in the path is an obstacle (1)."""
        return any(peta[y][x] == 1 for x, y in nodes)

    @staticmethod
    def prunning(jalur, peta):
        awal = 3
        jalur_prunning = [jalur[awal]]
        for akhir in range(awal, len(jalur)):
            titikPotong = NodeCut.supercover_line(jalur[awal], jalur[akhir])
            if NodeCut.has_obstacle(titikPotong, peta):
                print("Titik Potong untuk awal ", jalur[awal], "akhir ", jalur[akhir], "adalah", titikPotong, "Memotong")
            else:
                print("Titik Potong untuk awal ", jalur[awal], "akhir ", jalur[akhir], "adalah", titikPotong)


        return 1

# Example usage:
from main import utama

peta, jalur = utama()

peta_ori = peta

# Cetak jalur
if jalur:
    print("Jalur ditemukan:", jalur)

    for titik in jalur:
        peta[titik[1], titik[0]] = 7  # Tandai jalur dengan nilai 7
    
    # Ubah nilai dalam array sesuai permintaan
    peta = np.where(peta == 0, '.', peta)  # 0 menjadi titik (.)
    peta = np.where(peta == '1', '#', peta)  # 1 menjadi halangan (#)
    peta = np.where(peta == '2', '#', peta)  # 2 menjadi halangan (#)
    peta = np.where(peta == '7', '@', peta)  # 7 menjadi jalur (*)

    # Konversi peta ke pandas DataFrame untuk visualisasi yang lebih baik
    df = pd.DataFrame(peta)
    print("Peta dengan Jalur (direpresentasikan oleh 2):")
    print(df)
else:
    print("Tidak ada jalur yang ditemukan")

print("Jalur sebelumnya ", jalur)
print("Jalur Setelah Prunning ", NodeCut.prunning(jalur, peta_ori))
