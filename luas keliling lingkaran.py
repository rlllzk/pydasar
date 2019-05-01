import math
def main():
    print("luas dan keliling lingkaran\n")
    r=float(input("masukan nilai jari-jari:"))
    L=math.pi * (r**2)
    K=2*math.pi * r
    print("Luas \t: %.2f" %(L))
    print("Keliling\t:", K)
if __name__=="__main__":
    main()
