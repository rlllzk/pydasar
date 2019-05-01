def main():
    a=int(input("\nMasukan bilangan a:"))
    b=int(input("\nMasukan bilangan b:"))
    hasilkali=0
    for i in range (0, b):
        hasilkali+=a
    print("\n%d x %d = %d" % (a, b, hasilkali))
if __name__=="__main__":
    main()