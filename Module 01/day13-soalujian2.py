def segitigaKata(x):
    new_x=x.replace(" ","")
    counter=1
    panjang=len(new_x)
    valid= False
    while panjang != 0:
        if panjang - counter == 0:
            valid=True
            break
        elif panjang - counter > 0:
            panjang=panjang-counter
            counter+=1
        else:
            valid=False
            break

    if valid == True:
        new_kata1=x.replace(" ", '')
        new_kata2=x.replace(" ", '')
        i=0
        while len(new_kata1) != 0:
            kata=''
            i+=1
            # print(f"ini i {i}")
            for j in range(i):
                kata+=new_kata1[j] + ' '
                # print(f"ini j {j}")
            new_kata1=new_kata1[i:]
            # print(new_kata1)
            print(kata)
        # print("")
        # print("")
        while len(new_kata2) != 0:
            kata=''
            # print(f"ini i {i}")
            for k in range(i):
                # print(f"ini k {k}")
                kata+=new_kata2[k] +' '
            print(kata)
            new_kata2=new_kata2[i:]
            # print(new_kata2)
            i-=1
    else:
        print("Mohon maaf, jumlah karakter tidak memenuhi syarat membentuk pola.")


print("# segitigaKata('Purwadhika')")           
segitigaKata('Purwadhika')
# print("")

# print("# segitigaKata('Purwadhika Startup and Coding School @BSD')")           
# segitigaKata('Purwadhika Startup and Coding School @BSD')
# print("")

# print("# segitigaKata('kode')")           
# segitigaKata('kode')
# print("")

# print("# segitigaKata('kode python')")           
# segitigaKata('kode python')
# print("")

# print("# segitigaKata('lintang')")           
# segitigaKata('lintang')
# print("")