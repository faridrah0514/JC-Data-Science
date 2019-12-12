s = {x for x in range(0,10)}
a = {2,3,5,7}
b = {5,7,9}
#print(s)
#a
print(f"soal a : {a}")

#b
print(f"soal b : {b}")

#c
print(f"soal c : {(a & b)}")

#d
print(f"soal d : {(a | b)}")

#e
print(f"soal e : {a & (a | b)}")

#f
print(f"soal f : {b & (a | b)}")

#g
print(f"soal g : {(a | b) & (a | b)}")

#h
print(f"soal h : {(a & b) | (a | b)}")