# #= = = = = = = = = = = = = = = = = = 
# #r = read
# #w = write
# #a = append

# data = open('data.txt')
# # print(data.readable())
# # print(data.read())
# # print(data.readline())
# print(data.readlines())

# # data.write('Code')

# data2 = open('FileBelumAda.txt', 'w')
# data2.write('Test 1 2 3\n')
# data2.write('Makan makan')

# data3 = open('MyVideo.mp4', 'w')
# data3.write('My Video')

# data4 = open('test.py', 'w')
# data4.write(
#     "def test():\
#         \n\tprint(2 + 3)\
#     \ntest()"
# )

# #= = = = = = = = = = = = = = = = = = 

# f = open('data.txt')
# f1 = open('day12-1.py', 'w')

# # k=f.readlines()
# f1.write(f'{f.read()}\n')
# # f1.write(f'\n{k[1]}'')
# # f1.write(f'\n{k[2]}')

# #= = = = = = = = = = = = = = = = = = 

# f = open('data.txt', 'r')
# f1 = open('databaru.txt', 'w')

# for k in f.read().split(', ')[::-1]:
#     f1.write(f'{k}\n')

# # kalo JSON format mesti pake double quote ("")
# #= = = = = = = = = = = = = = = = = = 
# #Mengganti dari CSV ke JSON
'''f = open("Data/file.csv", "r")
k=f.readlines()
header=k[0].strip('\n').split(',')
data=[]

for i in range(1,len(k)):
    data2=k[i].strip('\n').split(',')
    dic={}
    for j in range(0,len(header)):
        dic[header[j]]=data2[j]
    data.append(dic)
print(data)
f.close()'''

# Ganti dari JSON ke CSV

# file = open('Data/file.json', 'r')
# print(file.read())


#package csv
import csv
with open('Data/file.csv', 'r') as x:
    baca = csv.reader(x)
    # print(list(baca))

x=['no', 'nama']
y=[12, 'Andi']

# print(dict(zip(x,y)))

# with open('Data/file.csv', 'r') as y:
#     baca = csv.DictReader(y)
    # for i in baca:
    #     print(i)

#menulis dari tipe data dictionary ke CSV file

data=[
    {'nama': 'Andi', 'Usia': 22, 'Kota': 'Jakarta'},
    {'nama': 'Budi', 'Usia': 21, 'Kota': 'Bandung'},
    {'nama': 'Caca', 'Usia': 23, 'Kota': 'Jogjakarta'}
]

with open('Data/file.csv', 'w', newline='') as x:
    kolom=['nama', 'Usia', 'Kota']
    a = csv.DictWriter(x, fieldnames=kolom, delimiter='+')
    a.writeheader()
    a.writerows(data)


