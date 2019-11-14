import xlrd
import json
import csv

'''
xlsx => json
xlsx => csv

xlsx => new xlsx
json => xlsx
csv => xlsx
'''

###########################
#convert dari xlsx ke json#
###########################
file_path="Data/data-excel.xlsx"
file=xlrd.open_workbook(file_path)
# print(file)
sheet=file.sheet_by_name("DataKaryawan")
# print(vars(sheet))

# print(sheet.row_values(0))
# sheet.cell_values
arr=[]
for i in range(1,sheet.nrows):
    dictionary={}
    for j in range(len(sheet.row_values(i))):
        dictionary[sheet.row_values(0)[j]]=sheet.row_values(i)[j]
    arr.append(dictionary)

with open('Data/data-json-from-excel.json', 'w') as json_file:
    json.dump(arr,json_file)

###########################
#convert dari xlsx ke csv#
###########################
with open('Data/data-csv-from-excel.csv', 'w', newline='') as csv_file:
    header=sheet.row_values(0)
    k = csv.DictWriter(csv_file, fieldnames=header)
    k.writeheader()
    k.writerows(arr)



###########################
#convert dari json ke xlsx#
###########################
import xlsxwriter

json_file2=open('Data/data-json-from-excel.json', 'r')
output=list(json.load(json_file2))
header=list(output[0].keys())

li=[header]
for i in output:
    li.append(list(i.values()))

file_new_xlsx = xlsxwriter.Workbook('Data/data-excel-from-json.xlsx')
sheet= file_new_xlsx.add_worksheet('Data Karyawan')

for i in range(len(li)):
    for j in range(len(header)):
        sheet.write(i , j, li[i][j])

file_new_xlsx.close()

##########################
#convert dari csv ke xlsx#
##########################

file_new_csv=open('Data/data-csv-from-excel.csv', 'r')
# print(file_new_csv.read())
arr=[]
for i in file_new_csv.readlines():
    arr.append(i.strip('\n').split(','))

file_new_xlsx2 = xlsxwriter.Workbook('Data/data-excel-from-csv.xlsx')
sheet=file_new_xlsx2.add_worksheet("Data Karyawan dua")

for i in range(len(arr)):
    for j in range(len(arr[i])):
        sheet.write(i , j, arr[i][j])

file_new_xlsx2.close()

'''#import xlwt => untuk write excel file versi lama
#import xlsxwriter => untuk write excel file versi baru'''

####
#PR#
####
'''
nambahin input dari user
tambahin nama dan kota
nomor akan increment sendiri
'''

#########################
#input dari user ke xlsx#
#########################
import xlsxwriter
import xlrd

nama=input("masukkan nama: ")
kota=input("masukkan kota: ")
file_path, nama_sheet ='Data/data-excel-add-input-from-user.xlsx', 'DataKaryawan'
file_excel=xlrd.open_workbook(file_path)
open_sheet=file_excel.sheet_by_name(nama_sheet)
data=[open_sheet.row_values(values) for values in range(open_sheet.nrows)]
last_number=data[-1][0]
data.append([last_number+1, nama, kota])

file_excel_write=xlsxwriter.Workbook(file_path)
write_sheet=file_excel_write.add_worksheet(nama_sheet)

for i in range(len(data)):
    for j in range(len(data[i])):
        # print(f"ini i {i}, ini j {j}")
        write_sheet.write(i,j, data[i][j])

file_excel_write.close()