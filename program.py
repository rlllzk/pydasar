#program bentuk
import sys
def main():
    print("CETAK BENTUK TOOLS v.1")
    def awal():
        while True:
            print('''
    ================================================================
    | 1:kotak 2:kotakkosong 3:segitiga 4:segitigakosong 10:-keluar |
    ================================================================''')
            menu=input("masukan pilihan: ")
            if menu=='1':
                a=int(input("masukan banyak baris:"))
                for y in range(a):
                    for x in range(a):
                        print('*', end='')
                    print()            
            elif menu=='2':
                a=int(input("masukan banyaknya baris:"))
                for y in range (a+1):
                    for x in range (a+1):
                        if(x==0 or y==0 or x==a or y==a):
                            print('*', end='')
                        else:
                            print(' ', end='')
                    print()
            elif menu=='3':
                a=int(input("masukan banyaknya baris:"))
                for i in range(a):
                    print(('*'*(1+2*i)).center(1+2*a))
                print()
            elif menu=='4':
                a=int(input("masukan banyaknya baris:"))
                isi=0
                kosong=0
                for i in reversed(range(a)):
                    for j in range(i+1):
                        print(' ', end='')
                    for k in range(isi+1):
                        if k==0:
                            print('*', end='')
                        else:
                            print(' ', end='')
                    for l in range(isi):
                        if l==kosong:
                            print('*', end='')
                            kosong+=1
                        else:
                            print(' ', end='')
                    isi+=1
                    print()
                for i in range(a+1):
                    print('* ', end='')
            elif menu=='10':
                sys.exit()
            else:
                print("salah masukan angka")
    awal()
if __name__=="__main__":
    main()


