############
#python OOP#
############

'''class Mobil:
    warna = 'Merah'
    tahun = 2020

mobil1 = Mobil()
mobil2 = Mobil()
'''
# print(mobil1)
# print(type(mobil1))
# print(mobil1.warna)
# print(mobil1.tahun)

# print(mobil2)
# print(type(mobil2))
# print(mobil2.warna)
# print(mobil2.tahun)

class MobilCustom:
    def __init__(self, warna, tahun, model):
        self.warna = warna
        self.tahun = tahun
        self.model = model

    def cetak(self):
        print(f"warna mobilnya adalah {self.warna}")
        print(f"tahun pembuatan mobilnya adalah {self.tahun}")
        print(self.warna, self.tahun, self.model, self.jadul())

    def jadul(self):
        if self.tahun < 2010:
            return True
        else: return False


mobil3 = MobilCustom('hijau', 1990, 'sport')

'''mobil3.cetak()'''
# print(mobil3.jadul())

#############
#inheritance#
#############
class Mobil:
    def __init__(self, warna, tahun):
        self.warna = warna
        self.tahun = tahun

class Car(Mobil):
    # gps = True
    def __init__(self, apalah):
        self.apalah = apalah


mobil4=Mobil('Black', 2019)
mobil5=Car('apasih')
mobil5.warna = 'merah'
mobil5.tahun = '1997'

print(mobil4.warna, mobil4.tahun)
# print(mobil5.warna, mobil5.tahun)
print(mobil5.apalah, mobil5.warna, mobil5.tahun)


class X:
    def __init__(self, nama, gelar):
        self.nama = nama
        self.gelar = gelar

#cara sendiri
'''class Y(X):
    def __init__(self,nama,gelar):
        X.__init__(self,nama)
        self.gelar = gelar
#cara1
class Y(X):
    pass

#cara2
class Y(X):
    def __init__(self, nama, gelar):
        X.__init__(self, nama, gelar)'''

#cara3
class Y(X):
    def __init__(self, nama, gelar, univ):
        super().__init__(nama, gelar)
        self.kampus = univ


obj1 = X("Farid", "Sarjana")
obj2 = Y("Farid", "Master","ITB")
obj3 = Y("Audi", "Doktor", "UGM")

# print(obj2)

print(vars(obj2))

print(getattr(obj2, 'gelar'))
print(hasattr(obj2, 'kampus'))

#cara menambahkan attribut
obj2.warna = 'merah'
obj3.umur = 40
setattr(obj3, 'alamat', 'BSD')
delattr(obj3, 'gelar')
print(vars(obj2))
print(vars(obj3))


class Z:
    nama = 'Z'
    usia = 23

objZ = Z()
print(objZ.nama)
print(objZ.usia)

del Z.nama
# print(objZ.nama) #akan ada error
print(objZ.usia)



class student:
    def __init__(self, nama, usia):
        self.nama = nama
        self.usia = usia

data = [
    {'nama': 'Andi', 'usia': 21},
    {'nama': 'Budi', 'usia': 22},
    {'nama': 'Caca', 'usia': 23},
    {'nama': 'Deni', 'usia': 24},
]

for k in range(len(data)):
    vars()[data[k]['nama']] = student(data[k]['nama'], data[k]['usia'])

'''cara pak guru
def createObj(x):
    return student(x['nama'], x['usia'])

dataNew = list(map(createObj, data))

#akses
print(dataNew[0].nama)
print(dataNew[0].usia)

'''
#salah satu contoh pemanfaatan class

class Persegi:
    def __init__(self, sisi):
        self.sisi = sisi
        self.keliling = self.sisi * 4
        self.luas = self.sisi ** 2

persegi1 = Persegi(10)
print(vars(persegi1))



'''class keRomawi():
    ...........

satu = keRomawi(1) => I
dua = keRomawi(2) => II
tiga = keRomawi(3) => X
maksimal angka 3000
'''