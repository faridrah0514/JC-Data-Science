#zomato API key=0a9b09f920694447f6adbfb4d6bb6219
#insert API key to header request
import requests

header={
    'user-key': '0a9b09f920694447f6adbfb4d6bb6219'
}

params={
    'entity_id': 74,
    'entity_type': 'city',
    'q': 'soto'
}

req = requests.get('https://developers.zomato.com/api/v2.1/search', params=params, headers=header)

print(req.json())

# requests.get()

# req=requests.post()
