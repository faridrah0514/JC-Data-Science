hari = [
    'Mon',
    'Tue',
    'Wed',
    'Thu',
    'Fri',
    'Sat',
    'Sun'
]

print(hari[0])
skrg='Tue'
brpHari=3

#soal
print(f"sekarang adalah hari {skrg}, hari apakah {brpHari} hari lagi?")
itung=brpHari%len(hari)
print(hari[(hari.index(skrg)+itung)%7])
print(f"sekarang adalah hari {skrg}, hari apakah {brpHari} yang lalu?")
itung_harilalu=brpHari%len(hari)
print(hari[hari.index(skrg)-itung_harilalu])