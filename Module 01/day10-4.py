import stats as st

ls=[1,2,3,4,5,6,7,8,9,3,4,2,6,7,5,3,5,4,1,2,4,7,7,7,7,7,7,7,7,7,7,7,7,7,7,100,1000]
# print(sorted(ls))
k = st.hitung_stats([1,9,8,2,3,7,4,5,6,10,10])
print(f'average-nya adalah {k.average}')
print(f'median-nya adalah {k.median}')
print(f'modusnya adalah {k.modus}')