import matplotlib.pyplot as plt
import numpy as np

class ImprovedGridIntersector:
    @staticmethod
    def line_intersects_cell(x0, y0, x1, y1, cell_x, cell_y):
        """
        Memeriksa apakah garis memotong sel grid tertentu
        """
        # Koordinat sudut sel
        x_min, x_max = cell_x - 0.5, cell_x + 0.5
        y_min, y_max = cell_y - 0.5, cell_y + 0.5
        
        # Jika salah satu titik ujung ada di dalam sel
        if (x_min <= x0 <= x_max and y_min <= y0 <= y_max) or \
           (x_min <= x1 <= x_max and y_min <= y1 <= y_max):
            return True
            
        # Menghitung parameter garis: y = mx + b
        if x1 - x0 != 0:  # Jika garis tidak vertikal
            m = (y1 - y0) / (x1 - x0)
            b = y0 - m * x0
            
            # Titik potong dengan batas vertikal sel
            for x in [x_min, x_max]:
                y = m * x + b
                if y_min <= y <= y_max and min(x0, x1) <= x <= max(x0, x1):
                    return True
                    
            # Titik potong dengan batas horizontal sel
            for y in [y_min, y_max]:
                if m != 0:  # Jika garis tidak horizontal
                    x = (y - b) / m
                    if x_min <= x <= x_max and min(y0, y1) <= y <= max(y0, y1):
                        return True
        else:  # Garis vertikal
            if x_min <= x0 <= x_max and \
               min(y0, y1) <= y_max and max(y0, y1) >= y_min:
                return True
                
        return False

    @staticmethod
    def find_all_intersected_cells(start, end, grid_size=(10, 10)):
        """
        Menemukan semua sel grid yang benar-benar terpotong oleh garis
        """
        x0, y0 = start
        x1, y1 = end
        intersected_cells = set()
        
        # Menggunakan Bresenham untuk mendapatkan sel-sel dasar
        dx = abs(x1 - x0)
        dy = abs(y1 - y0)
        sx = 1 if x0 < x1 else -1
        sy = 1 if y0 < y1 else -1
        
        x, y = x0, y0
        
        # Memeriksa area yang lebih luas di sekitar garis
        for i in range(max(grid_size[0], grid_size[1])):
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    check_x = x + dx
                    check_y = y + dy
                    if (0 <= check_x < grid_size[0] and 
                        0 <= check_y < grid_size[1] and
                        ImprovedGridIntersector.line_intersects_cell(
                            x0, y0, x1, y1, check_x, check_y)):
                        intersected_cells.add((check_x, check_y))
            
            if x == x1 and y == y1:
                break
                
            e2 = 2 * dy - dx
            if e2 > 0:
                y += sy
                dy -= dx
            x += sx
            dx += dy
            
        return list(intersected_cells)

    @staticmethod
    def visualize_intersection(start, end, grid_size=(10, 10)):
        """
        Memvisualisasikan grid dan sel yang terpotong
        """
        plt.figure(figsize=(10, 10))
        
        # Menggambar grid
        for i in range(grid_size[0] + 1):
            plt.axvline(x=i-0.5, color='gray', linestyle='-', alpha=0.3)
        for i in range(grid_size[1] + 1):
            plt.axhline(y=i-0.5, color='gray', linestyle='-', alpha=0.3)
            
        # Mendapatkan dan plot sel yang terpotong
        intersected = ImprovedGridIntersector.find_all_intersected_cells(start, end, grid_size)
        for cell in intersected:
            plt.fill([cell[0]-0.5, cell[0]+0.5, cell[0]+0.5, cell[0]-0.5],
                    [cell[1]-0.5, cell[1]-0.5, cell[1]+0.5, cell[1]+0.5],
                    'lightblue', alpha=0.5)
            
        # Plot garis
        plt.plot([start[0], end[0]], [start[1], end[1]], 'r-', linewidth=2)
        
        # Plot titik awal dan akhir
        plt.plot(start[0], start[1], 'go', label='Start')
        plt.plot(end[0], end[1], 'ro', label='End')
        
        plt.grid(True)
        plt.legend()
        plt.title('All Grid Cells Intersected by Line')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.axis('equal')
        plt.xlim(-0.5, grid_size[0]-0.5)
        plt.ylim(-0.5, grid_size[1]-0.5)
        
        return intersected

# Contoh penggunaan
start_point = (1, 1)
end_point = (8, 6)
grid_size = (10, 10)

intersected_cells = ImprovedGridIntersector.visualize_intersection(start_point, end_point, grid_size)
print("Sel grid yang terpotong:", sorted(intersected_cells))
plt.show()