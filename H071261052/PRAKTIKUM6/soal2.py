
# SOAL 2 - VOTECLASS
# Sistem Pemilihan Ketua Kelas


def daftar_kandidat(kandidat_set, nama):    #set biar tidak ada duplikat
    nama = nama.strip().capitalize()  

    if nama in kandidat_set:  #meriksa apakah nama sudah terdaftar 
        print(f"'{nama}' sudah terdaftar sebagai kandidat!")
    else:
        kandidat_set.add(nama)  #menambahkan nama ke dalam set kandidat
        print(f"'{nama}' berhasil didaftarkan sebagai kandidat!")


#untuk memvalidasi dan mencatat suara pemilih
def berikan_suara(rekap_suara, kandidat_set, nama_pemilih, pilihan):
    nama_asli = nama_pemilih.strip() 
    kunci = nama_asli.lower()  
    pilihan = pilihan.strip().capitalize()  

    if pilihan not in kandidat_set:  # Memeriksa apakah kandidat yang dipilih terdaftar
        print(f"Kandidat '{pilihan}' tidak terdaftar! Suara tidak dicatat.")
    elif kunci in rekap_suara:  # Memeriksa apakah pemilih sudah pernah memberikan suara
        print(f"'{nama_asli}' sudah memberikan suara sebelumnya!")
    else:
        rekap_suara[kunci] = pilihan  # Menyimpan nama pemilih dan kandidat yang dipilih ke dictionary
        print(f"Suara '{nama_asli}' untuk '{pilihan}' berhasil dicatat!")


def hitung_suara(rekap_suara, kandidat_set):
    perolehan = {}  

    for kandidat in kandidat_set:  
        perolehan[kandidat] = 0  #nilai awal 0 suara untuk setiap kandidat

    for pemilih in rekap_suara:  
        kandidat = rekap_suara[pemilih]  
        perolehan[kandidat] = perolehan[kandidat] + 1  # Menambah jumlah suara kandidat sebanyak 1

    return perolehan  


def tampilkan_hasil(perolehan):
    print("=" * 40)  
    print(" HASIL PEMILIHAN KETUA KELAS")
    print("=" * 40)

    total = 0  
    tertinggi = 0  
    
    for kandidat in sorted(perolehan):  # Mengulangi kandidat berdasarkan urutan abjad
        suara = perolehan[kandidat]  # Mengambil jumlah suara kandidat
        print(f" {kandidat}: {suara} suara") 

        total = total + suara  

        if suara > tertinggi:  #Memeriksa apakah suara kandidat lebih tinggi dari nilai tertinggi saat ini, kalo iya itulah suara tertinggi saatini
            tertinggi = suara  

    print(f"Total suara masuk: {total}")  

    if total == 0:  #apakah belum ada suara yang masuk
        print("Belum ada suara yang masuk, pemenang belum bisa ditentukan.")
    else:
        pemenang = []  #list kosong untuk menyimpan kandidat dengan suara tertinggi

        for kandidat in sorted(perolehan):  
            if perolehan[kandidat] == tertinggi:  # Memeriksa apakah suara kandidat sama dengan nilai tertinggi
                pemenang.append(kandidat)  # Menambahkan kandidat tersebut ke dalam list pemenang

        if len(pemenang) > 1:  # Memeriksa apakah ada lebih dari satu kandidat dengan suara tertinggi
            daftar_seri = ", ".join(pemenang)  #gabungin nama kandidat yg seri itu tp pake koma
            print(f"Hasil SERI antara: {daftar_seri}")
            print("Perlu dilakukan pemilihan ulang!")
        else:
            print(f"PEMENANG: {pemenang[0]} dengan {tertinggi} suara!") 

    print("=" * 40)  


kandidat_set = set()  #set kosong untuk menyimpan kandidat tanpa duplikat
rekap_suara = {}  #Dict kosong untuk menyimpan nama pemilih dan pilihannya


print("=" * 40)
print(" SISTEM PEMILIHAN KETUA KELAS")
print("=" * 40)



print("--- FASE PENDAFTARAN KANDIDAT ---")

while True:  
    nama = input("Masukkan nama kandidat (kosongkan untuk selesai): ").strip()  

    if nama == "":  #apakah pengguna memasukkan nama kosong
        if len(kandidat_set) < 2:  
            print(f"Minimal harus ada 2 kandidat! Saat ini baru {len(kandidat_set)}.")
        else:
            break
    else:
        daftar_kandidat(kandidat_set, nama)

print(f"Kandidat terdaftar: {kandidat_set}") 


print()
print("--- FASE PEMUNGUTAN SUARA ---")

while True:  
    nama_pemilih = input("Nama pemilih (kosongkan untuk selesai): ").strip()  

    if nama_pemilih == "":  
        break  

    print(f"Kandidat yang tersedia: {kandidat_set}")  
    pilihan = input("Pilih kandidat: ").strip()  

    berikan_suara(rekap_suara, kandidat_set, nama_pemilih, pilihan)  


perolehan = hitung_suara(rekap_suara, kandidat_set)
tampilkan_hasil(perolehan)
