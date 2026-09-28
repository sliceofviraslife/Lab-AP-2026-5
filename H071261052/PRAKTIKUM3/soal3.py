while True:
    try:
        N = int(input("Masukkan maksimal kursi bus: "))
        break
    except:
        print("Input jumlah kursi harus berupa angka")
        
print("--- Sistem Reservasi 'PO BUS' Dimulai ---")

sisa_kursi = N
total_pendapatan = 0

while sisa_kursi >0:
    print(f"Sisa kursi: {sisa_kursi}")
    
    try:
        umur = int(input("masukkan umur penumpang:"))
    except:
        print("Input umur harus berupa angka")
        continue
    
    if umur <=0:
        print("Umur tidak valid!")
        continue
    
    if umur <=5:
        harga = 0
        print("Kategori: Balita - Tiket Gratis (Rp 0)")
        
    elif umur <=12:
        harga = 50000
        print("Kategori: Anak - Harga: Rp 50000")

    else:
        harga = 100000
        print("Kategori: Dewasa - Harga Rp 100000")
        
    sisa_kursi -= 1
    total_pendapatan += harga
    
print(" --- Semua Kursi Terisi ---")
print(f"Total pendapatan perjalanan PO BUS kli ini: Rp {total_pendapatan}")            