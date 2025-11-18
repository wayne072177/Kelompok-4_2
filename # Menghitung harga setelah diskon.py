# Menghitung harga setelah diskon

harga = float(input("Masukkan harga awal: "))
diskon_persen = float(input("Masukkan diskon(%): "))

diskon_rp = harga * (diskon_persen / 100)
harga_setelah_diskon = harga - diskon_rp

print("\n=== HASIL PERHITUNGAN DISKON ===")
print("Harga Awal : ", harga)
print("Diskon     : ", diskon_persen, "%")
print("Potongan Harga : ", diskon_rp)
print("Harga setelah diskon:", harga_setelah_diskon)
