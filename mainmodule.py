import mymodule

def main():
    a=10
    b=3
    c=3.0

    hasiltambah = mymodule.tambah(a,b)
    hasilkurang = mymodule.kurang(a,b)
    hasilkali = mymodule.kali(a,b)
    hasilbagi1 = mymodule.bagi(a,b)
    hasilbagi2 = mymodule.bagi(a,c)

    print("%d + %d = %d" % (a,b, hasiltambah))
    print("%d - %d = %d" % (a,b, hasilkurang))
    print("%d * %d = %d" % (a,b, hasilkali))
    print("%d // %d = %d" % (a,b, hasilbagi1))
    print("%d / %f = %f" % (a,c, hasilbagi2))
if __name__=="__main__":
    main()