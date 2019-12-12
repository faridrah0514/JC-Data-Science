import mysql.connector
sql_detail={
    'user': 'admin',
    'password': 'admin',
    'host': 'localhost',
    'database': 'ptabc'
}
db=mysql.connector.connect(**sql_detail)

cursor=db.cursor()
query="insert into karyawan (nama, gaji) values (%s, %s)"
value=[('amys', 12200000), ('hanny', 21000000)]
cursor.executemany(query, value)
db.commit()

cursor.execute("select * from karyawan")
print(cursor.fetchall())


