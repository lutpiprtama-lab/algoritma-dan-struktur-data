def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# input data
n = int(input("masukan jumlah data: "))
data = []

# input data
for i in range(n):
    angka = int(input(f"Masukan angka ke-{i+1}: "))
    data.append(angka)

print("data sebelum di sorting:", data)

# proses
hasil = selection_sort(data)

print("data setelah di sorting:", hasil)