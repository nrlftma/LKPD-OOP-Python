class KarakterSurfer:
    def __init__(self, nama):
        self.nama = nama
        self.skor = 0
        self.koin = 0
        self.is_running = True

    def berlari(self):
        self.is_running = True
        print(f"{self.nama} mulai berlari!")

    def ambil_koin(self, jumlah):
        self.koin += jumlah
        print(f"{self.nama} mendapatkan {jumlah} koin!")

    def tabrak_rintangan(self):
        self.is_running = False
        print(f"{self.nama} menabrak rintangan! GAME OVER!")

    def info_player(self):
        print("=== STATUS PLAYER ===")
        print(f"Nama: {self.nama}")
        print(f"Skor: {self.skor}")
        print(f"Koin: {self.koin}")
        print(f"Sedang berlari: {self.is_running}")

# pengujian objek
player1 = KarakterSurfer("Jake")
player1.info_player()
player1.berlari()
player1.ambil_koin(5)
player1.ambil_koin(10)
player1.info_player()
player1.tabrak_rintangan()
player1.info_player()