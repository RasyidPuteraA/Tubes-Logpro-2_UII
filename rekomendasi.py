def rekomendasi(city, data) : 
        for item in data:
            if item['City'] == city:
            
                print(f'Maka sistem merekomendasikan jika pengguna melakukan keberangkatan dari {city}\n')
                print(f'Harga tiket untuk keberangkatan dari {city}: Rp {item["Tiket"]}\n\n')
                # Menggunakan return statement untuk kembali mengembalikan harga tiket
                return item['Tiket']
       