
def batas():
    print("===============================================================")
#berbagai operasi menggunakan SET
a=list('abcde')
b=list('bcfgh')

# find the intersection for a and b
a=set(a)
b=set(b)
print("INTERSECTION")
print(a.intersection(b))
print(b.intersection(a))
print(a & b)
print(b & a)

#find the union
print("UNION")
print(a.union(b))
print(b.union(a))
print(a | b)
print(b | a)

#Selisih, difference
print("DIFFERENCE")
print(a.difference(b))
print(b.difference(a))
print(a - b)
print(b - a)

#symmetric difference
print("SYMMETRYC DIFFERENCE")
print(a.symmetric_difference(b))
print(b.symmetric_difference(a))
print(a ^ b)
print(b ^ a)

batas()
P={1,2,4,7,9,19}
Q={5,12,16,17,7,8,19,6,9}
R={3,8,19,6}

#intersection P & Q
print(P & Q)
print(P.intersection(Q))
print(P.intersection(Q.intersection(R)))
print(P & Q & R)

batas()

# S={-9, -8, -7, -6, -5, -4, -3, -2, -1, 0,1,2,3,4,5,6,7,8,9}
S={x for x in range(-9,9)}
P={x for x in range(-4,4)}
Q={x for x in range(-7,1)}
R={x for x in range(-1,7)}
# P={-4, -3, -2, -1, 0,1,2,3,4}
# Q={-7, -6, -5, -4, -3, -2, -1, 0,1}
# R={-2, -1, 0,1,2,3,4,5,6,7}

# H={x for x in range(-10,10)}
# print(f"ini H {H}")

print(list(P|Q).sort())
print(P|R)
print(Q|R)