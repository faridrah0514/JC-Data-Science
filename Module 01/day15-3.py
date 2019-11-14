import requests
from datetime import datetime
from dateutil import tz

url='http://api.openweathermap.org/data/2.5/weather?q='
appid='appid=0286b9bc0ab1586c9aecb24b7fad6800'
kota=input("Ketik Kota: ")
url=f"{url}{kota}&{appid}"
data=requests.get(url)
# print(data.json())
print(f"sunrise: {data.json()['sys']['sunrise']}")
print(f"sunset: {data.json()['sys']['sunset']}")

print(datetime.utcfromtimestamp(int(data.json()['sys']['sunrise'])))
# print(datetime.timetz())
# print(vars(datetime))
local_timezone=tz.gettz('Asia/Jakarta')
print(local_timezone)


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