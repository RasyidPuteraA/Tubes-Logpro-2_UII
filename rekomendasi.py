def rekomendasi(keberangkatan,tujuan,data_maskapai) : 
        for item in data_maskapai:
            if item['Harga'] == data_maskapai[0]['Harga']:
                
                print(f'\nMaka sistem merekomendasikan jika pengguna melakukan keberangkatan dari Kota {keberangkatan} ke Kota {tujuan} \n')
                print('Maskapai : ', data_maskapai[0]['Maskapai'])
                print(f'Dengan Harga tiket : Rp {item["Harga"]}\n')
                # Menggunakan return statement untuk kembali mengembalikan harga tiket
                return item['Harga']
       