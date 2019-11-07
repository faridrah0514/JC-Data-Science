#if statement
#function
#while loop

# i = 0
# while i < 10:
#     print(i)
#     i+=1


def batas():
    print("--------------------------------------")
batas()

# stu=['a','b','c']
# while k in range(len(stu)):
#     print(k)
x=[1,2,3,4,5,6,7,8,9,10]
y=[]
i=0
while i <= len(x) - 1:
    y.append(x[i]**2)
    i +=1
print(y)
batas()



#aplikasi break dan continue

i=1
while i < 10:
    print(i)
    if i == 5:
        break
    i +=1

batas()
i=0
while i < 10:
    i += 1
    if i == 5:
        continue
    print(i)

password='12345'
i=0
while i <= 4:
    passwd=input(f"Input ke-{i+1}, Ketik password: ")
    if passwd == password:
        print("password benar!")
        break
    # else:
    #     print("Kesempatan habis, tunggu 24 jam")
    i +=1

#print(i)
if i == 5:
    print("Kesempatan habis, tunggu 24 jam")


# x=[40,100,1,5,25,10]

# #sorting
# for i in range(len(x)):
#     for j in range(len(x)):
#         k=0
#         if x[i] < x[j]:
#             k=x[i]
#             x[i] = x[j]
#             x[j] = k
# print(x)

# #max value
# x=[40,100,1,5,25,10,111]
# k=0
# for i in range(len(x)):
#     if k < x[i]:
#         k=x[i]

# print(k)
