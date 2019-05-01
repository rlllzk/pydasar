#menambah data list
def main():
    #list
    buah=["durian", "mangga", "apel"]
    print("element awal: ")
    print(buah)

    #metode append()
    buah.append("jeruk")
    print("\nSetelah append():")
    print(buah)

    #metode insert()
    buah.insert(0, "kiwi")
    print("\nSetelah Insert():")
    print(buah)

    #metode extend()
    buah.extend(["melon", "anggur"])
    print("\nSetelah extend():")
    print(buah)

    

if __name__=="__main__":
    main()