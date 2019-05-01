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
        #membuat objek kursor
        cur=conn.cursor()
        ddl="""
            create table buku(
                kode char(2) not null primary key,
                judul varchar(50),
                penerbit varchar(30),
                penulis varchar(25),
                tahun integer
            )
            """
        #mengeksekusi statemen sql
        #untuk membuat tabel buku    
        cur.execute(ddl)
        #menutup objek kursor
        cur.close()
    except mysql.connector.Error as e:
        print ("error", e)
    else:
        print("tabel buku sukses dibuat!")
        #menutup objek cursor dan koneksi
        conn.close()
if __name__=="__main__":
    main()
