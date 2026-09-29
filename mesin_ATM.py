#------ membuat mesin ATM sederhana --------
nasabah = 500000

stok_atm = {
    "50000": 10,
    "100000": 5
}


print("="*30)
print("Selamat Datang Di ATM")
print("="*30)

while True:
    atm_masuk = input("Silahkan tarik aung Anda(Hanya bisa uang '100000' atau '50000') atau 'keluar' : ").lower()
    
    if atm_masuk == "keluar":
        print("Terima Kasih Sudah Datang!!")
        break

    if atm_masuk in stok_atm:
        print("Silahkan Melanjutkan Penarikan!!")
    elif atm_masuk != stok_atm:
        atm_masuk != stok_atm 
        print("[ERROR] Pecahan Tidak Tersedia")
        continue
    else:
        atm_masuk = 0
        print("[ERROR] Uang Tidak Tersedia!!!")
        continue

    input_jumlah = int(input("Tarik Berapa? : "))

    

    input_nominal = int(atm_masuk) * input_jumlah

    if input_nominal > nasabah:
        print("SALDO TIDAK CUKUP")
        continue

    nasabah -= input_nominal
    stok_atm[atm_masuk] -= input_jumlah
    hasil = stok_atm

    
    print("="*30)
    print("")
    print("Sisa Stok ATM", stok_atm)
    print("")
    print("="*30)
    print("Anda Menarik Sebesar : ", input_nominal)
    print("Sisa Saldo : ", nasabah)
    print("="*30)
        

    

