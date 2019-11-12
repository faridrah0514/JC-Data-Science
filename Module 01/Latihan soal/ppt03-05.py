def segitiga3(x):
    space='   '
    bintang=' * '
    init=1
    maks=x
    for _ in range(x):
        print(space*(maks) + bintang*(init) + space*(maks))
        init+=2
        maks-=1

def segitiga4(x):
    space='   '
    bintang=' * '
    init=1
    seq=list(range(1,100,2))
    li=seq[0:x]
    for _ in range(len(li)):
        maks=li[x-1]
        print(space*(init) + bintang*(maks) + space*(init))
        init+=1
        x-=1
def segitiga5(x):
    segitiga3(x)
    segitiga4(x)

segitiga5(6)