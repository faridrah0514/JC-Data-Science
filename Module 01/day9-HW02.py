def Romawi(x):
    simbol_romawi={
        1 : 'I', #pengurangan
        4 : 'IV',
        5 : 'V',
        9 : 'IX',
        10 : 'X',
        40 : 'XL', #pengurangan 
        50 : 'L',
        90: 'XC',
        100: 'C', #pengurangan
        500: 'D',
        1000: 'M'
    }

    number=list(simbol_romawi.keys())
    komponen=[]
    komponen_romawi=[]

    for i in range(len(number)):
        if x >= number[i]:
            batas_bawah=number[i]

    while x != 0:
        if x - batas_bawah < 0:
            batas_bawah=number[number.index(batas_bawah)-1]
            #print(batas_bawah)
        else:
            x-=batas_bawah
            komponen.append(batas_bawah)
    for i in range(len(komponen)):
        komponen_romawi.append(simbol_romawi[komponen[i]])
    #komponen_romawi_new=set(komponen_romawi)
    rom=''.join(komponen_romawi)
    #simbol_romawi_key=list(simbol_romawi.keys())
    #simbol_romawi_value=list(simbol_romawi.values())
    #simbol_romawi_list=[simbol_romawi_key, simbol_romawi_value]
    #print(simbol_romawi_list)
    # for i in komponen_romawi_new:
    #     replacement=''
    #     if rom.count(i) > 3:
    #         replacement=simbol_romawi_value[simbol_romawi_value.index(i)] + simbol_romawi_value[simbol_romawi_value.index(i)+1]
    #         print(f"replacement {replacement}")
    #         print(i*3)
    #         rom.replace(i*3,replacement)
    print(komponen)
    print(rom)


Romawi(99)