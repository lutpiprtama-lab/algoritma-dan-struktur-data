import

data_mahasiswa = []

def pilih():
    print("Tambah Mahasiswa")
    print("Tampilkan Data Mahasiswa")
    print("Searching Mahasiswa")
    print("Hapus Data Mahasiswa")
    print("Urutan Mahasiswa")
    print("keluar")
    pilihan = int(input("Masukan Nilai Pilihan : "))
    return pilihan

def tambah_data():
    nama = input("Masukan Nama Mahasiswa : ")
    nim = input("Masukakn Nim Mahasiswa : ")
    ipk = int(input("Masukan Nilai IPK"))
    mahasiswa = ('nama' = Nama 'nim' = Nim 'ipk' = Ipk)
    data_mahasiswa.append(data_mahasiswa)
    print("data berhasil ditemukan", data_mahasiswa)

def menampilkan_data(sumber_data = None) :
    list_data = sumber_data if sumber_data is not None else data_mahasiswa
    if not list_data :
        print("data kosong")
        return
    else :
        print("data : ", data_mahasiswa)