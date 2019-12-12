import requests
api_url='https://kurs.web.id/api/v1/'
bitcoin_url='https://blockchain.info/tobtc?currency=USD&value='

print("####################")
print("pilih opsi: ")
print("1. USD => IDR")
print("2. IDR => USD")
print("3. USD => Bitcoin")
print("4. IDR => Bitcoin")
print("####################")
opsi=int(input("Pilihan Anda (1/2/3/4): "))

if opsi in [1,2,3,4]:
    nama_bank=input('Ketik nama bank: ')
    req = requests.get(api_url+nama_bank)
    content=req.json()
    if content['error'] == 'true':
        print("input nama bank salah")
        exit()
    nominal=float(input('Ketik nominal: '))
    idr_beli=float(content['beli'])
    idr_jual=float(content['jual'])
    idr_to_usd=round((nominal/idr_jual),2)
    if opsi == 1:
        print(f"{nominal} USD = Rp {nominal*idr_beli}")
    elif opsi== 2:
        print(f"Rp {nominal} = USD {idr_to_usd}")
    elif opsi == 3:
        req2= requests.get(bitcoin_url+str(nominal))
        print(f"{nominal} USD = {float(req2.json())} Bitcoin")
    else:
        req2= requests.get(bitcoin_url+str(idr_to_usd))
        print(f"{nominal} IDR = {round((req2.json()),5)} Bitcoin")
else:
    print("Salah input!")
