def quick_sort (data):

    index = len(data)

    if index <= 1:
        return  data
    else:
        pivot = data.pop()


    data_kiri = []
    data_kanan = []

    for i in data:
        if i < pivot:
            data_kiri.append(i)
        else:
            data_kanan.append(i)

    return quick_sort(data_kiri) + [pivot] + quick_sort(data_kanan)

data = [11, 7, 13, 4, 9, 2, 8]
print ("data acak : ", data)

hasil = quick_sort(data)
print("setelah sorting : ", hasil)