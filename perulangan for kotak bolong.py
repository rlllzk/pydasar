def main():
    a=10
    for y in range (a+1):
        for x in range (a+1):
            if(x==0 or y==0 or x==a or y==a):
                print('*', end='')
            else:
                print(' ', end='')
        print()
if __name__=="__main__":
    main()