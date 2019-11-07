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



def prima2(x):
    for i in range(2,x):
        prima=filter(lambda x: x==i or x%i,angka)
    print(list(prima))

prima2(5)
# coba=filter(prima2, angka)
# print(list(coba))