'''
url=http://www.scifijapan.com/articles/2015/10/04/bandai-ultraman-ultra-500-figure-list/
'''
from bs4 import BeautifulSoup
import requests

url='http://www.scifijapan.com/articles/2015/10/04/bandai-ultraman-ultra-500-figure-list/'
web=requests.get(url)
bs = BeautifulSoup(web.content, 'html.parser')
div=bs.find_all('strong')

print("===ULTRAMAN===")
for i in div[2:36]:
    print(i.text)
print("")
print("====MONSTER====")
for i in div[37:110]:
    print(i.text)
