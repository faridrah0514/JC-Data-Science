'''
webscrapping trus masukin ke mysql
database digimon,

'''
'''
kreasi sendiri
bikin object, object-nya web-scrapping dari website digimon
trus nanti import di sini
abis itu nanti baru bikin database
'''
import digimon
import mysql.connector

param={
    'username': 'admin',
    'password': 'admin',
    'host': 'localhost'
}

digi=digimon.digimon()
digi.create_and_connect(**param)
db = mysql.connector.connect(**param, database=digi.db_name)
cursor = db.cursor()
digimon_data=digi.scrapping()
persen_s="%s, "*len(digimon_data[0])
insert_data=(f"insert into {digi.table_name} {str(tuple(digi.head))} values ({persen_s.rstrip(', ')})").replace("'", '')
try:
    cursor.executemany(insert_data, digimon_data)
    db.commit()
    db.close()
    print("records inserted successfully")
except:
    print("records already exists")



