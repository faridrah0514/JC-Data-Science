def rata_rata(data):
    banyak_data=len(data)
    jumlah_data=sum(data)
    nilai_rata_rata = float(jumlah_data)/float(banyak_data)
    return nilai_rata_rata

if __name__ == '__main__':
    k=[2,3,4,5,6,7,7,8,9,1,2,3,5]
    rata = rata_rata(k)
    print(f"nilai rata-rata adalah : {rata}")

