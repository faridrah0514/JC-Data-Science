angka=list(range(1,101))

#print(angka)
def prima(x):
    Prim=False
    if x == 2:
        Prim=True
    elif x > 1:
        for k in range(2,x):
            if x % k == 0:
                Prim=False
                break
            else:
                Prim=True
    return Prim


coba=filter(prima, angka)
print(list(coba))

'''k=(lambda x,y: x+y)(2,3)
print(k)

nums = range(2, 50) 
for i in range(2, 8): 
    nums = filter(lambda x: x == i or (x % i != 0), nums)

print(list(nums))'''

genap=filter(lambda x: x % 2 == 0, angka)
# print(list(genap))
angka_genap=list(genap)
print(angka_genap)
genap_kali_2=map(lambda x: x*2, angka_genap)
var_genap_kali_2=list(genap_kali_2)

print(var_genap_kali_2)

from functools import reduce
total=reduce(lambda x,y: x+y, var_genap_kali_2)
print(f"jumlah seluruhnya {total}")