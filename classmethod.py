class tanggal(object):
    def __init__(self, dd=0, mm=0, yyyy=0):
        self.hari = tanggal.hari =dd
        self.bulan= tanggal.bulan = mm
        self.tahun = tanggal.tahun = yyyy

    @classmethod
    def dariString(cls, strTanggal):
        hari, bulan, tahun = map (int, strTanggal.split('-'))
        objekTanggal=cls(hari, bulan, tahun)
        return objekTanggal
    
    def cetakTanggal(self):
        BULAN=["januari", "Februari", "Maret", "April",
                "Mei", "juni", "juli", "Agustus",
                "September", "Oktober", "November", "Desember"]
        print("%d %s %d" % (self.hari, BULAN[self.bulan-1], self.tahun))

def main():
    #membuat objek dari kelas tanggal
    #menggunakan cara yang umum
    obj1=tanggal(19, 5, 1983)

    #membuat objek dari kelas tanggal
    #menggunakan metode kelas
    obj2=tanggal.dariString("13-6-2010")

    #mencetak tanggal
    print("tanggal pada obj1: ", end='')
    obj1.cetakTanggal()
    print("Tanggal pada obj2: ", end='')
    obj2.cetakTanggal()

if __name__=="__main__":
    main()