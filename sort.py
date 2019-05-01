def main():
    list1=[50, 10,40,20,43,32,67,34]
    print("sebelum diurutkan")
    print("list1:", list1)

    list1.sort()
    print("setelah diurutkan")
    print("list1:", list1)
    list1.reverse()
    print("dibalik")
    print("list1:", list1)
    list2=sorted(list1)
    print("urutan list1 tidak dirubah dibawahnya")
    print(list2)
    print(list1)

if __name__=="__main__":
    main()