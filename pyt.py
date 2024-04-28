class Buku:
    def __init__(self, judul, penulis, genre, status):
        self.judul = judul
        self.penulis = penulis
        self.genre = genre
        self.status = status

    def __str__(self):
        return "{} - {} ({}) - Status: {}".format(self.judul, self.penulis, self.genre, self.status)


class Perpustakaan:
    def __init__(self):
        self.koleksi_buku = []

    def check_ketersediaan(self, buku):
        if buku.status != "Tersedia":
            print("Buku '{}' tidak tersedia untuk dipinjam.".format(buku.judul))

    def tampilkan_buku(self):
        if self.koleksi_buku:
            print("-- Daftar Buku --")
            for buku in self.koleksi_buku:
                print(buku)
        else:
            print("Koleksi buku masih kosong.")

    def cari_buku(self, judul):
        for buku in self.koleksi_buku:
            if buku.judul.lower() == judul.lower():
                print(buku)
                return
        print("Buku dengan judul '{}' tidak ditemukan.".format(judul))

    def pinjam_buku(self, judul, anggota):
        for buku in self.koleksi_buku:
            if buku.judul.lower() == judul.lower():
                if buku.status == "Tersedia":
                    buku.status = "Dipinjam"
                    anggota.buku_pinjaman.append(buku)
                    print("Buku '{}' berhasil dipinjam oleh {}.".format(buku.judul, anggota.nama))
                    return
                else:
                    print("Buku '{}' tidak tersedia untuk dipinjam.".format(buku.judul))
                    return
        print("Buku dengan judul '{}' tidak ditemukan.".format(judul))


class Anggota:
    def __init__(self, nama, ID, alamat=None, nomor_telepon=None):
        self.nama = nama
        self.ID = ID
        self.alamat = alamat
        self.nomor_telepon = nomor_telepon
        self.buku_pinjaman = []

    def tampilkan_buku_pinjaman(self):
        if self.buku_pinjaman:
            print("-- Buku Pinjaman {} --".format(self.nama))
            for buku in self.buku_pinjaman:
                print(buku)
        else:
            print("{} tidak memiliki buku pinjaman.".format(self.nama))


def main():
   
    buku1 = Buku("Bumi", "Tere Liye", "Fiksi", "Tersedia")
    buku2 = Buku("Laskar Pelangi", "Andrea Hirata", "Fiksi", "Tersedia")
    buku3 = Buku("Filosofi Terbang", "Dewi Lestari", "Fiksi", "Dipinjam")

    
    perpustakaan = Perpustakaan()
    perpustakaan.koleksi_buku.extend([buku1, buku2, buku3])

    
    anggota1 = Anggota("Adi", 12345)
    anggota2 = Anggota("Adu", 56789)

    
    print("\n-- Menu Perpustakaan --")
    print("1. Tampilkan Daftar Buku")
    print("2. Cari Buku")
    print("3. Pinjam Buku")
    print("4. Kembalikan")
    angka = int(input("Pilih menu : "))

    if angka == 1:
        perpustakaan.tampilkan_buku()
    elif angka == 2:
        judul = input("Masukkan judul buku : ")
        perpustakaan.cari_buku(judul)
    elif angka == 3:
        perpustakaan.tampilkan_buku()
        judul = input("Judul buku yang akan dipinjam : ")
        perpustakaan.pinjam_buku(judul, anggota1)
    elif angka == 4:
        print("Daftar buku yang sudah dipinjem : ")
        print("1. Filosofi Terbang")
        ank = int(input("Pilih berdasarkan angka : "))
        if ank == 1:
            print("Terima kasih sudah mengembalikan bukunya")
        else:
            print("Maaf buku yang anda kembalikan tidak terdaftar di perpus kami")
    else:
        print("Anda salah memilih.")


if __name__ == "__main__":
    main()
memilih.")


if __name__ == "__main__":
    main()
