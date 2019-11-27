import mysql.connector
sql_detail={
    'user': 'admin',
    'password': 'admin',
    'host': 'localhost',
    'database': 'ptabc'
}
db=mysql.connector.connect(**sql_detail)

cursor=db.cursor(dictionary=True)

# cursor.execute("update karyawan set nama=%s where nama=%s", ('Wahyuni', 'Yuni'))
# cursor.execute("update karyawan set nama=%s, gaji=%s where id_kar=%s", ('Zizi', 20000000, 20))
cursor.execute("alter table karyawan\
    modify column\
        hobby varchar(255)\
            after gender")
db.commit()
# print(cursor.fetchall())

'''
    lanjut ke relational db concept
'''

'''insert into tablea values
(1,'Andi',1),
(2,'Budi',1),
(3,'Caca',2),
(4,'Deni',2),
(5,'Euis',1);'''

'''insert into tableb values
(1, 'Human Resource'),
(2, 'Marketing'),
(3, 'Finance'),
(4, 'Engineer');'''
