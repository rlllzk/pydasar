def main():
    a=100
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
if __name__=="__main__":
    main()