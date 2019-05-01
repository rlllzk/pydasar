import mysql.connector
import sys

def main():
    try:
        #membuat objak koneksi
        conn = mysql.connector.connect(
            user="root",
            password="toor",
            host="127.0.0.1",
            database="pythonDB"
        )
        cur=conn.cursor()
        data1=  ("P1",
                "Pro Python Programming",
                "Obor Publishing",
                "Marx Karl",
                 1983)
        data2=  ("P2",
                "Pro Machine Learning",
                "marxis Publishing",
                "Linus Trovald",
                 1976)
        sql="""
            insert into buku values
            (%s, %s, %s, %s, %s)
            """
        try:
            cur.execute(sql, data1)
            cur.execute(sql, data2)
        
        except mysql.connector.DataError:
            #melakukan rollback data
            conn.rollback()
            print ("Data gagal simpan!")
            sys.exit(1)
        else:
            #melakukan commit data
            conn.commit()
            cur.close()
    except mysql.connector.Error as e:
        print("ERROR lho", e)
    else:
        conn.close()
if __name__=="__main__":
    main()
