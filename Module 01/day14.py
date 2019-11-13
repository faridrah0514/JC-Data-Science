import xlrd
# import numpy as np
#cara install xlrd
#pip install xlrd
#py -m pip install xlrd
#conda install xlrd
#pip3 install xlrd
file = xlrd.open_workbook('Data/data-excel.xlsx')
print(vars(file))
sheet_names = file.sheet_names() # munculin list sheet di excel file
print(file.sheet_names())
# sheet=file.sheet_by_index(0)
sheet2=file.sheet_by_name("DataKaryawan")



print(sheet2.nrows, sheet2.ncols) # jumlah rows and column
# print(sheet2.cell_value(0,0)) # print cell valur di kol 1 row 0
# print(sheet2.cell_value(0,1))
# print(sheet2.cell_value(0,2))

# for i in range(sheet2.ncols):
#     print(sheet2.cell_value(0,i))
#     print(sheet2.cell_value(1,i))
#     print(sheet2.cell_value(2,i))

for i in range(sheet2.nrows):
    print(sheet2.row_values(i)) #untuk menampilkan value sepanjang row
    # print(sheet2.col_values(i))

'''
xlsx => json
xlsx => csv

json => xlsx
csv => xlsx
'''

#untuk menulis ke xlsx file
import xlsxwriter

file = xlsxwriter.Workbook('Data/test123.xlsx')

sheet = file.add_worksheet('DataKaryawan')

sheet.write(0, 0, 'Nama') #row, col, data
sheet.write(0, 1, 'Kota')
sheet.write(0, 2, 'Job')
sheet.write(1, 0, 'budi') #row, col, data
sheet.write(1, 1, 'jakarta')
sheet.write(1, 2, 'pengangguran')



file.close()

