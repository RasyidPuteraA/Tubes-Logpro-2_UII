def rekomendasi(keberangkatan,tujuan,data_maskapai,jarak) : 
        for item in data_maskapai:
            if item['Harga'] == data_maskapai[0]['Harga']:
                print(f'\nMaka sistem merekomendasikan jika pengguna melakukan keberangkatan dari Kota {keberangkatan} ke Kota {tujuan} \n')
                print(f'\nJarak antara Kota : {jarak}KM')
                print(f'Dengan Harga tiket : Rp {item["Harga"]}\n\n')
                # Menggunakan return statement untuk kembali mengembalikan harga tiket
                return item['Harga']
       