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
    [1,2,3,10,25],
    [4,5,6,11,26],
    [7,8,9,12,27],
    [13,14,15,16,28],
    [17,18,19,20,29],
    [21,22,23,24,30]
    ]

new_li=[]
panjang=len(li)

k=0
for j in range(len(li[k])):
    if k == (panjang - 1):
        break
    else:
        sub_list=[]
        m=panjang
        for i in range(len(li)):
            # print(f"m {m-1}")
            # print(f"j {j}")
            sub_list.append(li[m-1][j])
            m-=1
            # print(f"sub li {sub_list}")
    new_li.append(sub_list) 
    k+=1
    
print(new_li)
              






