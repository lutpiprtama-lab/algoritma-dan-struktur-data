

def hitung_pangkat(a, b):
    """Menghitung a pangkat n dan menampilkan hasil tiap langkah"""
    hasil = 1
    for i in range(1, b + 1):
        hasil *= a
        print(f"hasil {a} pangkat {i} adalah {hasil}")


def hitung_deret(jumlah_n):
    """"
    Pola:
      Pembilang: 1, 2, 5, 13  => p(n) = 3*p(n-1) - p(n-2)
      Penyebut:  1, 3, 8, 21  => q(n) = 3*q(n-1) - q(n-2)
      Tanda: +, -, +, -, ...
    """
    total = 0.0
    p = [1, 2] 
    q = [1, 3] 

    for i in range(jumlah_n):
        if i == 0:
            pembilang, penyebut = 1, 1
        elif i == 1:
            pembilang, penyebut = 2, 3
        else:
            pembilang = 3 * p[1] - p[0]
            penyebut  = 3 * q[1] - q[0]
            p = [p[1], pembilang]
            q = [q[1], penyebut]

        tanda = 1 if i % 2 == 0 else -1
        total += tanda * (pembilang / penyebut)

    return total


def menu():
    while True:
        print("\nmenu pilihan")
        print("1. a pangkat b")
        print("2. hitung deret")
        print("0. keluar")
        pilih = input("Masukkan :").strip()

        if pilih == "1":
            a = int(input("masukan suatu bilangan bulat :"))
            b = int(input("masukan pangkat yang diinginkan : "))
            hitung_pangkat(a, b)

        elif pilih == "2":
            jumlah_n = int(input("Masukkan jumlah N : "))
            hasil = hitung_deret(jumlah_n)
            print(f"{hasil:.7f}")

        elif pilih == "0":
            print("Keluar")
            break

        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    menu()