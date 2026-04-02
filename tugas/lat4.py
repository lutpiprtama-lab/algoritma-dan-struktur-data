x = int(input("Masukkan jumlah hari proyek: "))

tahun = x // 365
sisa_setelah_tahun = x % 365
bulan = sisa_setelah_tahun // 30
hari = sisa_setelah_tahun % 30

print(f"Tahun : {tahun}")
print(f"Bulan : {bulan}")
print(f"Hari  : {hari}")