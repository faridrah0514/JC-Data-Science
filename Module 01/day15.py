
'''
import xlsxwriter

file=xlsxwriter.Workbook('Data/z.xlsx')
sheet=file.add_worksheet('Data')

# sheet.write(0,0,1)
# sheet.write(0,1,"=A1 + 200")
# sheet.write(0,2,"=SUM(A1:B1)")
for i in range(10):
    sheet.write(i,0,i)

file.close()

import xlrd
file2=xlrd.open_workbook('Data/z.xlsx')
sheet2=file2.sheet_by_name('Data')
for i in range(sheet2.nrows):
    print(sheet2.cell_value(i,0))

'''




