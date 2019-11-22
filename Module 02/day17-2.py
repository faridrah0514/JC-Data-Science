from bs4 import BeautifulSoup
import requests
import csv

url='http://digidb.io/digimon-list/'
open_url=requests.get(url)
# print(open_url.content)
bs = BeautifulSoup(open_url.content, 'html.parser')

# header=bs.find_all('tr', class_='header')
header=bs.tr
header=header.find_all('th')
# header=header.find('tr',class_="header")
# print(header.text)
tbody=bs.tbody
tr=tbody.find_all('tr')
# print(td[0].find_all('td'))
# head=[]
# for j in header.text:
#     head.append(j)
# print(header)
head=[]
for i in header:
    head.append(i.text)
head.insert(1,"img-url")
# print(head)
data=[]
for i in range(len(tr)):
    new_data=[]
    for k in tr[i].find_all('td'):
        #print(str(k.text).lstrip(), end=",")
        new_data.append(str(k.text).lstrip())
    new_data.insert(1,tr[i].find('img')['src'])
    data.append(dict(zip(head,new_data)))

print(data)
file_csv=open('digimon.csv', 'w', newline='')
writer=csv.DictWriter(file_csv,fieldnames=head)
writer.writeheader()
writer.writerows(data)