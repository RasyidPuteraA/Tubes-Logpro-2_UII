def keberangkatan(city, data):
      # Membuat perulangan while yang akan terus berjalan selama tidak ditemukan harga tiket
  # untuk keberangkatan dari kota yang diminta
  while True:
    try:
      # Mencoba menampilkan harga tiket jika ditemukan
      for item in data:
        if item['City'] == city:
              print(f'Tiket keberangkatan dari {city}\n')
              return city
      else:
        city = input('Kota Keberangkatan: ')
        return city
        break 
    except ValueError as e:
      # Menangani error dengan memberikan instruksi kepada pengguna untuk memasukkan input kembali
      print(f'Tidak ditemukan harga tiket untuk keberangkatan dari {city}\n')
      
def tujuan(city, data):
      # Membuat perulangan while yang akan terus berjalan selama tidak ditemukan harga tiket
  # untuk keberangkatan dari kota yang diminta
  while True:
    try:
      # Mencoba menampilkan harga tiket jika ditemukan
      for item in data:
        if item['City'] == city:
              print(f'Tiket dengan Tujuan {city}\n')
              return city
      else:
        city = input('Kota Tujuan: ')
        return city
        break 
    except ValueError as e:
      # Menangani error dengan memberikan instruksi kepada pengguna untuk memasukkan input kembali
      print(f'Tidak ditemukan harga tiket untuk Tujuan Ke {city}\n')
      
