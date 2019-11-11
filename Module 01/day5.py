def batas():
    print("====================================")
'''
review
variable string integer list tuple dictionary frozenset
'''

def hello():
    print("hello world!")

#f(x) = x^2
def kuadrat(angka):
    print(angka ** 2)

'''
kuadrat(2)
kuadrat(3)
'''

def pangkat(angka1, angka2):
    print(angka1 ** angka2)
'''
pangkat(2,3)
pangkat(10,2)
'''

# pangkat(
#     float(input("ketik angka1: ")),
#     float(input("ketik angka2: "))
# )

'''
sebuah function dg 1 parameter
function => menentukan value param: ganjil/genap
'''

def gage(x):
    if x % 2 == 0:
        print(f"angka {x} adalah genap")
    else:
        print(f"angka {x} adalah ganjil")

'''
gage(-2)
gage(99)
'''

'''
sebuah function

input:
1. masukkan angka1: 
2. masukkan operator aritmatika: + - * /
3. masukkan angka2:

contoh:
angka1: 10
operator *
angka2: 2

output:
20
'''

def kalkulator(angka1, angka2, operator):
    if operator == "+":
         print(angka1 + angka2)
    elif operator == "-":
        print(angka1 - angka2)
    elif operator == "/":
        print(angka1 / angka2)
    elif operator == "*":
        print(angka1 * angka2)
    else:
        print("maaf ya!")

# a=float(input("masukkan angka1: "))
# b=str(input("masukkan operator: "))
# c=float(input("masukkan angka2: "))

# kalkulator(a,c,b)


def coba(args, kwargs):
    print(args)
    print(kwargs['nama'])

a = [1,2,3]
b={'nama': 'farid', 'umur': 29}

# coba(a,b)

def vokal(kalimat):
    #voc=['a','i','u','e','o']
    words=kalimat.lower()

    if "a" in words:
        words=words.replace("a", "o")
    if "i" in words:
        words=words.replace("i", "o")
    if "u" in words:
        words=words.replace("u", "o")
    if "e" in words:
        words=words.replace("e", "o")
    
    '''
    for i in range(len(voc)):
        if voc[i] in words:
            words = words.replace(voc[i], "o")
    '''
    print(words) 

#vokal("lintang makan nasi, air mata, kuda")

batas()

def hellow():
    print("Hello World!")

def returnHello():
    return "Hello return world!"

hellow()
print(hellow())
returnHello()
print(returnHello())

