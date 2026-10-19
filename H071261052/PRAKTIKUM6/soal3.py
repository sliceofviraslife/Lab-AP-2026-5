# SOAL 3 - PLAYTUNE
# Sistem manajemen playlist musik

def tambah_lagu(playlist, genre_set, judul, artis, genre, durasi):
    lagu = (judul, artis, genre, durasi)
    playlist.append(lagu)  
    genre_set.add(genre)  #menyimpan genre ke dalam set, yang tidak menyimpan duplikat.


def format_durasi(detik):
    menit = detik // 60
    sisa_detik = detik % 60  # % mengambil sisa pembagian
    return f"{menit}:{sisa_detik:02d}"  # :02d membuat angka minimal 2 digit


def tampilkan_playlist(playlist):
    if not playlist:  
        print("Playlist masih kosong.")
        print("Total durasi playlist: 0 menit 0 detik")
        return 

    print("\n" + "=" * 63)  
    print(f"{'No':<4}{'Judul':<21}{'Artis':<15}{'Genre':<10}{'Durasi':<8}")
    print("=" * 63)

    total_durasi = 0  
    for nomor, lagu in enumerate(playlist, start=1):
        judul, artis, genre, durasi = lagu

        print(f"{nomor:<4}{judul[:20]:<21}{artis[:14]:<15}"
              f"{genre:<10}{format_durasi(durasi):<8}")
        # [:20] mengambil maksimal 20 karakter pertama dari judul
        # [:14] mengambil maksimal 14 karakter pertama dari nama artis
        #:<21 menyediakan tempat selebar 21 karakter supaya judul rata kiri.
        # format_durasi() mengubah durasi detik menjadi menit:detik
        total_durasi += durasi  

    print("=" * 63)
    print(f"Total durasi playlist: {total_durasi // 60} menit "
          f"{total_durasi % 60} detik")


def filter_genre(playlist, genre_target):
    # list comprehension buat ambil lagu sesuai genre
    # list comprehension adalah cara singkat membuat list berdasarkan kondisi
    # lagu[2] adalah genre karena urutan tuple: judul[0], artis[1], genre[2], durasi[3]
    return [lagu for lagu in playlist
            if lagu[2].lower() == genre_target.lower()]


def hapus_lagu(playlist, nomor):
    if nomor < 1 or nomor > len(playlist):
        print("Nomor lagu tidak valid.")
        return  

    lagu = playlist.pop(nomor - 1)  # pop() menghapus sekaligus mengambil lagu pada indeks tertentu
    print(f"Lagu '{lagu[0]}' berhasil dihapus!") 


def statistik_playlist(playlist, genre_set):
    print("\n" + "=" * 40)
    print("STATISTIK PLAYLIST PLAYTUNE")
    print("=" * 40)
    print(f"  Total lagu      : {len(playlist)}")  # len() menghitung jumlah lagu
    print(f"  Jumlah genre    : {len(genre_set)}")  # jumlah genre unik dalam set
    print(f"  Daftar genre    : {genre_set}")  # menampilkan semua genre yang tersimpan

    distribusi = {}  
    for genre in genre_set:
        # 1 dihitung jika genre lagu sama dengan genre yang sedang diperiksa
        distribusi[genre] = sum(1 for lagu in playlist if lagu[2] == genre)

    print("\n  Distribusi genre:")
    for genre, jumlah in distribusi.items():
        # "#" * jumlah membuat simbol "#" sebanyak jumlah lagu dalam genre tersebut
        print(f"    {genre:<12}: {'#' * jumlah} ({jumlah})")

    if playlist:  # statistik lagu terpanjang dan terpendek hanya dihitung jika playlist tidak kosong
        terpanjang = max(playlist, key=lambda lagu: lagu[3])
        # max() mencari data dengan nilai terbesar
        # lambda lagu: lagu[3] berarti membandingkan lagu berdasarkan durasinya
        terpendek = min(playlist, key=lambda lagu: lagu[3])
        # min() mencari data dengan nilai terkecil berdasarkan durasi lagu
        print(f"\n  Lagu terpanjang : {terpanjang[0]} "
              f"({format_durasi(terpanjang[3])})")
        print(f"  Lagu terpendek : {terpendek[0]} "
              f"({format_durasi(terpendek[3])})")
    else:
        print("\n  Lagu terpanjang : Belum ada lagu")
        print("  Lagu terpendek : Belum ada lagu")
    print("=" * 40)


def input_durasi():
    # try-except biar input huruf tidak bikin program berhenti
    while True:  # perulangan terus berjalan sampai durasi yang benar dimasukkan
        try:
            durasi = int(input("Durasi (dalam detik): "))
            # int() mengubah input menjadi bilangan bulat
            if durasi <= 0:
                print("Durasi harus berupa angka positif.")
                continue  # melewati sisa kode dan mengulang perulangan dari awal
            return durasi  # mengembalikan durasi jika nilainya valid
        except ValueError:
            # except ValueError dijalankan jika input tidak bisa diubah menjadi int
            # contoh: pengguna memasukkan "abc" atau "3.5"
            print("Durasi harus berupa angka bulat.")


