def segitiga3(x):
    space='   '
    bintang=' * '
    init=1
    maks=x
    for _ in range(x):
        print(space*(maks) + bintang*(init) + space*(maks))
        init+=2
        maks-=1

segitiga3(5)