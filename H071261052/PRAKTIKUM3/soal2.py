print("--- Setup Denah Bioskop Nonton Yuk---")

while True:
    try:
        n = int(input("Masukkan jumlah baris: "))
        
        if n <=0:
            print("Jumlah baris harus lebih dari 0!")
            continue
        
        break
    except:
        print("Input baris harus berupa angka!")
        
    
while True:
    try:
        m = int(input("Masukkan jumlah kursi per baris: "))
        
        if m <=0:
            print("Jumlah kursi per baris harus lebih dari 0!")
            continue
        
        break
    except:
        print("Input kursi per baris harus berupa angka!")
        
print("--- Daftar Kursi Tersedia ---")
        
#nested loop
for baris in range (1, n + 1):
    for kursi in range (1, m + 1):
        
        #kursi no 13 tidak pernah dijual
        if kursi == 13:
            continue
        
        #baris 1 hanya kursi bernomor ganjil
        if baris == 1 and kursi % 2 == 0:
            continue
        
        print(f"Baris {baris} Kursi {kursi}")
            
        
        