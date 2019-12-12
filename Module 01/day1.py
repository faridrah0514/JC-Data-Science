
print(round(3.654231))
print(round(3.1231, 2))
print("==============")
print (0.1 + 0.3)

import math

print(math.pi)
print(math.floor(3.999999))
print(math.ceil(3.999999))
print(math.sqrt(196))
print(math.factorial(3))
print("=============")
#makan

# x="kambing" 
# y="ayam"

# x + y = 13
# 4x + 2y = 32 | 2x + 13 - x = 16
kaki1=4
kaki2=4
hewan1=0
hewan2=0


jumlah_kaki=32
jumlah_ekor=13
jmlAyam=(jumlah_kaki/2)-jumlah_ekor
print("jumlah ayam {}".format(int(jmlAyam)))
print("jumlah kambing {}".format(int(jumlah_ekor - jmlAyam)))


print("=============")
jumlah_usia=49
rasio=0.4
umur_andi = jumlah_usia/(rasio + 1)
umur_budi = jumlah_usia - umur_andi
print(f"umur andi {umur_andi} umur budi {umur_budi}")
print(f"umur andi dua tahun lagi {umur_andi + 2} umur budi dua tahun lagi {umur_budi + 2}")
print("=============")



total_hewan=int(input("Masukkan Total Hewan: "))
total_kaki=int(input("Masukkan Total Kaki Hewan: "))
kaki_hewan1=int(input("Masukkan jumlah kaki hewan pertama: "))
kaki_hewan2=int(input("Masukkan jumlah kaki hewan kedua: "))
hewan1=abs((total_kaki/kaki_hewan1)-total_hewan)
hewan2=total_hewan - hewan1
print(f"Hewan pertama = {hewan1}, hewan kedua= {hewan2}")





