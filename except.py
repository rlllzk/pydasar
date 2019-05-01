import sys
def  main():
    try:
        filename="samplex.txt"
        f=open(filename)

        for line in f:
            print(line, end='')

        f.close()
    except IOError as e:
        print("File '%s' tidak ditemukan" % filename)
        sys.exit()
if __name__=="__main__":
    main() 