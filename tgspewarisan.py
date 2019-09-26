class Ibu(object):
    def __init__(self, nama, tinggi, berat):
        self.nama = nama
        self.tinggi = tinggi
        self.berat = berat
        
    def cetakData(self):
        print("Nama\t: ", self.nama)
        print("Tinggi\t: " , self.tinggi)
        print("Berat\t: ", self.berat)
        
    def berjalan(self):
        print("Berjalan ke depan")

    def berlari(self):
        print("Berlari dengan cepat")


# class Anak turunan dari class Bapak
class Anak(Ibu):
    def __init__(self, nama, tinggi, berat, rambut):
        self.nama = nama
        self.tinggi = tinggi
        self.berat = berat
        self.rambut = rambut
    def cetakData(self):
        print("Nama\t: ", self.nama)
        print("Tinggi\t: " , self.tinggi)
        print("Berat\t: ", self.berat)
        print("Rambut\t: ", self.rambut)
    def berjalan(self):
        print("Berjalan ke depan")

    def berlari(self):
        print("Berlari dengan cepat")

    
def main():
    anak1 = Anak("Aeni", 148, 48, "Lurus")
    ibu1 = Ibu("Risa", 155, 55)

    print("Anak")
    anak1.cetakData()
    anak1.berjalan()
    anak1.berlari()

    print(' ')
    print("Ibu")
    ibu1.cetakData()
    ibu1.berjalan()
    ibu1.berlari()
    
if __name__ == "__main__":
    main()
 
 
