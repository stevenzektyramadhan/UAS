def tambah(a,b):
    hasil = a + b
    print(hasil)
def kurang(a,b):
    hasil = a - b
    print(hasil)
def pembagian(a,b):
    if b == 0:
        print("pembagian 0 tidak diperbolehkan")
        menu()
    hasil = a/b
    print(hasil)
def perkalian(a,b):
    hasil = a * b
    print(hasil)

def menu():
    user = int(input("Berikut ini Program kalkulator\n1. Penjumlahan\n2. Pengurangan\n3. Pembagian\n4. Perkalian\n\n Masukan pilihan anda:"))
    if user == 1:
        a = int(input("masukan angka pertama: "))
        b = int(input("masukan angka kedua: "))
        tambah(a,b)
    elif user == 2:
        a = int(input("masukan angka pertama: "))
        b = int(input("masukan angka kedua: "))
        kurang(a,b)
    elif user == 3:
        a = int(input("masukan angka pertama: "))
        b = int(input("masukan angka kedua: "))
        pembagian(a,b)
    elif user == 4:
        a = int(input("masukan angka pertama: "))
        b = int(input("masukan angka kedua: "))
        perkalian(a,b)
        
menu()