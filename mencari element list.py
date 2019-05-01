#mencari element
def main():
    #list
    buah=["durian", "mangga", "apel"]
    print("element: ")
    print(buah)

    #mencari element list
    print("durian berada pada indeks ke- ", buah.index("durian"))
    print("mangga berada pada indeks ke-", buah.index("mangga"))
    print("apel berada pada indeks ke-", buah.index("apel"))

if __name__=="__main__":
    main()