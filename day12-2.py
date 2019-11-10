#JSON = Java Script Object Notation
import json

#membaca json di python
with open('./Data/file2.json', 'r') as x:
    out = json.load(x)

print(type(out))
print(out)
#menulis ke json file dari python
with open('Data/file3.json', 'w') as y:
    json.dump(out, y)

'''cara manual atau pakai package (csv/JSON):
convert
1. csv => json
2. json => csv'''