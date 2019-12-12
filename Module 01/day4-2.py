days={
    'senin':'monday',
    'selasa':'tuesday',
    'rabu':'wednesday',
    'kamis':'thursday',
    'jumat':'friday',
    'sabtu': 'saturday',
    'minggu': 'sunday'
}

nama_hari=input("masukkan nama hari: ").lower()
k=[list(days.values()),list(days.keys())]

if nama_hari in days.keys():
    print(f"bahasa inggrisnya {nama_hari} adalah {days[nama_hari]}")
elif nama_hari in days.values():
    print(f"bahasa indonesianya {nama_hari} adalah {k[1][k[0].index(nama_hari)]}")
else:
    print("ra ono")
