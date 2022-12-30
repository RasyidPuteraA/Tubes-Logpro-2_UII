def transport(jarak, data):
    MAX_DISTANCE = 2000
    maskapai = data[0]['Maskapai'] 
    if jarak <= MAX_DISTANCE:
        print(f'Penerbangan {maskapai} dapat dilakukan tanpa transit\n')
    else:
        print(f'Penerbangan{maskapai} memerlukan transit\n')