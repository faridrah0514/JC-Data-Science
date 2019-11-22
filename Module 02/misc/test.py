print("Hello!")

import numpy as np
import pandas as pd
arr=np.arange(0,11)

# print(arr)
# print(arr + arr)
# print(arr*3)
# print((arr*4) - 2)

# print(np.sqrt(arr))
# arr

# my_list=[1,2,3]
# print(np.array(my_list))
# my_matrix=[
#     [1,2,3],
#     [4,100,6],
#     [7,8,88]
# ]
# print(my_matrix)
# np_matrix=np.array(my_matrix)
# print(np_matrix[0])

# # arr2=np.full((3,3), True, dtype=bool)
# arr2=np.full((10,10), 20,dtype=int)
# print(arr2)


# new_arr=np.array([
#     [1,2,3,4,5],
#     [6,7,8,9,10]
# ])
# np_new=new_arr.reshape(5,2)
# print(new_arr)
# print(np_new)

# print(np.mean(np_matrix))
# print(np.median(np_matrix))
# print(np.sum(np_matrix))
# print(np.max(np_matrix))
# print(np.min(np_matrix))
# print(
#     "shape"
# )
# print(np.shape(np_matrix))


# # print(np.random.rand(5,5))

# list_arr=[
#     [11,2,3],
#     [4,52,6],
#     [7,8,93]
# ]

# np_arr=np.array(list_arr)
# np_arr[0][0] = 212
# np_arr2=np_arr[1:5]
# print(np_arr)

# np_arr2=np.ravel(np_arr2)
# print(np_arr2)
# np_arr2=np_arr2.reshape(3,2)
# # np_arr2=100
# print(np_arr2)

# arr_2d=np.arange(150).reshape(50,3)
# # arr_2d=arr_2d.reshape(15,10)
# print(arr_2d)
# # print(arr_2d[:2,1:])
# # print(arr_2d[:2][1:])
# # print(arr_2d[2,:])

# # for i in arr_2d:
# #     print(i)

# print(arr_2d[arr_2d > 50])

# a=['nama','usia','kota']
# b=['andi', 22, 'jakarta']
# print(list(zip(a,b)))

labels=['a','b','c','d','e']
my_list=[10,11,12,13,14]
arr=np.array(my_list)
d=dict(zip(labels,my_list))
print(d)
print(pd.Series(data=my_list,index=['satu','dua','tiga','empat','lima']))

print(np.arange(20).reshape(5,4))

df=pd.DataFrame(np.arange(20).reshape(5,4), index=['A', 'B', 'C', 'D', 'E'], columns=['SATU', 'DUA', 'TIGA', 'EMPAT'])
print(df)
print("============")
print(df[['TIGA','EMPAT']])
df['LIMA']=[23,24,25,27,29]

print(df)