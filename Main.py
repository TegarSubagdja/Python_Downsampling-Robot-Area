import numpy as np

def simplify_grid(small_grid, robot_size):
    # Temukan posisi robot ('r') dalam grid kecil
    robot_positions = np.argwhere(small_grid == 'r')
    if len(robot_positions) == 0:
        raise ValueError("Tidak ada posisi robot ('r') dalam grid kecil.")
    
    # Ambil batas minimum dan maksimum posisi robot
    min_row, min_col = robot_positions.min(axis=0)
    max_row, max_col = robot_positions.max(axis=0)

    # Ukuran grid baru
    new_height = small_grid.shape[0] // robot_size[0]
    new_width = small_grid.shape[1] // robot_size[1]
    new_grid = np.zeros((new_height, new_width), dtype=int)

    # Hitung posisi robot di grid hasil
    robot_row = min_row // robot_size[0]
    robot_col = min_col // robot_size[1]

    # Tandai area robot dengan 1
    new_grid[robot_row, robot_col] = 1

    return new_grid

# Contoh input
small_grid = np.array([
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 'r', 'r', 0, 0, 0, 0, 0],
 [0, 0, 0, 'r', 'r', 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

])

robot_size = (2, 2)  # Ukuran robot dalam grid kecil

# Transformasi grid
result_grid = simplify_grid(small_grid, robot_size)

# Print hasil
print("Grid Disederhanakan:")
print(result_grid)
