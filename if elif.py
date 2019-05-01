def main():
    x=float(input("masukan bilangan pertama\t: "))
    y=float(input("masukan bilangan kedua\t: "))
    op=input("masukan operator +-*/ \t: ")
    
    if op=='+':
        print("%.2f + %.2f = %.2f" % (x,y, x+y))
    elif op=='-':
        print("%.2f - %.2f = %.2f" % (x,y, x-y))
    elif op=='*':
        print("%.2f * %.2f = %.2f" % (x,y, x*y))
    elif op=='/':
        print("%.2f / %.2f = %.2f" % (x,y, x/y))
    else:
        print("ERROR: gunakan operator +.-,*,/")
if __name__=="__main__":
    main()