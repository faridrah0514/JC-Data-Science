#belajar numpy
import numpy as np

x =[1,2,3]
x=np.array(x)
y=[
    [1,2,3],
    [4,5,6]
]
y=np.array(y)

#array 3d
z=[[
        [1,2,3,10],
        [4,5,6,11],
        [7,8,9,12]
    ]]
z=np.array(z)
print(x)
print(y)
print(z)
#cek dimensi
print("dimensi")
print(x.ndim, y.ndim, z.ndim)
#cek size
print("size")
# print(x.size, y.size, z.size)
print("x", x.size, "y", y.size, "z", z.size)

#merubah tipe data
z = z.astype('float')
print(z)
print(z.dtype)
#ukuran matrix
print("x:", x.shape, " y:", y.shape, " z:", z.shape)

a=np.arange(1,10)
print(a)
a=a.reshape(3,3)
print(list(range(1,10,2)))

print(a + 2)

#create random array
print(np.random.random(10))
print(np.random.rand(2,4))
print(np.random.randint(7, size=(2,5)))

#persamaan tiga dimensi asal-asalan

persamaan=[[2,1,4],
          [1,1,10],
          [3,4,5]]
# hasil=[5,7,9] # satu dimensi
hasil=[[5],[7],[9]] #dua dimensi juga bisa
persamaan=np.array(persamaan)
hasil=np.array(hasil)
# print(persamaan.shape)
# print(hasil.shape)
hasil2=np.linalg.solve(persamaan,hasil)
print(hasil2)



matrix=np.array([[2,1,1],
                [1,2,1],
                 [3,2,1]])
hasil=np.array([4700,4300,7100])
solve=np.linalg.solve(matrix,hasil)

print(solve)
print(f'''buku: {int(round(solve[0]))}
pensil: {int(round(solve[1]))}
penghapus: {int(solve[2])}''')
# print(int(round(solve[0])))
# print(int(round(solve[1])))
# print(int(round(solve[2])))