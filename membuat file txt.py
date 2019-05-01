def main():
    f=open("sample1.txt", "w")

    f.write("Industri 4.0\n")
    f.write("Kita Sambut\n")
    f.write("Kesuksesan kita\n")
    f.close()

    #membaca file sample1.txt
    for line in open("sample1.txt"):
        print(line, end='')
if __name__=="__main__":
    main()
