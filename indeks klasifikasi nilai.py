def main():
    uts=float(input("\nNilai UTS:"))
    uas=float(input("Nilai UAS:"))
    na=(0.65 * uas) + (0.35 *uts)

    if na>=80:
        indeks='A'
    elif na>=70:
        indeks='B'
    elif na>=55:
        indeks='C'
    elif na>=40:
        indeks='D'
    else:
        indeks='E'

    print("\nNilai Akhir = %0.2f" % na)
    print("Nilai Indeks= %c" % indeks)
if __name__=="__main__":
    main()