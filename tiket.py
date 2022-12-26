def tiket(city, data):
      # Membuat perulangan while yang akan terus berjalan selama tidak ditemukan harga tiket
  # untuk keberangkatan dari kota yang diminta
  while True:
    try:
      # Mencoba menampilkan harga tiket jika ditemukan
      for item in data:
        if item['City'] == city:
              print(f'Tiket keberangkatan dari {city}\n\n')
              return
      else:
        # Jika tidak ditemukan harga tiket, maka akan mengalami error
        raise ValueError(f'Tidak ditemukan harga tiket untuk keberangkatan dari {city}\n')
    except ValueError as e:
      # Menangani error dengan memberikan instruksi kepada pengguna untuk memasukkan input kembali
      print(e)
      city = input('Masukkan kota keberangkatan yang sesuai: ')
      return city 
