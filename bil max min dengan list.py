def main():
    daftar=[]
    for i in range(1, 20):
        nilai=int(input("masukan bilangan ke-%d: " %i))
        daftar.append(nilai)
    maks=max(daftar) 
    mini=min(daftar)
    print("Nilai tertinggi: %d,nilai terendah: %d" %(maks,mini))
if __name__=="__main__":
    main()