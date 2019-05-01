def main():
    #mengakses file
    f=open("sample.txt") #mengembalikan objek file
    line = f.readline() #membaca baris pertama
    while line:
        print(line, end='')
        line=f.readline() #membaca baris berikutnya

    #menutup gile
    f.close
if __name__=="__main__":
    main()