def main():
    #input nilai x y
    print("memasukan data kordinat")
    x=int(input("masukan nilai x:"))
    y=int(input("masukan nilai y:"))

    info="Kordinat ("+str(x)+ "," + str(y) + \
    ") berada pada kuadran "

    #memeriksa nilai x dan y
    if x > 0 and y>0:
        print(info + "r")
    elif x < 0 and y > 0:
        print(info + "II")
    elif x<0 and y<0:
        print(info + "III")
    elif x>0 and y <0:
        print(info + "IV")
    else:
        pass
if __name__=="__main__":
    main()