Namakaryawan = str (input(("masukan nama karyawan : ")))
Gajipokok = float (input(("masukan gaji pokok : ")))

persentunjangan = 0.2
persenpajak = 0.15

tunjangan = persentunjangan * Gajipokok
pajak = persenpajak * (Gajipokok+tunjangan)
gajibersih = Gajipokok + tunjangan - pajak

print("nama karyawan : ", Namakaryawan)
print("gaji bersih : ", gajibersih)