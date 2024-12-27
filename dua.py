def cetak_pola(baris):
    for i in range(1,baris + 1):
        print("*" * i)
        
        
baris = int(input("Masukan jumlah baris: "))
cetak_pola(baris)