nama = input("Masukkan Nama: ")
nik = input("Masukkan NIK: ")

status_list = ["Pegawai Tetap", "Honor"]
golongan_list = ["A", "B", "C"]

gaji_pokok = {
    "Pegawai Tetap": 1000000,
    "Honor": 750000
}

bonus_golongan = {
    "Pegawai Tetap": {"A": 200000, "B": 400000, "C": 550000},
    "Honor": {"A": 150000, "B": 275000, "C": 480000}
}


total_gaji_per_status = {
    "Pegawai Tetap": 0,
    "Honor": 0
}

print("\n=== Daftar Gaji dan Bonus ===")
print("Nama:", nama)
print("NIK:", nik)
print("===========================================")

for status in status_list:
    for golongan in golongan_list:
        gaji = gaji_pokok[status]
        bonus = bonus_golongan[status][golongan]
        gaji_total = gaji + bonus

        total_gaji_per_status[status] += gaji_total

        print("Status    :", status)
        print("Golongan  :", golongan)
        print("Gaji Pokok: Rp", gaji)
        print("Bonus     : Rp", bonus)
        print("Gaji Total: Rp", gaji_total)
        print("-------------------------------------------")

print("===========================================")

print("Total Gaji + Bonus untuk setiap Status:")
for status in total_gaji_per_status:
    print(status, ": Rp", total_gaji_per_status[status])
print("===========================================")