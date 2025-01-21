import heapq
import numpy as np
import cv2  # Untuk menggambar pada gambar

class AStar:
    def __init__(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
    
    def heuristic(self, a, b):
        """Menghitung heuristik (jarak Euclidean)."""
        return abs(a[0] - b[0]) + abs(a[1] - b[1])
    
    def valid_move(self, x, y):
        """Memastikan langkah valid di dalam grid dan tidak dalam area yang diblokir (nilai 1)."""
        return 0 <= x < self.rows and 0 <= y < self.cols and self.grid[x][y] == 0
    
    def find_path(self, start, goal):
        """Mencari rute dari start ke goal menggunakan algoritma A*."""
        open_list = []
        heapq.heappush(open_list, (0 + self.heuristic(start, goal), 0, start))
        
        g_costs = {start: 0}
        came_from = {}
        
        while open_list:
            _, current_cost, current = heapq.heappop(open_list)
            
            if current == goal:
                path = []
                while current in came_from:
                    path.append(current)
                    current = came_from[current]
                path.reverse()
                return path  # Mengembalikan jalur yang ditemukan
            
            for direction in self.directions:
                neighbor = (current[0] + direction[0], current[1] + direction[1])
                if self.valid_move(neighbor[0], neighbor[1]):
                    new_cost = current_cost + 1
                    if neighbor not in g_costs or new_cost < g_costs[neighbor]:
                        g_costs[neighbor] = new_cost
                        priority = new_cost + self.heuristic(neighbor, goal)
                        heapq.heappush(open_list, (priority, new_cost, neighbor))
                        came_from[neighbor] = current
        return []  # Tidak ada rute ditemukan

    def draw_path(self, image, path, color=(0, 0, 0), thickness=3):
        """Menggambar jalur A* pada gambar menggunakan garis (atau titik)."""
        for i in range(1, len(path)):
            start_point = (path[i-1][1], path[i-1][0])  # (x, y)
            end_point = (path[i][1], path[i][0])      # (x, y)
            cv2.line(image, start_point, end_point, color, thickness)  # Menggambar garis
        return image
