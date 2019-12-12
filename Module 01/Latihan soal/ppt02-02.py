massa=float(input("Masukkan Massa(kg) : "))
tinggi=float(input("Masukkan Tinggi(cm) : "))
print(f"Massa {massa} kg & tinggi {(tinggi)/100} m")
imt=massa/((tinggi/100)**2)
if imt < 18.5:
    print(f"IMT = {imt}, BERAT BADAN KURANG!")
elif imt >= 18.5 and imt <= 24.9:
    print(f"IMT = {imt}, BERAT BADAN IDEAL!")
elif imt >= 25 and imt <= 29.9:
    print(f"IMT = {imt}, BERAT BADAN BERLEBIH!")
elif imt >= 30 and imt <= 39.9:
    print(f"IMT = {imt}, BERAT BADAN SANGAT BERLEBIH!")
else:
    print(f"IMT = {imt}, OBESITAS!")

# print(f"IMT = {imt}")