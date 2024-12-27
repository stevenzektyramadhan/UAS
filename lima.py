def kategori_usia(usia):
    if usia < 0:
        return "Usia tidak valid"
    elif usia <= 5:
        return "Balita"
    elif usia <= 12:
        return "Anak-anak"
    elif usia <= 17:
        return "Remaja"
    elif usia <= 59:
        return "Dewasa"
    else:
        return "Lansia"



usia_pengguna = int(input("Masukkan usia Anda: "))
kategori = kategori_usia(usia_pengguna)
print(f"Kategori usia Anda: {kategori}")
