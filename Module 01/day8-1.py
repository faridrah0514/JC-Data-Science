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



# def prima2(x):

#     prima=filter(lambda a,i: (a % i != 0) and (a > 1),range(x))
#     print(list(prima))

#prima2(angka)
coba=filter(prima, angka)
# coba2=filter(prima2, angka)

print(list(coba))
# print(list(coba2))

# prima2(4)

k=filter(lambda x, y: x > 5 and y > 7, (10,10))
print(list(k))