def main():
    playlist = []  # list kosong untuk menyimpan semua lagu dalam bentuk tuple
    genre_set = set()  # set() membuat set kosong untuk menyimpan genre unik

    print("=" * 40)
    print("PLAYLIST MUSIK - PLAYTUNE")
    print("=" * 40)

    while True:  # menu terus ditampilkan sampai pengguna memilih keluar
        print("\nMenu:")
        print("1. Tambah Lagu")
        print("2. Tampilkan Playlist")
        print("3. Filter berdasarkan Genre")
        print("4. Hapus Lagu")
        print("5. Statistik Playlist")
        print("6. Keluar")
        pilihan = input("Pilih menu (1-6): ").strip()
        # input() menerima masukan pengguna sebagai teks
        # strip() menghapus spasi di awal dan akhir teks

        if pilihan == "1":
            judul = input("Judul lagu: ").strip()
            artis = input("Artis: ").strip()
            if not judul or not artis:
                # not judul berarti judul kosong, not artis berarti artis kosong
                print("Judul dan artis tidak boleh kosong.")
                continue  # kembali ke awal perulangan menu

            genre_input = input("Genre (Pop/Rock/Jazz/RnB/Dangdut): ").strip().lower()
            # lower() menyamakan input menjadi huruf kecil agar mudah diperiksa
            # samakan penulisan genre biar RnB tidak berubah jadi Rnb
            genre_map = {
                "pop": "Pop", "rock": "Rock", "jazz": "Jazz",
                "rnb": "RnB", "dangdut": "Dangdut"
            }
            # genre_map adalah dictionary untuk menyamakan penulisan genre
            # get() mengambil value berdasarkan key; jika key tidak ditemukan, hasilnya None
            genre = genre_map.get(genre_input, genre_input.capitalize())
            # capitalize() membuat huruf pertama kapital dan sisanya huruf kecil
            durasi = input_durasi()
            # memanggil fungsi untuk meminta durasi dan memeriksa inputnya
            tambah_lagu(playlist, genre_set, judul, artis, genre, durasi)
            # mengirim data lagu ke fungsi tambah_lagu()
            print(f"Lagu '{judul}' oleh {artis} berhasil ditambahkan!")

        elif pilihan == "2":
            tampilkan_playlist(playlist)  # memanggil fungsi untuk menampilkan semua lagu

        elif pilihan == "3":
            print(f"Genre tersedia: {genre_set}")
            genre_target = input("Masukkan genre yang ingin difilter: ").strip()
            hasil = filter_genre(playlist, genre_target)
            # hasil berisi lagu-lagu yang cocok dengan genre yang dicari

            print(f"\nLagu bergenre '{genre_target}':")
            if not hasil:  # jika hasil kosong, berarti tidak ada lagu yang cocok
                print("  Tidak ada lagu untuk genre tersebut.")
            else:
                for nomor, lagu in enumerate(hasil, start=1):
                    # enumerate() memberi nomor urut mulai dari 1
                    print(f"  {nomor}. {lagu[0]} - {lagu[1]} "
                          f"({format_durasi(lagu[3])})")
                    # lagu[0] adalah judul, lagu[1] adalah artis, lagu[3] adalah durasi

        elif pilihan == "4":
            tampilkan_playlist(playlist)  # menampilkan playlist agar pengguna tahu nomor lagu
            if playlist:  # proses hapus hanya dilakukan jika playlist berisi lagu
                try:
                    nomor = int(input("Nomor lagu yang ingin dihapus: "))
                    # int() mengubah nomor yang dimasukkan menjadi bilangan bulat
                    hapus_lagu(playlist, nomor)
                    # hitung ulang genre supaya genre lagu yang dihapus tidak tertinggal
                    genre_set.clear()  # clear() menghapus semua isi set
                    genre_set.update(lagu[2] for lagu in playlist)
                    # update() menambahkan semua genre dari playlist ke set
                    # set otomatis menghindari genre yang sama tersimpan berulang
                except ValueError:
                    # dijalankan jika input nomor bukan bilangan bulat
                    print("Nomor lagu harus berupa angka bulat.")

        elif pilihan == "5":
            statistik_playlist(playlist, genre_set)
            # memanggil fungsi untuk menampilkan statistik playlist

        elif pilihan == "6":
            print("Terima kasih telah menggunakan PlayTune!")
            break  # menghentikan perulangan menu dan mengakhiri program

        else:
            print("Pilihan tidak valid. Masukkan angka 1-6.")
            # dijalankan jika pengguna memilih selain angka 1 sampai 6


if __name__ == "__main__":
    # __name__ == "__main__" mengecek apakah file ini dijalankan langsung
    # jika iya, fungsi main() akan dijalankan
    main()