import math
def main():
    a=int(input("\nNilai a:"))
    b=int(input("\nNilai b:"))
    c=int(input("\nNilai c:"))

    D=(b*b) - (4*a*c)

    if D<0:
        print("akar-akar imajiner")
        sys.exit(1)
    elif D==0:
        x1=(-b + math.sqrt(D)) / (2*a)
        x2=x1
    else:
        x1=(-b + math.sqrt(D)) / (2*a)
        x2=(-b - math.sqrt(D)) / (2*a)

    print("\nx1 = %d" %x1)
    print("x2 = %d" % x2)
if __name__=="__main__":
    main()