#if statement
#if confition:
#   program()
def batas(kata):
    print("============================")
    print(f"{kata}")
    print("============================")

x = 5
if x == 4:
    print('ini empat')
else:
    print('ini bukan empat')

#equation
print(x == 4)
print(x >= 4)
print(x <= 4)

#comparison
print(x > 4)
print(x < 4)
print(x != 4)

batas("coba nilai")

'''
nilai >= 82 : A
nilai 72-81 : B
nilai 62-71 : C
nilai 52-61 : D
nilai < 52 : E
'''
nilai=62
if nilai >= 85:
    print("nilai anda A")
elif nilai >= 72 and nilai <= 81:
    print("nilai anda B")
elif nilai >=62 and nilai <= 71:
    print("nilai anda C")
elif nilai >=52 and nilai <=61:
    print("nilai anda D")
else:
    print("nilai anda E")