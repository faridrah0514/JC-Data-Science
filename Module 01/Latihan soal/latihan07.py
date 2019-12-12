def batas():
    print("----------------------------------")

def star(x):
    star=''
    for _ in range(x):
        star+=' * '
        print(star)

star(5)
batas()
def star_reverse(x):
    #star=' * '
    k = x
    for _ in range(x):
        star=' * '*k
        print(star)
        k -= 1
star_reverse(5)
batas()

def segitigaAngka(x):
    for i in range(x):
        k = i + 1
        kata=''
        for m in range(1, k+1):
            kata += str(m) + ' '
        print(kata)

segitigaAngka(5)

batas()

def segitigaAngkaReverse(x):
    k = x
    for _ in range(x):
        kata=''
        for m in range(k):
            kata += str(m+1) + ' '
        print(kata)
        k -=1

segitigaAngkaReverse(5)
batas()

def segitigaAngka2(x):
    for i in range(x):
        k = i+1
        kata=''
        for _ in range (k):
            kata += str(k) + ' '
        print(kata)
segitigaAngka2(5)

batas()
def segitigaAngka2Reverse(x):
    for i in range(x):
        k = x - i
        kata=''
        for _ in range(k):
            kata += str(i+1) + ' '
        print(kata)

segitigaAngka2Reverse(5)
batas()

def segitigaAngkaBesar(x):
    for i in range(x):
        k = x
        kata=''
        for _ in range(i+1):
            kata += str(k) + ' ' 
            #print(k)
            k-=1
        print(kata)
segitigaAngkaBesar(5)
batas()
def segitigaAngkaBesarReverse(x):
    for i in range(x):
        k= x
        kata=''
        for _ in range(x-i):
            kata += str(k) + ' '
            k -=1
        print(kata)
segitigaAngkaBesarReverse(5)
batas()

def pangkat(x,y):
    hasil=1
    for _ in range(abs(y)):
        hasil*=x
    return hasil if y > 0 else float(1/hasil)
    #print(float(hasil))

print(pangkat(2,-1))
#rekursif function: fungsi yang di dalamnya memanggil dirinya sendiri
def pangkatB(x,y):
    if y == 1:
        return x
    else:
        return x * pangkatB(x, y-1)

def pangpangkat(x,y):
    return pangkatB(x,y) if y > 0 else float(1/(pangkatB(x,y)))

print(pangpangkat(2,3))


# print(pangkatB(2,10))

#faktorial
def factorial(x):
    return 1 if x <= 1 else (x*factorial(x-1))

print(factorial(4))


