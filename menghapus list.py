#menghapus data list
def main():
    #list sebelum dihapus
    buah=["durian", "mangga", "apel"]
    print("sebelum dihapus: ")
    print(buah)

    #setelah dihapus()
    buah.remove("apel")
    print("\nSetelah dihapus():")
    print(buah)

    #hapus semua()
    buah.clear()
    print("\nsetelah clear():")
    print(buah)

if __name__=="__main__":
    main()