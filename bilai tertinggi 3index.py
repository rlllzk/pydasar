def main():
    a=int(input("\nmasukan bilangan 1:"))
    b=int(input("\nmasukan bilangan 2:"))
    c=int(input("\nmasukan bilangan 3:"))

    if a>b:
        if a>c:
            maks=a
        else:
            if b>c:
                maks=b
            else:
                maks=c

    print("\nNilai tertinggi adalah %d" % maks)
if __name__=="__main__":
    main()

