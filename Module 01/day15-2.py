'''
input nama club:
munculkan nama pemain dari club yang di cari:
kalau ga ada tim-nya di database, kasih output "tim tidak ditemukan"
'''
import requests

club_name=input("Ketik Club: ")
url='https://www.thesportsdb.com/api/v1/json/1/searchplayers.php?t='+club_name
request=requests.get(url)

if request.json()['player']:
    for player in request.json()['player']:
        print(f"{player['strPlayer']} ({player['strPosition']})")
else:
    print("Tim tidak ditemukan dalam database")
