ALFABET = "abcdefghijklmnopqrstuvwxyz"


def bersihkan_teks(teks):
    hasil = ""  #Menyiapkan string kosong untuk menampung huruf-huruf yang lolos pemeriksaan.

    for karakter in teks:
        karakter_kecil = karakter.lower()

        #cuma ambil huruf dari alfabet 
        if karakter_kecil in ALFABET: 
            hasil += karakter_kecil

    return hasil


def cek_palindrome(teks):
    teks_balik = "".join(reversed(teks))  #membalik urutan karakter->menggabungkan karakter yang sudah dibalik menjadi sebuah string.

    if teks == teks_balik:
        return (True, -1)  #tidak ada indeks yg salah

    for i in range(len(teks)):         #kalau bukan palindorme
        if teks[i] != teks_balik[i]: 
            return (False, i)

    return (True, -1)


def inti_palindrome(teks):
    teks_bersih = bersihkan_teks(teks)

    if teks_bersih == "":
        return {
            "teks": "",
            "panjang": 0,
            "indeks_awal": -1
        }

    palindrom_terbaik = ""
    indeks_terbaik = 0

    # coba semua substring
    for i in range(len(teks_bersih)):     #i menentukan indeks awal substring
        for j in range(i + 1, len(teks_bersih) + 1):   #j menentukan indeks akhir substring
            bagian = teks_bersih[i:j]     #mengambil potongan indeks i sampai sblm indeks j

            hasil_cek = cek_palindrome(bagian)

            if hasil_cek[0]:      #0 adalah nilai True atau False yang menunjukkan apakah potongan itu palindrom.
                # kalau sama panjang, hasil sebelumnya tetap dipakai
                if len(bagian) > len(palindrom_terbaik):
                    palindrom_terbaik = bagian
                    indeks_terbaik = i

    return {
        "teks": palindrom_terbaik,
        "panjang": len(palindrom_terbaik),
        "indeks_awal": indeks_terbaik
    }


# program utama
teks = input("masukkan teks: ")

hasil = inti_palindrome(teks)

print("teks bersih :", bersihkan_teks(teks))
print("hasil       :", hasil)