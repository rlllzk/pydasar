def main():
    n=int(input("\nMasukan bilangan:"))
    if n<0:
        print("\nBilangan tidak boleh negatif")
        sys.exit(1)
    
    faktorial=1

    print("%d!= " % n, end='')
    i=n
    while i >=1:
        if i!=1:
            print("%d x " % i, end='')
        else:
            print("%d = " % i, end='')
        faktorial *=i;
        i -= 1; #decrement

    print(faktorial)
if __name__=="__main__":
    main()