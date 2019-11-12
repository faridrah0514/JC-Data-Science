A={2,4,6,8,10,12,14,16,18,20} #bilangan genap antara 1 dan 20
B={1,3,5,7,9,11,13,15,17,19} #bilangan ganjil antara 1 dan 20
C={-9,-8,-7,-6,-5,-4,-3,-2,-1} #bilangan negatif lebih dari -10
D={2,3,5,7,11,13,17,19} #bilangan prima antara 1 dan 20
E={4,6,8,9,10,12,14,15,16,18,20} #bilangan komposit antara 1 dan 20

# print(type(A))
#soal A
print(A | B | C | D | E )

#soal B
print(((A & B) | (D & E)))

#soal C
print((A | B) & (D | E))

#soal D
print((A | B) - (D | E))

#soal E
print((A | B | C) - (A & E))