# === PROGRAM SISTEM MANAJEMEN INVENTARIS TOKO PINTAR ===

database_produk = {
    "PRD01" : {"nama": "kopi susu", "harga": 15000, "stok": 12},
    "PRD02" : {"nama": "roti bakar", "harga": 12000, "stok": 3},
    "PRD03" : {"nama": "indomie goreng", "harga": 3500, "stok": 25}
}

def tampilkan_inventaris():
    print("\n" + "="*50)
    print("                 Daftar Inventaris Toko")
    print("="*50)
    print(f"{'ID': <7} | {'Nama Barang':<18} | {'Harga':<5}")
    print("="*50)

    for id_prd, detail in database_produk.items():
        print(f"{id_prd:<7} | {detail['nama']:<8} | Rp {detail['harga']:<8}, | {detail['stok']:<5}")
    print("="*50)

def tambah_atau_update_produk(id_produk, nama ,harga, stok):
    if harga < 0 or stok < 0:
        print(">> ERROR: harga atau stok tidak boleh bernilai negatif!")
        return False

    if id_produk in database_produk:
        database_produk[id_produk]["nama"] =  nama
        database_produk[id_produk]["harga"] = harga
        database_produk[id_produk]["stok"] += stok
        print(f">>> BERHASIL: Produk {id_produk} berhasil diperbaharui (stok ditambahkan)")
    else:
        database_produk[id_produk] = {"nama": nama, "harga": harga, "stok": stok}
        print(f">> BERHASIL: Produk baru {id_produk} ({nama}) berhasil didaftarkan.")
    return False

def cek_restok(batas_maksimum):
    barang_butuh_restok = []

    for id_prd, detail in database_produk.items():
        if detail["stok"] <= batas_maksimum:
            barang_butuh_restok.append(detail["nama"])

    return barang_butuh_restok

# --- AREA PENGUJIAN SISTEM (Uji Coba Otomatis) ---
tampilkan_inventaris()

print("\n--- Skenario 1: Menambahkan Produk Baru ---")
tambah_atau_update_produk("PRD04", "Teh Manis", 5000, 30)
print("\n--- Skenario 2: Mengupdate Produk yang Sudah Ada (PRD01) ---")
# Kopi Susu harganya naik menjadi 16000, dan ada pasokan masuk sebanyak 10 pcs
tambah_atau_update_produk("PRD01", "Kopi Susu", 16000, 10)
print("\n--- Skenario 3: Validasi Error Input Negatif ---")
tambah_atau_update_produk("PRD05", "Garam", -2000, 5)
# Tampilkan kembali kondisi inventaris setelah operasi di atas
tampilkan_inventaris()

print("\n--- Skenario 4: Cek Barang yang Stoknya Menipis (Stok <= 5) ---")

butuh_restok = cek_restok(5)

print("Barang yang harus segera di-restok:", butuh_restok)

