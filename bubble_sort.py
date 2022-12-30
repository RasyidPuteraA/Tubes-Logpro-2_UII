def bubble_sort(data):
    # Menentukan panjang data
    n = len(data)

    # Loop sebanyak jumlah elemen data dikurangi satu kali
    for i in range(n-1):
        # Membuat flag untuk menandakan apakah ada elemen yang berpindah posisi atau tidak
        swapped = False

        # Loop untuk membandingkan setiap pasangan elemen data
        for j in range(n-i-1):
            # Menukar posisi elemen jika diperlukan
            if data[j]['Harga'] > data[j+1]['Harga']:
                data[j], data[j+1] = data[j+1], data[j]
                swapped = True
            # Jika Harga sama, maka bandingkan kota
            elif data[j]['Harga'] == data[j+1]['Harga'] and data[j]['City'] > data[j+1]['City']:
                data[j], data[j+1] = data[j+1], data[j]
                swapped = True
        
        # Jika tidak ada elemen yang berpindah posisi, berarti data sudah terurut dengan tepat
        # dan proses sorting dapat dihentikan
        if not swapped:
            break
