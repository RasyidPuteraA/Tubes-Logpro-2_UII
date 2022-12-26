def position(data, keberangkatan) :  
    # Mencari harga tiket sesuai dengan kota keberangkatan yang dimasukkan
    for i in data:
        if i['City'] == keberangkatan:
            # Jika kota keberangkatan merupakan kota termurah, harga tiket diubah menjadi 0
            if i == data[0]:
                i['Tiket'] = 0
            # Selain itu, harga tiket diubah menjadi harga tiket kota termurah ditambah jarak antar kota
            else:
                for i, item in enumerate(data):
                    if i != 0:
                        #Swapping Tiket
                        temp = item['Tiket']
                        item['Tiket'] = data[0]['Tiket']
                        data[0]['Tiket'] = temp
                        
                        #Swapping Maskapai
                        temp1 = item['Maskapai']
                        item['Maskapai'] = data[0]['Maskapai']
                        data[0]['Maskapai'] = temp1