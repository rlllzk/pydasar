def main():
    a=int(input("\nmasukan bilangan 1:"))
    b=int(input("\nmasukan bilangan 2:"))
    c=int(input("\nmasukan bilangan 3:"))

    maks=a
    if b>maks: maks=b
    if c>maks: maks=c

    print("\nNilai tertinggi adalah %d" % maks)
if __name__=="__main__":
    main()

