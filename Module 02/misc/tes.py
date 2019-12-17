import requests
from bs4 import BeautifulSoup
import pandas as pd

url='http://www.viraindo.com/notebook.html'
data=requests.get(url)

# print(data.content)
df = pd.read_html(url)
export_csv = df[0].to_csv('/Users/Farid/Documents/harga_laptop.csv')
# print(df[0])