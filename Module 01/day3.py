def batas():
    print("======================================================================================")

x=[1,2,3]
for i in x:
    print(f"untuk langkah pertama -> {i}")
y=(1,2,3)

x=[
    (1,['a','b','c'],3),
    (4,5,6)
]

print(x[1][1])

x[0][1][2]="Andi"
x[0][1].append('d')
print(x)
x=tuple(x)
print(x)

batas()
x=[1,2,3]
y=(1,2,3)
#set/himpunan, no indexing
#1. no indexing
#2. unique element
#3. set itu mutable, eleme2nya immutable (set itu bisa masukin tuple (karena immutable), tapi ga bisa masukkin array (karena mutable))

z = {1,2,3,4}
print(z)
print(list(z))
test=[
    {
        "nama": "farid",
        "kelas": [
            "satu", "dua"
        ]
    }
]
print(test)
z.add('a')
print(z)
# for i, j in enumerate(z):
#     print(f"index {i} -> value {j}")
#     #print(j)

#cara akses elemen dari set
# -> ubah jadi list
#   z=list(z); print(z[0])
# -> pake looping
#   for i in z: print(i)
batas()
# z.add(8)
# print(z)
# z.update([10])
# print(z)
# z.discard('a')
# print(z)
z={1,2,3,4,5,6,7,8,9}
z.pop()
z.pop()

#to delete the set -> del z 
print(z)