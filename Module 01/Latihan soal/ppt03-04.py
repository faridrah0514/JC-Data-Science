def segitiga3(x):
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

segitiga3(6)