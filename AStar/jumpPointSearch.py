class Simpul:
    """Sebuah kelas simpul untuk A* Pathfinding"""

    def __init__(self, induk=None, posisi=None):
        self.induk = induk
        self.posisi = posisi

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, lainnya):
        return self.posisi == lainnya.posisi


def astar(labirin, awal, akhir):
    """Mengembalikan daftar tuple sebagai jalur dari titik awal ke titik akhir dalam labirin"""

    # Buat simpul awal dan akhir
    simpul_awal = Simpul(None, awal)
    simpul_akhir = Simpul(None, akhir)

    # Inisialisasi daftar terbuka dan tertutup
    daftar_terbuka = []
    daftar_tertutup = []

    # Tambahkan simpul awal ke daftar terbuka
    daftar_terbuka.append(simpul_awal)

    # Loop sampai menemukan akhir
    while daftar_terbuka:
        # Ambil simpul saat ini
        simpul_saat_ini = daftar_terbuka[0]
        indeks_saat_ini = 0
        for indeks, item in enumerate(daftar_terbuka):
            if item.f < simpul_saat_ini.f:
                simpul_saat_ini = item
                indeks_saat_ini = indeks

        # Hapus simpul saat ini dari daftar terbuka, tambahkan ke daftar tertutup
        daftar_terbuka.pop(indeks_saat_ini)
        daftar_tertutup.append(simpul_saat_ini)

        # Ditemukan tujuan
        if simpul_saat_ini == simpul_akhir:
            jalur = []
            saat_ini = simpul_saat_ini
            while saat_ini is not None:
                jalur.append(saat_ini.posisi)
                saat_ini = saat_ini.induk
            return jalur[::-1]  # Kembalikan jalur yang dibalik

        # Hasilkan anak-anak
        anak_anak = []
        for posisi_baru in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
            # Dapatkan posisi simpul
            posisi_simpul = (
                simpul_saat_ini.posisi[0] + posisi_baru[0],
                simpul_saat_ini.posisi[1] + posisi_baru[1],
            )

            # Pastikan dalam jangkauan
            if (
                posisi_simpul[0] > (len(labirin) - 1)
                or posisi_simpul[0] < 0
                or posisi_simpul[1] > (len(labirin[len(labirin) - 1]) - 1)
                or posisi_simpul[1] < 0
            ):
                continue

            # Pastikan terrain dapat dilalui
            if labirin[posisi_simpul[0]][posisi_simpul[1]] != 0:
                continue

            # Buat simpul baru
            simpul_baru = Simpul(simpul_saat_ini, posisi_simpul)

            # Tambahkan ke anak-anak
            anak_anak.append(simpul_baru)

        # Loop melalui anak-anak
        for anak in anak_anak:
            # Anak ada dalam daftar tertutup
            if anak in daftar_tertutup:
                continue

            # Buat nilai f, g, dan h
            anak.g = simpul_saat_ini.g + 1
            anak.h = (
                (anak.posisi[0] - simpul_akhir.posisi[0]) ** 2
                + (anak.posisi[1] - simpul_akhir.posisi[1]) ** 2
            )
            anak.f = anak.g + anak.h

            # Anak sudah ada dalam daftar terbuka
            if any(
                simpul_terbuka for simpul_terbuka in daftar_terbuka if anak == simpul_terbuka and anak.g > simpul_terbuka.g
            ):
                continue

            # Tambahkan anak ke daftar terbuka
            daftar_terbuka.append(anak)
    return None  # Kembalikan None jika tidak ada jalur yang ditemukan