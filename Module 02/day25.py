import numpy as np
import pandas as pd

# x=[1,2,3,4,5]
# y=[6,7,8,9,10]

# z=list(map(lambda a,b: [a,b], x,y))
# npy=np.array(x)
# npx=np.array(y)
# npz = np.vstack((npx,npy))

# pdf=pd.DataFrame(npz)
# spd=pd.Series()
# print(pdf)
# print(list(zip(x,y)))
# fr="Farid"
# print(list(fr))

# df=pd.DataFrame({
#     "A": np.arange(20,26),
#     "B": [10,11,12,13,14,15],
#     "C": np.random.randint(10, size=6),
#     'D': np.ones(6)
# })
# print(df)
# print(df.describe())

df=pd.DataFrame({
    "Aa": np.arange(20,26),
    "Bb": [10,11,12,13,14,15],
    "Cc": np.random.randint(10, size=6),
    # "Fg": df["Cc"]/100,
    'GG': np.random.rand(6),
    'Dd': np.ones(6)
})
print(df["Cc"])
df['Kk']=df['Cc']/100
print(df)
# df.sort_values(by='Cc', ascending=True, inplace=True)
print("=====")
print(df.loc[1:3,'Aa'])
df.loc[1:3,'Aa'] = np.nan
# df.set_index('Aa', inplace=True)
print(df.index)
df.index='a b c d e f'.split()
# df.values[0][0]=14051990
# print(df.values[0][0])
# print(df)
# print(df.isnull())
print(df)
for i in df:
    print(i)


#create dataframe dari:
#csv, excel, json, tanpa pd.read_XXX

#create dataframe dari:
# dari database db.mysql
# dari database db.mongodb
# tanpa pd.read_sql