#python: lambda function
x = lambda a,b,c:a+b+c

def y(a,b,c):
    return a+b+c

def MyFunction(x):
    return lambda a : \
        a ** x

m = lambda a: \
    True if a % 2 == 0 \
        else False

# print((MyFunction(2))(5))

pangkat2=MyFunction(2)
pangkat3=MyFunction(3)

# print(pangkat2(2))
# print(pangkat3(3))

# print(x(2,3,4))
# print(y(2,3,4))
print(m(2))

test = lambda a:\
    a

#map python
# def y(a):
#     return len(a)


# print(list(map([1,2,3,4],[0,9,8,7])))

a = ['Cokelat', 'Melon', 'Nangka']
b = ['Apel', 'Jeruk', 'Nanas']

def combi(a,b):
    return a+" "+b
x=map(combi, a, b)

print(list(x))

x=[2,4,6,8,10]

def func1(y):
    return y ** 2

x1=map(func1, x)
print(list(x1))

x2=map(lambda a: a ** 2, x)
print(list(x2))

x3=map(lambda a: a ** 2 , x)
print(list(x3))


x4=range(11)

#coba lagi
x = pow(2,2)
y=pow(3,3)

print(x)
print(y)
z=list(map(pow, [2,3], [2,3]))
print(z)

# z1 = list(filter(lambda x,y: x < 2 or y > 4, [1,2,3,4],[6,7,8,9]))
# print(z1)

#reduce
from functools import reduce
angka=[1,2,3,4,5,6,7,8]
# z=reduce(lambda x,y,z: x*y*z, angka)
# print(z)

#filter() in map()
angka=[1,2,3,4,5]
z1=list(
    map(
        lambda x: x*2, filter(
            lambda x: x>3, angka
        )
    )
)
z2=list(
    filter(
        lambda x: x>3, map(
            lambda x: x*2, angka
        )
    )
)
print(z1)
print(z2)

#soal
'''angka = [1-100]
=>angka genap => setiap angka genap x2
=> semua angka hasilnya dijumlahkan satu samal ain'''

from functools import reduce
nomor = list(range(1,101))
hasil=reduce(
    lambda a, b: a+b
    , map(
        lambda x: x*2, filter(
            lambda y: y % 2 == 0, nomor
        )
    )
)
print(f'inilah hasilnya: {hasil}')
