print("Nomor 1. Kendaraan")
# Membaca input dari pengguna
nama_kendaraan = input("Nama kendaraan? (Mobil, Motor): ")
jenis_bensin = input("Jenis bensin? (Pertalite, Pertamax, Pertamax Turbo): ")
kota_tujuan = input("Kota yang dituju? (Jakarta, Bekasi, Depok, Tangerang, Bogor): ")

# Mendefinisikan data jarak dan harga bensin
data_jarak = {
    "Jakarta": 20,
    "Bekasi": 35.7,
    "Depok": 5,
    "Tangerang": 99,
    "Bogor": 120.6
}

data_bensin = {
    "Pertalite": {"harga": 10000, "jarak_tempuh": 12},
    "Pertamax": {"harga": 14000, "jarak_tempuh": 13},
    "Pertamax Turbo": {"harga": 17000, "jarak_tempuh": 13.5}
}

# Menghitung pemakaian bensin
jarak = data_jarak.get(kota_tujuan, 0)
jarak_tempuh = data_bensin[jenis_bensin]["jarak_tempuh"]
pemakaian_bensin = jarak / jarak_tempuh

# Menghitung total harga
harga_per_liter = data_bensin[jenis_bensin]["harga"]
total_harga = pemakaian_bensin * harga_per_liter

# Menampilkan output
print("\nOutput:")
print("Nama Kendaraan:", nama_kendaraan)
print("Jenis Bensin:", jenis_bensin)
print("Kota yang Dituju:", kota_tujuan)
print("Pemakaian Bensin:", pemakaian_bensin, "liter")
print("Total Harga dari Bensin: Rp", total_harga, "rupiah")

print("")
print("Nomor 2. Makanan dan Minuman")
# Daftar menu makanan dan harganya
menu_makanan = {
    "Nasi Goreng": 15000,
    "Mie Goreng": 12000,
    "Ayam Geprek": 18000
}

# Daftar menu minuman dan harganya
menu_minuman = {
    "Aneka Jus": 15000,
    "Soft Drink": 10000,
    "Sweet Ice Tea": 5000
}

# Input data dari pembeli
nama_pembeli = input("Masukkan Nama Pembeli: ")
no_hp_pembeli = input("Masukkan No Hp Pembeli: ")
jenis_pesanan = input("Pesan Menu Apa? (makanan atau minuman): ")

if jenis_pesanan.lower() == "makanan":
    print("Daftar Menu Makanan:")
    for menu, harga in menu_makanan.items():
        print(f"{menu}: Rp. {harga}")

    pesanan = input("Masukkan pesanan: ")
    jumlah_pesanan = int(input("Masukkan Jumlah Pesanan: "))

    if pesanan in menu_makanan:
        harga_total = menu_makanan[pesanan] * jumlah_pesanan
    else:
        print("Menu tidak valid.")
        exit()

elif jenis_pesanan.lower() == "minuman":
    print("Daftar Menu Minuman:")
    for menu, harga in menu_minuman.items():
        print(f"{menu}: Rp. {harga}")

    pesanan = input("Masukkan pesanan: ")
    jumlah_pesanan = int(input("Masukkan Jumlah Pesanan: "))

    if pesanan in menu_minuman:
        harga_total = menu_minuman[pesanan] * jumlah_pesanan
    else:
        print("Menu tidak valid.")
        exit()
else:
    print("Jenis pesanan tidak valid.")
    exit()

# Output
print("Nama Pembeli:", nama_pembeli)
print("No Hp Pembeli:", no_hp_pembeli)
print("Menu yang di Pesan:", pesanan)
print("Jumlah pesanan:", jumlah_pesanan)
print("Harga yang harus dibayarkan: Rp", harga_total)

print("")
print("Nomor 3.")
for i in range (1, 21):
    if i % 3 == 0:
        print("STT Terpadu Nurul Fikri")
    else:
          print(i)