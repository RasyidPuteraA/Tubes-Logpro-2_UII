def position(data, keberangkatan) :  
    # Mencari harga tiket sesuai dengan kota keberangkatan yang dimasukkan
    for i in data:
        if i['City'] == keberangkatan:
            #Swapping Tiket
            temp = i['Tiket']
            i['Tiket'] = data[0]['Tiket']
            data[0]['Tiket'] = temp
                        
            #Swapping Maskapai
            temp1 = i['Maskapai']
            i['Maskapai'] = data[0]['Maskapai']
            data[0]['Maskapai'] = temp1