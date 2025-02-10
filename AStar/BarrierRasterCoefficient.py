import numpy as np
import time

class BRC:
    def __init__(self, start, end, matrix,):
        if not isinstance(matrix, (list, np.ndarray)):
            raise ValueError("Matriks harus berupa list atau numpy array")
        
        self.matrix = matrix
        self.start = start
        self.end = end
        self.count = 0
    
    def get_matrix(self):
        return self.matrix
    
    def get_params(self):
        return self.start, self.end
    
    def barrierRaster(self):
        start = time.time()
        for i in range(self.start[1], self.end[1]):
            for j in range(self.start[0], self.end[0]):
                if self.matrix[i][j] == 1:
                    self.count += 1
        end = time.time()
        print("Waktu tanpa library : ", end-start)
        return self.count
    
    def barrierRasterLib(self):
        start = time.time()
        sub_matrix = self.matrix[self.start[1]:self.end[1], self.start[0]:self.end[0]]
        self.count = np.count_nonzero(sub_matrix == 1)
        end = time.time()
        print("Waktu dengan library : ", end-start)
        return self.count
