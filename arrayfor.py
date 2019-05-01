A = [
        [23, 11, 54, 38, 76],
        [14, 12, 32, 43, 78],
        [76, 34, 87, 21, 68],
        [67, 42, 65, 34, 23]
    ]
baris = 4
kolom = 5

def main():
    print("isi array A:")
    #menmapilkan elemen array dua dimensi
    for baris in A:
        for nilai in baris:
            print("%d " % nilai, end='')
        print() #ganti baris
if __name__=="__main__":
    main()