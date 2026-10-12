# antrean_awal = [10,20,30,40,50,60]
# antrean_awal.append([70])
# print("setelah append:", angka)
# antrean_awal.insert(2,25)
# print("setelah vip:", angka)
# antrean_awal.pop()

# kata_kunci = ["python", "java", "go", "kotlin"]
# hasil = [kata.upper() for kata in kata_kunci if len(kata) >4]
# print("Setelah filter dan upper:", hasil)
# hasil.reverse()
# print("setelah di reverse:", reversed)

# t = (1,2,3)

# t_list = list(t)
# t_list[0] = 10
# t_list.append(4)
# t_final = tuple(t_list)
# print("tuple final:", t_final)
# print("panjang elemen:", len(t_final))

# data_kelulusan = [
#     ("mahasiswa A", 85),
#     ("mahasiswa B", 40),
#     ("mahasiswa C", 95)
# ]

# print("===Rekap Nilai Mahasiswa===")
# for nama,skor in data_kelulusan:
#     if skor >=80:
#         grade = "grade a"
#     elif skor >=60:
#         grade = "grade b"
#     else:
#         grade = "grade c"
        
#     print(f"{nama} mendapat skor {grade}")

# teks_a = "ID: 1,2,2,3,4"
# teks_b = "ID: 3,4,4,5"


# data_a_str = teks_a.replace("ID: ", "").split(", ")
# data_b_str = teks_b.replace("ID: ", "").split(", ")


# a=set()
# for item in data_a_str:
#     a.add(int(item.strip()))
    
# b=set()
# for item in data_b_str:
#     b.add(int(item.strip()))

# hasil=(len(a), len(a|b), len(a & b), len(a ^ b))
# print(hasil)

# stok_gudang = {"buku":5, "pulpen": 0, "spidol": 12}
# def cek_stok(kunci):
#     if kunci in stok_gudang:
#         if stok_gudang [kunci] > 0:
#             return "tersedia"
#         else:
#             return"habis/kosong"
        
#     else:
#         return"barang tidak terdaftar"

# daftar_pesanan = ["spidol", "pulpen", "penggaris"]
# for i in daftar_pesanan:
#     status = cek_stok(i)
#     print(f"status {i} : {status}")


