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
            if data[j]['Total Biaya'] > data[j+1]['Total Biaya']:
                data[j], data[j+1] = data[j+1], data[j]
                swapped = True
            # Jika total biaya sama, maka bandingkan kota
            elif data[j]['Total Biaya'] == data[j+1]['Total Biaya'] and data[j]['City'] > data[j+1]['City']:
                data[j], data[j+1] = data[j+1], data[j]
                swapped = True
        
        # Jika tidak ada elemen yang berpindah posisi, berarti data sudah terurut dengan tepat
        # dan proses sorting dapat dihentikan
        if not swapped:
            break

# Contoh penggunaan
data = [
    {'Place_Name': 'Pulau Pelangi', 'City': 'Jakarta', 'Price': 900000, 'Tiket': 0, 'Total Biaya': 900000, 'Maskapai': 'None'},
    {'Place_Name': 'Monumen Batik Yogyakarta', 'City': 'Yogyakarta', 'Price': 40000, 'Tiket': 1200000, 'Total Biaya': 1240000, 'Maskapai': 'Garuda'},
    {'Place_Name': 'Trans Studio Bandung', 'City': 'Bandung', 'Price': 280000, 'Tiket': 1800000, 'Total Biaya': 2080000, 'Maskapai': 'Lion Air'},
    {'Place_Name': 'Ciputra Waterpark', 'City': 'Surabaya', 'Price': 95000, 'Tiket': 1200000, 'Total Biaya': 1295000, 'Maskapai': 'Lion Air'},
    {'Place_Name': 'Safari & Marine Park', 'City': 'Bali', 'Price': 600000, 'Tiket': 1800000, 'Total Biaya': 2400000, 'Maskapai': 'Garuda'}
]

bubble_sort(data)

print([item['City'] for item in data])
