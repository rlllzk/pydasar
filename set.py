import sys
def printElements(s, info):
    print (info)
    if len(s) == 0:
        print("himpunan kosong\n")
        sys.exit(1)
    for e in s:
        print(str(e) + " ", end=' ')
    print("\n")

def main():
    #membuat himpunan
    s=set([11,22,33,44,55])
    printElements(s, "Elemen awal:")

    #menambah elemen
    s.add(66)
    printElements(s, "setelah add():")
    s.update([77,88])
    printElements(s, "setelah update():")
    #hapus elemen
    s.remove(44)
    printElements(s, "setelah hapus 44:")
    #clear elemen
    s.clear()
    printElements(s, "setelah clear")

if __name__=="__main__":
    main()