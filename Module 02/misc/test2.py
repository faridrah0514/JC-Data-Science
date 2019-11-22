import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="admin",
    passwd="admin",
    database="testdb1"
)
table="new_table"
mycursor=mydb.cursor()

# number=int(input("berapa data yang mau di insert: "))
# for i in range(number):
#     nama=str(input("masukkan nama: "))
#     kota=str(input("masukkan kota: "))
#     exe=f"INSERT INTO new_table (nama, kota) VALUES ('{nama}', '{kota}')"
#     print(exe)
#     mycursor.execute(exe)
#     mydb.commit()

mycursor.execute("select * from new_table")
result=mycursor.fetchall()
print(result)