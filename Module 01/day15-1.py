'''
#######
#A P I# => RESTFUL
#######

web untuk test API:jsonplaceholder.typicode.com => for dummy data, for testing
untuk coba: https://thesportsdb.com/
untuk coba2: openweathermap.org => username: fr.farid.rahman, api-key: 0286b9bc0ab1586c9aecb24b7fad6800
untuk coba3: quotes.rest
# untuk coba4: tiketux.com
software untuk ngecek API: postman, insomnia

python GET request => API
    import urllib
    import requests
'''

import requests
import urllib

url='http://jsonplaceholder.typicode.com/users'
payload={
    'name': 'Leanne Graham',
}
data=requests.get(url)

print(data.url) # => untuk print url yang di request

# print(data)

output=data.json() # => untuk masukkin data output JSON ke variable
# print(data.json()['address']['street'])
# print(type(data.json()))
# print(data.request)
print(output)
# for i in output:
#     print(i['address']['street'])

for i in data.json():
    print(f"{i['name']} ada di jalan {i['address']['street']}")

#test website => thestportsdb.com