data = [81,76,21,18,16,13,10,7]

cari = int(input("masukan angka yang dicari : "))

awal = 0
akhir = len(data) -1
ketemu = False

while awal <= akhir:
    tengah = (awal + akhir) //2

    if data[tengah] == cari:
        print("data ditemukan di index ke-", tengah)
        ketemu = True
        break
    elif data[tengah] > cari :
        awal = tengah + 1
    else:
        akhir = tengah - 1

if not ketemu : 
    print("data tidak ditemukan")