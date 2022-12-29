import bubble_sort
import welcome
import tabel
import tiket
import positioning
import update_totalbiaya
import rekomendasi 
from data import data
 
 
welcome.welcome()

nama = input('NAMA : ')
nim = int(input('NIM : '))
keberangkatan = input('Masukkan kota keberangkatan: ')

keberangkatan = tiket.tiket(keberangkatan, data)

print('\nBerikut data yang di dapat pada Raw Data Sheet Traveloka \nperjalanan dan biaya selama melakukan aktifitas di 5 kota\n\n')

a = nim % 10
b = round(a / 2)

bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]

print(f"Tanggal keberangkatan: {a} {bulan[b-1]} 2023\n")


positioning.position(data, keberangkatan)

update_totalbiaya.biaya(data)

tabel.tabel(data)

print(f"\n\nTanggal keberangkatan: {a} {bulan[b-1]} 2023\n")

bubble_sort.bubble_sort(data)

tabel.tabel(data)

rekomendasi.rekomendasi(keberangkatan, data)

print('\nBerikut Merupakan Urutan yang didapat setelah melakukan Algoritma Bubble Sort : ')
print([item['City'] for item in data], '\n')



