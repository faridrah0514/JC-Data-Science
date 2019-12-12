import pymongo
import datetime

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient['pymongodb']
mycollection=mydb['colmong2']

mycollection.insert_one({"nama": "Bunga", "waktu": datetime.datetime.now()})
print(f'''ini query-nya

{list(mycollection.find())}
''')
print(list(mycollection.find())[0]['waktu'])

'''
query={"usia" : {"$gte": 24}}
query_and={'$and': [{'usia' : {'$gte': 22}}, {'usia': {'$lte': 30}}]}


query_and={
    '$and':[
        {
            'usia': {
                '$gte': 22
            }
        },
        {
            'usia':{
                '$lte': 30
            }
        }
    ]
}

set_data={'$set': {'nama': 'youngman'}}

print(list(mycollection.find(query_and)))

mycollection.update_many(query_and, set_data)
'''