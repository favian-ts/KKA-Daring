pasien = ["andi", "budi","citra","novan"]

p_darurat = str(input("Masukkan Nama Pasien Darurat: "))
pasien.insert(0, (p_darurat.capitalize()+" (EMERGENCY)"))
print(pasien)