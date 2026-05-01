def seq_search_boolean(array, x):
    i = 0
    ketemu = False
    n = len(array)

    while (i < n) and (not ketemu):
        if array [i] == x:
            ketemu = True
        else:
            i += 1
    return ketemu

def seq_search (L, n, x):
    i=0

    while i < n :
        if L[i] == x:
            return i
        i += 1

    return -1

data = [81, 76, 21, 18, 16, 13, 10, 7]
cari = int(input("masukan angka yang dicari : "))

hasil = seq_search(data, len(data), cari)

if hasil != -1:
    print("data ditemukan di index ke-", hasil)
else:
    print("data tidak ditemukan")