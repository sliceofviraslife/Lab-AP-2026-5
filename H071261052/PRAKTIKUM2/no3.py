nilai = int(input("masukkan nilai tes (0-100): "))

if nilai <0 or nilai >100:
    print("invalid")
elif nilai >=80: 
    print("lolos ke tahap wawancara")
else:
    pengalaman = int(input("masukkan pengalaman kerja (tahun): "))
    
    if pengalaman <0:
        print("pengalaman kerja tidak boleh negatif")    
    else:
        if nilai >=65 and pengalaman >=2:
         print("Lolos Bersyarat")
    
        else:
            print("tidak lolos")