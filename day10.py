#############
#inheritance#
#############

class Manusia:
    def __init__(self,nama):
        self.nama = nama

class Pria(Manusia):
    def __init__(self, nama):
        Manusia.__init__(self,nama)
        self.gender = 'Laki-Laki'

class Wanita(Manusia):
    def __init__(self, nama):
        Manusia.__init__(self,nama)
        self.gender = 'Wanita'


objA=Manusia('Andi')
objB=Pria('Andi')
objC=Wanita('Andi')
print(vars(objA))
print(vars(objB))
print(vars(objC))

########################
#Multilevel Inheritance#
########################

class X:
    def __init__(self, x):
        self.x = x

class Y(X):
    def __init__(self,x,y):
        X.__init__(self,x)
        self.y = y

class Z(Y):
    def __init__(self,x,y,z):
        Y.__init__(self,x,y)
        self.z = z

objD=Z('a', 'b', 'c')
print(vars(objD))

######################
#multiple Inheritance#
######################

class Karnivora:
    def __init__(self):
        self.daging = True
        self.nama = 'Karnivora'

class Herbivora:
    def __init__(self):
        self.tumbuhan=True
        self.nama='Herbivora'

class Omnivora(Karnivora, Herbivora):
    def __init__(self):
        Karnivora.__init__(self)
        Herbivora.__init__(self)
        self.McD = True
        self.nama = 'Omnivora'

objE=Omnivora()
print(vars(objE))
#resolution order
print(Omnivora.__mro__)