def Romawi(x):
    simbol_romawi={
        1 : 'I', #pengurangan
        5 : 'V',
        10 : 'X', #pengurangan 
        50 : 'L',
        100: 'C', #pengurangan
        500: 'D',
        1000: 'M'
    }

    romawi=''
    number=[1,5,10,50,100,500,1000]

    for i in range(len(number)):
        if x >= number[i]:
            batas_bawah=number[i]
    
    def kurang10(y):
        ulang=0
        romawi=''
        while y > 0:
            romawi+=str(simbol_romawi[batas_bawah])
            ulang+=1
            y-=batas_bawah
        if ulang > 3:
            romawi=''
            romawi=str(simbol_romawi[batas_bawah]) + str(simbol_romawi[number[number.index(batas_bawah)+1]])
        print(romawi)

    def kurang100(z):
        pass

    if x in simbol_romawi:
        romawi=simbol_romawi[x]
        print(romawi)
    elif x < 10:
        kurang10(x)
    elif x < 100:
        kurang100(x)
    else:
        pass


Romawi(6)