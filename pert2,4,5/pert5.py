nim={
    "10121001" : "asep",
    "10121002" : "budi",
    "10121003" : "cecep",
}
nilai{
    "10121001" : [50,70,40,80],
    "10121002" : [78,78,80,65],
    "10121003" : [57,88,67,69]
}

mata_kuliah=["mk1",",mk2","mk3","mk4"]

rata_mahasiswa = {}

for nim,daftar_nilai in nilai.items():
    rata= sum(daftar_nilai)/len(daftar_nilai)
    rata_mahasiswa[nim]=rata

    nim_terpintar = max (rata_mahasiswa, key=rata_mahasiswa.get)

    rata_mk=[]

    for i range(len(mata_kuliah)) :
        total = 0
        for nim in nilai:
            total += nilai[nim][i]
        rata = total / len(nilai)
        rata_mk.append(rata)
    
    index_mk_terkecil = rata_mk.index(min(rata_mk))
