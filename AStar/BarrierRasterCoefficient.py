class BRC:
    def barrierRaster(awal, akhir, peta):
        jumlah = 0
        for i in range(awal[1], akhir[1]):
            for j in range(awal[0], akhir[0]):
                if peta[i][j] == 1:
                    jumlah += 1
        lebar = awal[0] - akhir[0]
        tinggi = awal[1] - akhir[1]
        luas = lebar * tinggi
        koeficien = jumlah / luas
        return koeficien
    
    # def barrierRasterLib(self):
    #     sub_peta = self.peta[self.awal[1]:self.akhir[1], self.awal[0]:self.akhir[0]]
    #     self.jumlah = np.jumlah_nonzero(sub_peta == 1)
    #     return self.jumlah
