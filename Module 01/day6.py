#for loop
'''
    for condition:
        program
'''

kota = ['jakarta', 'bandung', 'surabaya']
coba = [(1,2),(3,4)]

'''for i in kota:
    print(i)

for k, l in coba:
    print(k)
    print(l)'''

for m in range(2,10,3):
    print(m)
else:
    print("OK")


#break
for i in range(2,10):
    print(i)
    if i == 7:
        break

#continue
for i in range(2,10):
    if i ==7:
        continue
    print(i)

space=' '
star='*'
print("----------------")
for i in range(1,11):
    if i % 2 == 0:
        print("wow")
    else:
        print(i)

#data=[(x,y) for x,y in (range(1,))]
print("----------------")
'''print(range(1,10))
print(list(range(10,1)))'''
#fizzbuzz
'''for i in range(1,16):
    if i / 3 = :
''' 
'''def fizzbuzz(number):
    for i in range(1,number + 1):
        if i % 5 == 0:
            if i % 3 == 0:
                print("fizzbuzz")
            else:
                print("buzz")
        elif i % 3 == 0:
            if i % 5 == 0:
                print("fizzbuzz")
            else:
                print("fizz")
        else:
            print(i)'''

def fizzbuzz(number):
    for i in range(1,number+1):
        if i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz")
        elif i % 5 == 0:
            print("buzz")
        elif i % 3 == 0:
            print("fizz")
        else:
            print(i)

fizzbuzz(30)

'''i = 1
j = 6
while i <= 5:
    print(f"{space*int(j/2)}{star*i}{space*int(j/2)}")
    i+=1
    j-=1'''

'''
    1. reverse
        x.reverse()
        print(x)
    2. print(x[::]-1)
    3. reversed
        print(list(reversed(x)))
'''
#reverse
def balik(x):
    y =[]
    for i in range(1,len(x)+1):
        # if i == 0:
        #     continue
        y.append(x[-i])
    print(y)

li=['andi', 'budi', 'caca']
li2=[1,2,3,4,5,6,7]
balik(li)
balik(li2)

# kata="lintang makan nasi" 
#ganti konsonan dengan
def ganti(kata):
    vocal=['a','i','u','e']
    kata2=""
    for i in kata:
        if i in vocal:
            kata2+='o'
        else:
            kata2+=i
    print(kata2)

ganti("lintang makan nasi kocar kocak")

def palindrome(x):
    y =''
    for i in range(1,len(x)+1):
        y+=x[-i]
    if x == y:
        return True
    else:
        return False


print(palindrome("katak"))

kalimat = 'Hai aku Lintang anak mama'
def balikbalik(kata):
    kata = kata.split()
    kata2=''
    for i in kata:
        kata2 += i[::-1] + ' '
    return kata2

print(balikbalik(kalimat))


# A •–
# B –•• •
# C – • – •
# D – • •
# E •
# F • • – •
# G – – •
# H • • • •
# I • •
# J • – – –
# K – • –
# L • – • •
# M – –
# N – •
# O – – –
# P • – – •
# Q – – • –
# R • – •
# S • • •
# T –
# U • • –
# V • • • –
# W • – –
# X – • • –
# Y – • – –
# Z – – • •


A ="• –"

print(A)