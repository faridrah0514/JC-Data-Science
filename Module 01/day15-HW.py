'''
untuk di coba
1. get api dari sportsdb, daftar pemain suatu klub
2. input: klub apa?
3. daftar pemain: nama, posisi, usia, negara
4. save ke excel, json, dan csv => nama file-nya adalah nama clubnya => barcelona.xlsx, barcelona.json, barcelona.csv
=> json =[
    {
        "nama": "messi",
        "posisi": "striker"
        "usia": 30
        "negara": "argentina"
    },
    ...
    {...}
]
'''
import requests
from datetime import datetime
import json
import xlsxwriter
import csv

now=datetime.now()
year_now=str(now).split()[0].split('-')
# print(year_now)
club_name=input("Ketik Club: ")
url='https://www.thesportsdb.com/api/v1/json/1/searchplayers.php?t='+club_name
request=requests.get(url)
print(request.headers['Content-Type'])

if request.json()['player']:
    tim_member=[]
    for player in request.json()['player']:
        birth_date=player['dateBorn'].split('-')
        age=int(year_now[0]) - int(birth_date[0])
        if int(birth_date[1]) <= int(year_now[1]) and int(birth_date[2]) < int(year_now[2]):
            age-=1
        PlayerName=player['strPlayer']
        PlayerPosition=player['strPosition']
        PlayerNationality=player['strNationality']
        tim_member.append(
            {
                "Name": PlayerName,
                "Position": PlayerPosition,
                "Age": age,
                "Nationality": PlayerNationality
            }
        )
        print(f"{PlayerName}, {PlayerPosition}, {age}, {PlayerNationality}")
    # print(tim_member)
else:
    print("Tim tidak ditemukan dalam database")
    exit()


if tim_member:
    csv_file=open('Data/Nama_Pemain/'+club_name+'.csv', 'r+', newline='', encoding='utf-8')
    header=['Name','Position','Age','Nationality']
    file=csv.DictWriter(csv_file, fieldnames=header)
    file.writeheader()
    file.writerows(tim_member)

    json_file=open('Data/Nama_Pemain/'+club_name+'.json', 'w', encoding='utf-8')
    json.dump(tim_member, json_file)

    excel_file=xlsxwriter.Workbook('Data/Nama_Pemain/'+club_name+'.xlsx')
    sheet=excel_file.add_worksheet('Nama_Pemain')
    k=list(csv.reader(csv_file))
    for i in range(len(k)):
        for j in range(len(k[i])):
            sheet.write(i,j,k[i][j])
    
    excel_file.close()

    

    
