import random

def harga(data_maskapai) :  

    for i, maskapai in enumerate(data_maskapai):
        harga_acak = random.uniform(1 * 10**6, 2.2 * 10**6)
        harga_acak = int(str(harga_acak)[:4])
        harga_acak = harga_acak * 1000
        data_maskapai[i]['Harga'] = harga_acak