menu =["kopi susu", "matcha latte", "americano"]
harga =[18000, 22000, 15000]
jumlah =[4, 3, 5]

#Hitung subtotal
sub_kopi = jumlah [0] * harga [0]
sub_matcha = jumlah [1] * harga [1]
sub_americano = jumlah [2] * harga [2]

#Subtotal pendapatan
subtotal_pendapatan = sub_kopi, sub_matcha, sub_americano

#Total
BIAYA_OPERASIONAL = 15000
total_seluruh = sub_kopi + sub_matcha + sub_americano
pendapatan_bersih = total_seluruh - BIAYA_OPERASIONAL

#Total barang terjual
total_barang = jumlah[0] + jumlah [1] + jumlah [2]
target_tercapai = total_seluruh > 200000 and total_barang > 10


print(" subtotal :", total_seluruh)
print(" pendapatan bersih :", pendapatan_bersih)
print(" target tercapai :", target_tercapai)