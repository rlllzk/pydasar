def main():
    a="python"
    for c in a:
        print (c+ ' ', end='')
    print("\n===========")
    b=["python","ruby","perl","php"]
    for e in b:
        print (e)

    c={'one':"satu",'two':"dua",'three':"tiga"}
    for key in c:
        print("arti '%s' adalah '%s'" %(key, c[key]))
    
    for i in range(6):
        print(i, end='')
    print("\n===========")

    #for index range(start, stop, step):
    for i in range(10,21,2):
        print(i, end='\t')
        
if __name__=="__main__": 
    main()
