# import csv

# header=['nama', 'usia', 'kota']
# data=[
#     ['Andi', 22, 'Jakarta'],
#     ['Budi', 23, 'Bandung'],
#     ['Caca', 24, 'Bandung']
# ]
# data.insert(0,header)
# print(data)

# file=open('test5.csv', 'w', newline='')
# csv_writer = csv.writer(file)
# csv_writer.writerows(data)

# import numpy
# arr = numpy.random.randint(1,10, size=(3,3))

# print(numpy.random.random((10,2)))
import pandas as pd
import numpy as np

data=np.random.randint(10, size=(5,3))
df=pd.DataFrame(data)
print(df)