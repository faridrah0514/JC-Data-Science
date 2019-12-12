from bs4 import BeautifulSoup
import requests
import csv
import mysql.connector

class digimon:
    head=[]
    def scrapping(self):
        url='http://digidb.io/digimon-list/'
        open_url=requests.get(url)
        bs = BeautifulSoup(open_url.content, 'html.parser')

        header=bs.tr
        header=header.find_all('th')
        tbody=bs.tbody
        tr=tbody.find_all('tr')
        for i in header:
            self.head.append(i.text)
        self.head.insert(1,"img_url")
        self.head[0] = 'no'
        self.head[7] = 'Equip_Slots'
        self.head[12] = 'Intelligence'
        data=[]
        for i in range(len(tr)):
            new_data=[]
            for k in tr[i].find_all('td'):
                new_data.append(str(k.text).lstrip())
            new_data.insert(1,tr[i].find('img')['src'])
            # data.append(dict(zip(head,new_data)))
            data.append(tuple(new_data))
        return data

    def write_to_csv(self, csv_file_name):
        pass

    def create_db(self):
        self.db_name = 'digimon'
        return f'create database if not exists {self.db_name}'

    def connect_db(self):
        return f'use {self.db_name}'

    def create_table(self):
        self.table_name='digimon'
        return f'''
create table if not exists {self.table_name}(\
no int(5) not null auto_increment,\
img_url varchar(100),\
digimon varchar(50),\
stage varchar(50),\
type varchar(50),\
attribute varchar(50),\
memory int(5),\
equip_slots int(5),\
HP int(10),\
SP int(5),\
Atk int(5),\
Def int(5),\
Intelligence int(5),\
Spd int(5),\
primary key (no)\
);
'''
    def create_and_connect(self, **kwargs):
        self.data={
            'username': kwargs['username'],
            'password': kwargs['password'],
            'host': kwargs['host']
        }
        db = mysql.connector.connect(**self.data)
        cursor = db.cursor()
        cursor.execute(self.create_db())
        cursor.execute(self.connect_db())
        cursor.execute(self.create_table())
        db.close()
    
    def drop_table(self):
        pass

