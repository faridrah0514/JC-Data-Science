# print(1+1)
# print('test aja ah')

'''
nama nama nama
saya saya saya
makan makan makan
'''
nama = "Andi" #string
usia = 14 #integer
tinggi = 189.300 #float
jomblo = True # boolean

print(type(nama))
print("Halo, aku", nama)

print("test deh", usia)


print('test \'ah')

print("jajajajajajaj\
    jsjsjsjsjsjsjs\
        skssjsjsj")

print("makan\nmakan")
print('nama %s usia %d' % (nama,usia))
print('nama {} usia {}'.format(nama,usia))
print(f'Saya {nama} usia {usia}')
print('TEST SEMUANYA'.lower())
print('apa aja saya suka'.upper())

print('Nah Kalau ini Lower apa Upper'.isupper())
'''
selanjutnya pake ini
'''
#mencari jumlah huruf
print(len('masak masak'.replace(' ', '')))

print("menghitung huruf m")

print('purwadhika'.index("d"))

print('masak masak'.count('m'))


misal = "python oke sekali"
#[start:stop:step]
print(misal[4:len(misal):2])
print(misal.index('o'))


k="purwadhika school"
print((k.index("c")))

print("ini coba dulu")
print(k.__len__)





nama2='Purwadhika Startup & Coding School'
#jumlah huruf 'c' ?
print("jumlah huruf c")
print(nama2.lower().count('c'))
huruf="a"
x=nama2.lower().replace(huruf.lower(),"")
jml_huruf = len(nama2) - len(x)
print(f"jumlah huruf {huruf} ada {jml_huruf}")

#jumlah kata 'startup'?
print("jumlah kata startup")
print(nama2.lower().count('startup'))
