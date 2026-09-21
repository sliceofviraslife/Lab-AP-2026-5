tujuan = input ("masukkan tujuan (pantai/pegunungan/kota): ").lower()
if tujuan not in ["pantai","pegunungan","kota"]:
    print("tujuan invalid")
else:
    waktu = input ("masukkan waktu (pagi/malam): ").lower()
    if waktu not in ["pagi","malam"]:
        print("waktu invalid")
    else:
        tipe_pengunjung = input ("masukkan tipe_pengunjung (anak/dewasa): ").lower()
        if tipe_pengunjung not in ["anak","dewasa"]:
            print("tipe_pengunjung invalid")
        else:
            match tujuan:
                case "pantai":
                    if waktu == "pagi":
                        print("paket rekomendasi: paket A")
                    elif waktu == "malam" and tipe_pengunjung == "dewasa":
                        print("paket rekomendasi: paket C")
                    else:
                        print("tidak ada paket yang cocok")
                        
                case "pegunungan":
                    if waktu == "pagi" and tipe_pengunjung == "dewasa":
                        print("paket rekomendasi: paket B")
                    elif waktu == "malam" and tipe_pengunjung == "dewasa":
                        print("paket rekomendasi: paket C")
                    else:
                        print("tidak ada paket yang cocok")

                case "kota":
                    if waktu == "malam":
                        print("paket rekomendasi: paket C")
                    else:
                        print("tidak ada paket yang cocok")
                        
                case _:
                    print("tidak ada paket yang cocok")
