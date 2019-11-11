'''problem description:
1. Fibonanci
    class Fibo:
        ....

    Fibo=Fibo()

2. x = 'AbcdEFgHi'
    return function => x = 'aBCDefHhI'

3. function cek sudut antara 2 sisi
    sisi A = 8cm, sisi B = 10cm, sudut AB = ?

4. [                        [
    [1,2,3],                    [7,4,1],
    [4,5,6],    def =>          [8,5,2],
    [7,8,9]                     [9,6,3]
]                           ]

5.
'''
##############
#soal nomor 1#
##############

class Fibo:
    def cek(self, x):
        #fibo = [0,1,1,2,3,5,8,13 ... ]
        if x == 0:
            return 0
        elif x == 1:
            return 1
        else:
            return self.cek(x-1) + self.cek(x-2)

Fibo = Fibo()
print(Fibo.cek(6))

##############
#soal nomor 2#
##############
x = 'AbcdEFgHi'
def rev(x):
    y=''
    for i in x:
        if i == i.upper():
            y+=i.lower()
        else:
            y+=i.upper()
    return y

print(rev(x))

##############
#soal nomor 3#
##############

##############
#soal nomor 4#
##############

li=[
    [1,2,3,10],
    [4,5,6,11],
    [7,8,9,12],
    [13,14,15,16]
    ]
new_li=[]
for i in range(len(li)):
    j=len(li[i])
    sub_li=[]
    while j > 0:
        sub_li.append(li[j-1][i])
        j-=1
    new_li.append(sub_li)
print(new_li)
# print(li)                  






