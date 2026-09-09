def bubble_sort_desc(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# input jumlah data
n = int(input("masukan jumlah data: "))
data = []

# input satu persatu
for i in range(n):
    angka = int(input(f"masukan angka ke-{i+1}:"))
    data.append(angka)

print("data sebelum di sorting:", data)

# proses descending
hasil = bubble_sort_desc(data)

print("data setelah di sorting:", hasil)