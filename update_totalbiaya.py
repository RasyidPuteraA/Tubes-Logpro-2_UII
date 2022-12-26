def biaya(data):
    for item in data:
        item['Total Biaya'] = item['Price'] + item['Tiket']
