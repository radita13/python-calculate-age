# Program menghitung umur
import datetime as dt

print("\n============================================")
print("========== Program Menghitung Umur =========")
print("============================================")

# Pengguna diminta untuk menginput tanggal lahir untuk mengetahui umur
Year = int(input("Masukkan tahun lahir anda\t: "))
Month = int(input("Masukkan bulan lahir anda\t: "))
day = int(input("Masukkan tanggal lahir anda\t: "))

# Hitung tanggal lahir
dayofbirth = dt.date(Year, Month, day)

# Hari ini
today = dt.date.today()

# Hitung umur dalam hari
youragedays = (today - dayofbirth).days

# Hitung umur dalam tahun,
yourageyears = youragedays // 365

# Hitung umur dalam bulan
youragemonthsremainder = (youragedays % 365) // 30

print("============================================")
print(f"Anda lahir pada {dayofbirth.strftime("%a %b %d-%m-%Y")}")
print(f"Hari ini adalah {today.strftime("%a %b %d-%m-%Y")}")
print("============================================")
print(f"Umur anda dalam hari adalah {youragedays} Hari")
print(f"Umur anda dalam tahun adalah {yourageyears} Tahun")
print(f"Umur anda dalam bulan sisa adalah {youragemonthsremainder} Bulan")
print("============================================\n")