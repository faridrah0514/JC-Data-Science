'''convert secara manual/dengan package:
csv => json
json => csv'''

#####################
#convert CSV ke JSON#
#####################

#convert CSV ke JSON secara manual
f = open('Data/file4.csv', 'r')
header=f.readline().strip('\n').split(',')
data=[]
for each_line in f.readlines():
    dictionary={}
    data1=each_line.strip('\n').split(',')
    for each_header in range(len(header)):
        dictionary[header[each_header]]=data1[each_header]
    data.append(dictionary)

fjson=open('Data/file4json.json', 'w')
fjson.write(str(data).replace("'", '"'))

f.close()
fjson.close()

#convert CSV ke json dengan package
import csv
import json

f=open('Data/file4.csv', 'r')
fjson2=open('Data/file4json2.json', 'w')
reader=csv.DictReader(f)
reader=str(list(reader)).replace("'",'"')
fjson2.write(reader)
f.close()
fjson2.close()

#convert CSV ke json dengan package => cara kedua
with open('Data/file4.csv', 'r') as data:
    reader=csv.DictReader(data)
    output=list(reader)

with open('Data/file4json3.json', 'w', newline='') as json_file:
    json.dump(output, json_file)


#####################
#convert JSON ke CSV#
#####################
fl=open('Data/file.json', 'r')
output=json.load(fl)
flcsv=open('Data/file2.csv', 'w', newline='')
j=['nama','usia','kota','pekerjaan','gaji']
csv.DictWriter(flcsv,fieldnames=j).writeheader()
csv.DictWriter(flcsv,fieldnames=j).writerows(output)

