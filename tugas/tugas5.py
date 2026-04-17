# Input matriks 2x2
def input_matriks(nama):
    print(f"Masukkan matriks {nama}:")
    matriks = []
    for i in range(2):
        baris = list(map(int, input(f"Baris {i+1}: ").split()))
        matriks.append(baris)
    return matriks


def tampilkan(m):
    for row in m:
        print(row)


while True:
    print("\n=== MENU ===")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("0. Exit")

    pilihan = int(input("Pilih: "))

    if pilihan == 0:
        print("Program selesai")
        break

    A = input_matriks("A")
    B = input_matriks("B")

    hasil = [[0, 0], [0, 0]]

    if pilihan == 1:  # Penjumlahan
        for i in range(2):
            for j in range(2):
                hasil[i][j] = A[i][j] + B[i][j]

    elif pilihan == 2:  # Pengurangan
        for i in range(2):
            for j in range(2):
                hasil[i][j] = A[i][j] - B[i][j]

    elif pilihan == 3:  # Perkalian
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    hasil[i][j] += A[i][k] * B[k][j]

    else:
        print("Pilihan tidak valid")
        continue

    print("Hasil:")
    tampilkan(hasil)