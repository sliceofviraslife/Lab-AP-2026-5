#SOAL 1 - BOOKNEST
#Sistem inventaris toko buku

def tambah_buku(inventaris, judul, penulis, harga, stok):
    # simpan data buku dalam dictionary
    buku = {
        "judul": judul,                  #dict menyimpan data 1 buku
        "penulis": penulis,
        "harga": harga,
        "stok": stok
    }
    inventaris.append(buku)  # masukin buku ke list inventarisA


def cari_buku(inventaris, kata_kunci):             #inventaris=kumpulan buku yg trsimpan
    hasil = [buku for buku in inventaris           #meriksa setiap buku dalam inventaris.
             if kata_kunci.lower() in buku["judul"].lower()]   #apakah katakunci ada di judul

    if not hasil:
        print("Buku tidak ditemukan.")
        return

    print(f"Ditemukan {len(hasil)} buku:")           #menampilkan jumlah buku yg ditemukan
    for nomor, buku in enumerate(hasil, start=1):     #enumerate: memberikannomor urut serta mengambik elemen list
        print(f"  {nomor}. {buku['judul']} - {buku['penulis']} | "
              f"Rp{buku['harga']} | Stok: {buku['stok']}")


def update_stok(inventaris, judul, jumlah):
    for buku in inventaris:
        if buku["judul"].lower() == judul.lower():      #memeriksa apakah judul dalam dictionary sama dengan judul yang dimasukkan pengguna.
            stok_baru = buku["stok"] + jumlah

            if stok_baru < 0:  # jangan sampai stok minus
                print("Gagal update: stok tidak boleh negatif.")
                return   #kalo stokbaru negatif, program tidak akan disimpan
            buku["stok"] = stok_baru
            
            if jumlah > 0:
                print(f"Stok '{buku['judul']}' bertambah {jumlah}. "
                      f"Stok sekarang: {stok_baru}")
            elif jumlah < 0:
                print(f"Stok '{buku['judul']}' berkurang {abs(jumlah)}. "   #abs=nilai mutlak, ini dipake kalo berkurang
                      f"Stok sekarang: {stok_baru}")
            else:
                print(f"Stok '{buku['judul']}' tidak berubah. "
                      f"Stok sekarang: {stok_baru}")
            return

    print("Error: buku tidak ditemukan.")


def ringkasan_inventaris(inventaris):
    print("=" * 40)
    print("RINGKASAN INVENTARIS BOOKNEST")
    print("=" * 40)

    jumlah_jenis = len(inventaris)     #menghitung jumlah elemen dalam list.
    total_stok = sum(buku["stok"] for buku in inventaris)    #buku["stok"] mengambil stok setiap buku.
    total_aset = sum(buku["harga"] * buku["stok"] for buku in inventaris)      

    print(f"Jumlah jenis buku : {jumlah_jenis}")
    print(f"Total seluruh stok: {total_stok}")
    print(f"Total nilai aset  : Rp{total_aset}")

    if inventaris:  # hindari error kalau belum ada buku
        termahal = max(inventaris, key=lambda buku: buku["harga"])   #lambda buku: buku["harga"] adalah fungsi kecil yang mengambil harga dari setiap dictionary.
        print(f"Buku termahal     : {termahal['judul']} (Rp{termahal['harga']})")
    else:
        print("Buku termahal     : Belum ada buku")
    print("=" * 40)


def input_angka(pesan, minimum=None):
    # ulangi input sampai angka valid dan memenuhi batas minimum
    while True:
        try:
            angka = int(input(pesan))
            if minimum is not None and angka < minimum:
                print(f"Input tidak boleh kurang dari {minimum}.")
                continue
            return angka
        except ValueError:
            print("Input harus berupa angka bulat.")


def main():
    inventaris = []  # semua buku disimpan dalam list of dictionary

    print("=" * 40)
    print("SISTEM INVENTARIS TOKO BUKU BOOKNEST")
    print("=" * 40)

    while True:
        print("\nMenu:")
        print("1. Tambah Buku")
        print("2. Cari Buku")
        print("3. Update Stok")
        print("4. Ringkasan Inventaris")
        print("5. Keluar")
        pilihan = input("Pilih menu (1-5): ").strip()

        if pilihan == "1":
            judul = input("Judul buku: ").strip()
            penulis = input("Penulis: ").strip()
            if not judul or not penulis:
                print("Judul dan penulis tidak boleh kosong.")
                continue
            harga = input_angka("Harga: ", 0)
            stok = input_angka("Stok awal: ", 0)
            tambah_buku(inventaris, judul, penulis, harga, stok)
            print(f"Buku '{judul}' berhasil ditambahkan!")

        elif pilihan == "2":
            kata_kunci = input("Masukkan kata kunci judul: ").strip()
            cari_buku(inventaris, kata_kunci)

        elif pilihan == "3":
            judul = input("Judul buku yang ingin diupdate: ").strip()
            jumlah = input_angka("Jumlah perubahan (positif=tambah, negatif=kurang): ")
            update_stok(inventaris, judul, jumlah)

        elif pilihan == "4":
            ringkasan_inventaris(inventaris)

        elif pilihan == "5":
            print("Terima kasih telah menggunakan BookNest!")
            break

        else:
            print("Pilihan tidak valid. Masukkan angka 1-5.")


if __name__ == "__main__":
    main()