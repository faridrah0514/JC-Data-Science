x=12
x=13
x+=2
x-=2
x*=2
x/=2
print(x)

x ='abcdefghijklmnopqrstuvwxyz'
print(x[::2])
print('g' in x)
print(x.count('g'))
y=12
print(lambda y: y + 12)

def batas():
    print("==================================================================")

batas()
kalimat="Hari ini Andi tidak Kuliah"
cari='h'
print(cari.lower() in kalimat.lower())
print(kalimat.lower().count(cari.lower()))
batas()
x=['Andi', 'Budi', 'Caca', 123, True]
print(x[len(x) - 1])
print(type(x[-1]))
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

batas()

hari.append('senin2')
print(hari)
hari.insert(4, 'senin3')
print(hari)

batas()


hari.reverse() #reverse by index
print(hari)
hari = hari[::-1] #reverse by index
print(hari)

x = [1,2,3,4,5]
print(list(reversed(x)))
print()

batas()

z = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(z[0])



a=[2,3,4,5,6,3]