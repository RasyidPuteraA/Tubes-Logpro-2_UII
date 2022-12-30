from math import radians, sin, cos, sqrt, atan2

def haversine(data, Keberangkatan, Tujuan):
    for item in data:
        if item['City'] == Keberangkatan:
            lat1, lon1 = map(float, item['Kordinat'].split(', '))
        if item['City'] == Tujuan:
            lat2, lon2 = map(float, item['Kordinat'].split(', '))
    # Menconversi derajat ke radian
    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)
    
    # Menghitung selisih latitud dan longitud
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    
    # Menghitung jarak dengan rumus Haversine
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    
    # Menghitung jarak dalam kilometer
    distance = 6371 * c
    print(distance)
    
    return distance
    