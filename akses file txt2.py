import os
def main():
    os.chdir("D:/tes")
    for line in open("sample.txt"):
        print(line, end='')
if __name__=="__main__":
    main()

