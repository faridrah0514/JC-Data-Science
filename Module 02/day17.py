#webscraping using beautiful soup
'''
webscraping tutorial https://www.dataquest.io/blog/web-scraping-beautifulsoup/
'''
# import bs4
from bs4 import BeautifulSoup
import requests

#from HTML file
data = BeautifulSoup(
    open('test.html', 'r'), 'html.parser'
)

    # print(data.prettify())
    # print(f'data.title: {data.title}')
    # print(data.title.name)
    # print(data.title.text)
    # print(data.title.string)
    # # print(data.h1.string)
    # # print(data.h1.text)
    # print(f'data ul text :{data.ul.text}')
    # print(data.find_all('h1'))
    # print(data.find(class_ = 'orang'))
    # print(data.find_all(class_ = 'orang'))
    # print(data.findAll(class_ = 'orang'))
print(data.find(class_ = 'orang'))
print(data.find('li', class_ = 'orang'))

print(data.ul)

for i in data.find_all('li', class_ = 'orang'): #pake "class_" karena keyword class itu udah reserved keyword di python
    print(i.text)

for k in data.find_all('li', id = "person"):
    print(k.text)


#webscrapping dari url
#import request

web = requests.get('http://127.0.0.1:5500/test.html')
bs = BeautifulSoup(web.content, 'html.parser')
web2 = requests.get('http://digidb.io/digimon-list/')
bs2 = BeautifulSoup(web2.content, 'html.parser')

thead=bs2.thead
tbody=bs2.tbody
print(bs.find_all('li', id="person"))
# print(bs2.find_all('tr'))
print(thead.find_all('tr'))
print(tbody.find_all('tr')[0])