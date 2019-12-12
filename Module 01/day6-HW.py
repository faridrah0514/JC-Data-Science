def sandimorse(kata):    
    morse={
        "A" : "•–",
        "B" : "–•••",
        "C" : "–•–•",
        "D" : "–••",
        "E" : "•",
        "F" : "••–•",
        "G" : "––•",
        "H" : "••••",
        "I" : "••",
        "J" : "•–––",
        "K" : "–•–",
        "L" : "•–••",
        "M" : "––",
        "N" : "–•",
        "O" : "–––",
        "P" : "•––•",
        "Q" : "––•–",
        "R" : "•–•",
        "S" : "•••",
        "T" : "–",
        "U" : "••–",
        "V" : "•••–",
        "W" : "•––",
        "X" : "–••–",
        "Y" : "–•––",
        "Z" : "––••"
    }
    kata_morse=''
    for i in kata.upper():
        if i in morse:
            kata_morse+=morse[i] + '/'

    return kata_morse

def caesarCipher(kata, parameter):
    alphabet='abcdefghijklmnopqrstuvwxyz'
    kata = kata.split()
    for k in kata:
        cipher=''
        Capital = False
        for i in k:
            #cek kapital atau bukan
            if i == i.upper():
                Capital = True
                i=i.lower()
            else:
                Capital=False

            #index
            if alphabet.index(i) + parameter > 25:
                idx = ((alphabet.index(i) + parameter) % 26)
                #idx = (alphabet.index(i) + parameter) - 26
            else:
                idx = alphabet.index(i) + parameter

            #geser
            if Capital:
                cipher+=alphabet[idx].upper()
            else:
                cipher+=alphabet[idx]
                
        kata[kata.index(k)] = cipher

    return ' '.join(kata)



print(sandimorse("lintang"))
print(caesarCipher("Lintang Guru Python ku",200))
# caesarCipher()

def fungsi(x: str) -> bool:
    return x+1

print(fungsi(10))

print((lambda x,y : x+y)(2,3))

