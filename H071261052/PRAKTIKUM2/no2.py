jarak =float(input("masukkan jarak pengiriman (km): "))

if jarak <=0:
    print("jarak tidak boleh 0 atau negatif")
else:
    express = input("layanan express (ya/tidak): ").lower()
    
    if express != "ya" and express != "tidak":
        print("Invalid")      
    
    else:   
        if jarak <5:
         tarif = 10000
        elif jarak <=20:
         tarif = 20000
        else:
         tarif = 35000
    tarif += 15000 if express =="ya" else 0

    print(f"total tarif pengiriman: Rp{tarif}")