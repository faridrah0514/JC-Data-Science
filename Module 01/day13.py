class X:
    def __init__(self, nama,usia):
        self.nama = nama
        self.usia = usia
    
    def pensiun(self):
        return 55-self.usia

class Y(X):
    def __init__(self, nama, usia, city):
        X.__init__(self, nama, usia)
        self.city = city

objX = X('Farid', 29)
objX.__setattr__('alamat', 'tangerang selatan')

objA=X('banu', 19)
objB=Y('ali',12 ,'jakarta')

# print(objA.kota); print(objB.city)
print(__name__)


print(objX.nama)
print(vars(objX))