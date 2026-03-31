# 1. Deklarasi Variabel dan Tipe Data
nama_depan  = "Muhammad" #string
umur = 23 #integer
tinggi_badan = 175.5 #float
is_mahasiswa = True #boolean
hobi = ["musik", "gaming", "jogging"] 

print("=== DEKLARASI VARIABEL DAN TIPE DATA ===")
print("String:", nama_depan)
print("Integer:", umur)
print("Float:", tinggi_badan)
print("Boolean:", is_mahasiswa)
print("List:", hobi)

# 2. Manipulasi String
print("\n=== MANIPULASI STRING ===")
nama_lengkap = nama_depan + " Sirojul Fuad"
print("Nama lengkap:", nama_lengkap)
print("Panjang string:", len(nama_lengkap))
print("Huruf besar:", nama_lengkap.upper())
print("Huruf kecil:", nama_lengkap.lower())

# 3. Operasi Matematika Sederhana
print("\n=== OPERASI MATEMATIKA SEDERHANA ===")
a = 25
b = 6
print("Nilai a =", a)
print("Nilai b =", b)
print("Penjumlahan:", a + b)
print("Pengurangan:", a - b)
print("Perkalian:", a * b)
print("Pembagian:", a / b)
print("Pembagian bulat:", a // b)
print("Sisa bagi:", a % b)


# 4. List dan Akses Elemen
print("\n=== LIST DAN AKSES ELEMEN ===")
makanan = ["soto", "pecel", "mie ayam", "sate", ]
print("List awal:", makanan)
print("Elemen pertama:", makanan[0])
print("Elemen ketiga:", makanan[2])

makanan.append("gule")
print("Setelah append('gule'):", makanan)

makanan.remove("pecel")
print("Setelah remove('pecel'):", makanan)

makanan.pop()
print("Setelah pop():", makanan)

# 5. Penggunaan Input dari User
print("\n=== INPUT USER ===")
input_nama = input("Masukkan nama Anda: ")
input_umur = input("Masukkan umur Anda: ")

print(f"Halo, nama saya {input_nama} dan umur saya {input_umur} tahun.")