days={
    'senin':'monday',
    'selasa':'tuesday',
    'rabu':'wednesday',
    'kamis':'thursday',
    'jumat':'friday',
    'sabtu': 'saturday',
    'minggu': 'sunday'
}

nama_hari = input('ketik nama hari : ')
print(f"nama hari yang di ketik adalah : {nama_hari}")
print(f"bahasa inggrisnya {nama_hari} adalah {days[nama_hari.lower()]}")
#nama_hari_en = input("ketik nama hari in english : ")
#print(f"bahasa id {nama_hari_en} = {days.value(nama_hari_en)}")
#print(days.keys('senin'))

# print(days.items())
# days.
# k=[list(days.values()),list(days.keys())]
# #k.index('senin')
# nama_hari_en=input("masukkan nama hari : ").lower()
# try:
#     print(f"nama hari {nama_hari_en} dalam bahasa indonesia adalah {k[1][k[0].index(nama_hari_en)]}")
# except ValueError:
#     print("ga ada!")


#m=list(days.items())
# l=dict({days.values})
c={}
for a, b in days.items():
    c[b] = a

hari_en = input("masukkan nama hari en : ").lower()
print(f"bahasa indonesia {hari_en} adalah {c.get(hari_en, 'ga ada')}")