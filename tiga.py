def hitung_gaji(tarif_per_jam, jam_kerja_per_hari, hari_kerja):
    jam_normal = 8
    tarif_lembur = 1.5 * tarif_per_jam
    total_gaji = 0

    for hari in range(1, hari_kerja + 1):
        jam_kerja = jam_kerja_per_hari[hari - 1]
        if jam_kerja > jam_normal:
            lembur = jam_kerja - jam_normal
            total_gaji += (jam_normal * tarif_per_jam) + (lembur * tarif_lembur)
        else:
            total_gaji += jam_kerja * tarif_per_jam

    return total_gaji


try:
    tarif_per_jam = float(input("Masukkan tarif gaji per jam: "))
    hari_kerja = int(input("Masukkan jumlah hari kerja dalam sebulan: "))

    jam_kerja_per_hari = []
    for i in range(hari_kerja):
        jam_kerja = float(input(f"Masukkan jam kerja untuk hari ke-{i + 1}: "))
        jam_kerja_per_hari.append(jam_kerja)

    
    total_gaji = hitung_gaji(tarif_per_jam, jam_kerja_per_hari, hari_kerja)
    print(f"\nTotal gaji bulanan Anda adalah: Rp{total_gaji:.2f}")
except ValueError:
    print("Input tidak valid. Harap masukkan angka yang benar.")
