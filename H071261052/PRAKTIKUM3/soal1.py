print("---Rekapitulasi Transaksi Dins Store---")
print("Ketik '0' Untuk Menutup Toko Atau Mengakhiri Sesi")

while True:
    try:
        jumlah = int(input("Masukkan Jumlah Item: "))
        
        if jumlah == 0:
            print("Toko ditutup. Sesi rekap selesai")
            break
        
        if jumlah <0:
            print("jumlah tidak boleh negatif")
            continue
        
        if jumlah >100:
            print("Maksimal 100 item per transaksi")
            continue
        
        print(f"Transaksi {jumlah} item berhasil")
        
    except:
        print("Input harus berupa angka!")