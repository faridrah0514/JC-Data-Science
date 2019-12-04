import pandas as pd
import numpy as np
import json
import xlrd
import mysql.connector
import pymongo

# mydf=pd.read_csv('misc/appstore_games.csv')
# mydf.info()
# print("===")
# print(mydf.describe())

# myxls=xlrd.open_workbook(filename='misc/appstore_games.xlsx')
# sheet=myxls.sheet_by_name('appstore_games')
# header=sheet.row_values(0)[:18]
# print(header)
# data=[]
# for i in range(1,sheet.nrows):
#     data.append(sheet.row_values(i)[:18])

# json_file=open('misc/iris.json', 'r')
# loader=json.load(json_file)
# # loader2=json.loads()
# # print(loader)
# df3=pd.DataFrame(loader)
# print(df3)
# dbdetail={
#     "user": "admin",
#     "password": "admin",
#     "host": "localhost",
#     "database": "world"
# }
# mydb=mysql.connector.connect(**dbdetail)
# cursor=mydb.cursor()
# cursor.execute("describe country")
# header=cursor.fetchall()
# head=[]
# for i in header:
#     head.append(i[0])
# # print(head)
# cursor.execute("select * from country")
# df4=cursor.fetchall()
# pd_df=pd.DataFrame(df4,columns=head)
# print(pd_df)

myclient=pymongo.MongoClient("mongodb://localhost:27017")
mydb=myclient['resto']
mycol=mydb['resto']
data=list(mycol.find())
# print(data)

pd_df2=pd.DataFrame(data)
print(pd_df2['grades'])



