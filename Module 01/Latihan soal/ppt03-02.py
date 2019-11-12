def segitiga2(x):
    maks=x
    for _ in range(x):
        print("* "*maks)
        maks-=1
    for _ in range(1,x):
        maks+=1
        print("* "*(maks+1))
        

segitiga2(6)