import os

def main():
    os.chdir("D:\\code\\fundamental")
    #data mdalam bentuk list
    data=[
            ["101", "DEWI AYU", "085634234"],
            ["102", "ANJANI", "0857542342"],
            ["103", "BELLA", "0856373435"],
            ["104", "SONYA", "0856342343"],
         ]
    #menulis data ke file
    f=open("data.csv", "w+")
    for baris in data:
        f.write(";".join(baris)+"\n")
    
    f.close()
    #menampilkan isi file
    f=open("data.csv")
    for baris in f:
        print(baris, end='')
if __name__=="__main__":
    main()