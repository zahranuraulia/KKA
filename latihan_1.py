print ('---- VARIABEL DAN TIPE DATA ----')
a = 3
type(a)
print('=== int ===')
print(a)
print(type(a))
print('===contoh penjumlahan===')
a = a + 4
print(a)
print('=== float ===')
b = 3.5
type(b)
print (b)
print (type(b))
print('=== str ===')
contoh_teks = 'hai semuanya'
print(contoh_teks)
print(type(contoh_teks))
print('=== list ===')
contoh_list = [1,2,3,4,5,6]
print(contoh_list)
print(type(contoh_list))
print('=== list ke-2 ===')
contoh_list_kedua = ['a', 'b', 'c', 'd', 'e']
contoh_list_kedua[3]
print(contoh_list_kedua[3])

print('---- LIST DAN MANIPULASI ----')
print('-list belanjaan: ')
list_belanja = ['sayur', 'buah', 'daging']
print(list_belanja)
list_belanja.append('kopi')
list_belanja.append('beras')
print('-tambahkan item gula, kopi, beras: ')
print(list_belanja)
for x in list_belanja:
    print('Nama barang belanjaan: ', x)
print('---- DICTIONARY ----')
print('- harga semua belanjaan:')
daftar_harga = {'beras': 12.000, 'minyak': 17.000, 'telur' : 24.000, 'gula': 15.000, 'kopi': 20.000}
barang_belanjaan = ['beras', 'minyak', 'telur', 'gula', 'kopi']
list_harga = [daftar_harga[x] for x in barang_belanjaan]
print(list_harga)
total_harga = sum(list_harga)
print('- Total harga semua barang belanjaan: ')
print(total_harga)
print('----FUNGSI----')
print('- menghitung luas lingkaran yang mengembalikan nilas luas dan keliling')
import math
def luas_keliling_lingkaran(r):
    luas = math.pi * r * r
    keliling = 2 * math.pi * r
    print('Luas lingkaran: ', round(luas, 2))
    print('Keliling lingkaran: ', round(keliling, 2))
luas_keliling_lingkaran(7)
print('---- PERCABANGAN ----')
usia = int(input('Masukkan usia: '))
print('Anda adalah', usia)
if usia > 50:
    print('Lansia')
elif usia >= 25:
    print('Dewasa')
elif usia >= 14:
    print('Remaja')
else:
    print('Anak')
