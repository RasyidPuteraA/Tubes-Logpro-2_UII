import bubble_sort
import welcome
import Loading
import tabel
import tiket
import update
import rekomendasi 
from Jarak import haversine
from data import data
from data import data_maskapai 
 
welcome.welcome()

nama = input('NAMA : ')
nim = int(input('NIM : '))
keberangkatan = input('Kota Keberangkatan: ')
tujuan = input('Kota Tujuan :')

keberangkatan = tiket.keberangkatan(keberangkatan, data)
tujuan = tiket.tujuan(tujuan, data)

print(f'\nBerikut data yang di dapat pada Raw Data Sheet Traveloka \n Untuk melakukan perjalanan dari Kota {keberangkatan} ke Kota {tujuan}\n\n')

a = (nim % 10)
b = round(a / 2)

bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]

Loading.page()

print(f"\n\nTanggal keberangkatan: {3*a} {bulan[b-1]} 2023\n")

update.harga(data_maskapai)

tabel.tabel(data_maskapai)

Loading.page()

print(f"\n\nTanggal keberangkatan: {3*a} {bulan[b-1]} 2023\n")

bubble_sort.bubble_sort(data_maskapai)

tabel.tabel(data_maskapai)

rekomendasi.rekomendasi(keberangkatan,tujuan,data_maskapai)
print(f'Jarak antar Kota : {haversine(data,keberangkatan,tujuan)} KM\n')







