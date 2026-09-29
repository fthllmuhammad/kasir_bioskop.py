#=== PROGRAM SISTEM KASIR MANDIRI PINTAR ===

# Inisialisasi Variabel Awal
total_belanja = 0
jumlah_barang = 0
daftar_barang = "" # Menyimpan nama-nama barang yang dibeli

print("="*45)
print(" SELAMAT DATANG DI SMART SELF-CHECKOUT")
print("="*45)
print("Ketik 'selesai' pada nama barang untuk mengakhiri transaksi\n")

while True:
    # 1. CEK PEMBATASAN TRANSAKSI (Maksimal 5 barang)
    if jumlah_barang >= 5:
        print("\n>> Keranjang penuh! Maksimal pembelian adalah 5 barang.")
        break

    # 2. INPUT DATA BARANG
    nama_barang = input(f"Masukkan nama barang ke-{jumlah_barang + 1}: ")

    # Cek jika pengguna ingin menyudahi belanjaan
    if nama_barang.lower() == "selesai":
        break

    harga_barang = int(input(f"Masukkan harga untuk {nama_barang}: Rp"))

    # 3. VALIDASI HARGA (Jika harga <= 0, lewati iterasi ini)
    if harga_barang <= 0:
        print(">> Harga tidak valid! Harap masukkan harga lebih dari 0.\n")
        continue

    # 4. PROSES BARANG YANG VALID
    total_belanja += harga_barang
    
    if daftar_barang == "":
        daftar_barang = nama_barang
    else:
        daftar_barang += ", " + nama_barang
        
    jumlah_barang += 1

    print(f">> Berhasil menambahkan {nama_barang} (Rp{harga_barang}) ke keranjang.")
    print("-" * 40)

# 5. LOGIKA PERHITUNGAN DISKON BERDASARKAN TOTAL BELANJA
diskon = 0

if total_belanja >= 500000:
    diskon = 0.20  # Diskon 20%
elif total_belanja >= 250000:
    diskon = 0.10  # Diskon 10%
elif total_belanja >= 100000:
    diskon = 0.05  # Diskon 5%
else:
    diskon = 0    # Tanpa diskon

# Hitung harga akhir setelah diskon
potongan_harga = total_belanja * diskon
harga_akhir = total_belanja - potongan_harga

# 6. MENAMPILKAN STRUK PEMBELIAN AKHIR
print("\n" + "="*45)
print(" STRUK BELANJA MANDIRI PINTAR")
print("="*45)
print("Barang dibeli  :", daftar_barang if daftar_barang else "Tidak ada barang")
print("Jumlah Item    :", jumlah_barang)
print(f"Total Kotor    : Rp{total_belanja}")
print(f"Diskon Didapat : {int(diskon * 100)}% (Potongan: Rp{int(potongan_harga)})")
print("-" * 45)
print(f"TOTAL AKHIR    : Rp{int(harga_akhir)}")
print("="*45)
print(" Terima kasih telah menggunakan layanan Mandiri kami!")