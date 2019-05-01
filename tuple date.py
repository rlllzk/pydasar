import datetime as dt
def main():
    BULAN=("januari","februari","maret","april","mei","juni","juli","agustus","september","oktober","november","desember")

    #today akan berisi: 'YYYY-MM-DD'
    today=dt.date.isoformat(dt.date.today())

    yyyy=today[:4]
    mm=today[5:7]
    dd=today[8:]

    print(today)
    print("%s %s %s" % (dd, BULAN[int(mm)-1], yyyy))

if __name__=="__main__":
    main()