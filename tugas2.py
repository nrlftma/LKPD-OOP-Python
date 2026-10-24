class VirtualPet:
    def __init__(self, nama, jenis):
        self.nama = nama
        self.jenis = jenis
        self.lapar = 50
        self.energi = 100
        self.kebahagiaan = 50

    def beri_makan(self):
        self.lapar = max(0, self.lapar - 20)
        self.kebahagiaan = min(100, self.kebahagiaan + 10)
        print(f"{self.nama} sudah diberi makan!")

    def ajak_bermain(self):
        if self.energi >= 20:
            self.energi -= 20
            self.kebahagiaan = min(100, self.kebahagiaan + 15)
            print(f"{self.nama} senang bermain!")
        else:
            print(f"{self.nama} kelelahan dan perlu istirahat.")

    def istirahat(self):
        self.energi = min(100, self.energi + 30)
        print(f"{self.nama} sedang beristirahat.")

    def cek_status(self):
        print("\n=== STATUS HEWAN ===")
        print(f"Nama: {self.nama}")
        print(f"Jenis: {self.jenis}")
        print(f"Tingkat lapar: {self.lapar}/100")
        print(f"Energi: {self.energi}/100")
        print(f"Kebahagiaan: {self.kebahagiaan}/100")

# pengujian objek
pet1 = VirtualPet("Moly", "Kucing")
pet1.cek_status()
pet1.beri_makan()
pet1.ajak_bermain()
pet1.cek_status()
pet1.istirahat()
pet1.cek_status()