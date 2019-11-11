nama2='Purwadhika Startup & Coding School & startup 1234567 ccccccc'
#jumlah huruf 'c' ?
# print("jumlah huruf c")
huruf="c"
x=nama2.lower().replace(huruf.lower(),"")
jml_huruf = len(nama2) - len(x)
print(f"jumlah huruf {huruf} ada {jml_huruf}")

#jumlah kata 'startup'?
kata="startup"
y=nama2.lower().replace(kata.lower(), "")
jml_kata=(len(nama2) - len(y))/len(kata)
print(f"jumlah kata startup ada {int(jml_kata)}")
