def tabel(data):
    # Tentukan nama kolom
    kolom = list(data[0].keys())

    # Tentukan lebar kolom masing-masing dengan mencari panjang string terpanjang
    # di setiap kolom
    lebar_kolom = [max(len(str(baris[nama])) for baris in data) for nama in kolom]

    # Cetak baris pemisah dengan menggunakan tanda "-" sebanyak lebar kolom
    pemisah = '-'.join('-' * lebar for lebar in lebar_kolom)
    print(pemisah)

    # Cetak nama kolom dengan menggunakan format string
    for i, nama in enumerate(kolom):
        print(f"{nama:{lebar_kolom[i]}} ", end=' | ')
    print()

    # Cetak baris pemisah lagi
    print(pemisah)

    # Cetak data dengan menggunakan format string
    for baris in data:
        for i, nama in enumerate(kolom):
            print(f"{baris[nama]:{lebar_kolom[i]}} ", end=' | ')
        print()

    # Cetak baris pemisah lagi
    print(pemisah)
