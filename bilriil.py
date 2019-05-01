#bil riil
def main():
    #prompt data float
    bilriil=float(input("masukan bilangan riil: "))
    #menggunakan variabel melakukan perhitungan
    hasil=bilriil*2
    #menampilkan nilai variabel
    print("bilangan yg dimasukan adalah %f" %bilriil)
    print("%f x 2 = %.2f " % (bilriil, hasil))
if __name__=="__main__":
    main()