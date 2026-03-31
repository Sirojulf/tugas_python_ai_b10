
# List – akses & manipulasi
print("=== LIST – AKSES & MANIPULASI ===")
angka_campuran = ["sate", 10, 3.14, "bakso", 25, "geprek"]
print("List awal:", angka_campuran)
print("Elemen pertama:", angka_campuran[0])
print("Elemen terakhir:", angka_campuran[-1])
print("Slicing [1:5:2]:", angka_campuran[1:5:2])

list_manipulasi = angka_campuran.copy()
print("\nSebelum manipulasi:", list_manipulasi)

list_manipulasi.append("pecel")
print("Setelah append('pecel'):", list_manipulasi)

list_manipulasi.insert(2, "mie ayam")
print("Setelah insert(2, 'mie ayam'):", list_manipulasi)

list_manipulasi.extend([99, "seblak"])
print("Setelah extend([99, 'seblak']):", list_manipulasi)

item_pop = list_manipulasi.pop()
print(f"Setelah pop() -> item yang dihapus: {item_pop}")
print("List sekarang:", list_manipulasi)

list_manipulasi.remove("pecel")
print("Setelah remove('pecel'):", list_manipulasi)
print("Sesudah semua manipulasi:", list_manipulasi)


# Tuple – immutability & unpacking
print("\n=== TUPLE – IMMUTABILITY & UNPACKING ===")
profil_tuple = ("Muhammad", "Sirojul", "Fuad", 2022, "Informatika")
print("Tuple:", profil_tuple)
print("Panjang tuple:", len(profil_tuple))
print("Akses indeks 2:", profil_tuple[2])

nama_depan, nama_tengah, *sisa_data = profil_tuple
print("Unpacking:")
print("nama_depan =", nama_depan)
print("nama_tengah =", nama_tengah)
print("sisa_data =", sisa_data)

# Set – keunikan & operasi himpunan
print("\n=== SET – KEUNIKAN & OPERASI HIMPUNAN ===")
set_a = {1, 2, 3, 4, 4, 5}
set_b = {4, 5, 6, 7, 7, 8}
print("Set A:", set_a)
print("Set B:", set_b)
print("Union (A | B):", set_a | set_b)
print("Intersection (A & B):", set_a & set_b)
print("Difference (A - B):", set_a - set_b)
print("Symmetric Difference (A ^ B):", set_a ^ set_b)
print("Contoh duplikat otomatis hilang pada set A dan set B.")

# Dictionary – key/value dasar
print("\n=== DICTIONARY – KEY/VALUE DASAR ===")
mahasiswa = {
    "nama": "Muhammad Sirojul Fuad",
    "nim": "1304212094",
    "angkatan": 2022,
    "kota": "Bandung"
}
print("Dictionary awal:", mahasiswa)

mahasiswa["prodi"] = "Informatika"
print("Setelah tambah key 'prodi':", mahasiswa)

mahasiswa["kota"] = "Tanjungpinang"
print("Setelah ubah nilai key 'kota':", mahasiswa)

del mahasiswa["angkatan"]
print("Setelah hapus key 'angkatan':", mahasiswa)

print("Keys():", mahasiswa.keys())
print("Values():", mahasiswa.values())
print("Items():", mahasiswa.items())
print("Iterasi dictionary:")
for key, value in mahasiswa.items():
    print(f"{key}: {value}")

# Nested structures
print("\n=== NESTED STRUCTURES ===")
daftar_buku = [
    {"judul": "Clean Code", "penulis": "Robert C. Martin", "tahun": 2008},
    {"judul": "Atomic Habits", "penulis": "James Clear", "tahun": 2018},
    {"judul": "Deep Work", "penulis": "Cal Newport", "tahun": 2016},
    {"judul": "The Pragmatic Programmer", "penulis": "Andrew Hunt", "tahun": 1999},
]

print("Semua judul buku dan tahun:")
for buku in daftar_buku:
    print(f"- {buku['judul']} ({buku['tahun']})")


tahun_minimal = 2010
buku_filter = [buku for buku in daftar_buku if buku["tahun"] >= tahun_minimal]
print(f"\nBuku terbit >= {tahun_minimal}:")
for buku in buku_filter:
    print(f"- {buku['judul']} ({buku['tahun']})")

# Comprehension & utilitas
print("\n=== COMPREHENSION & UTILITAS ===")
daftar_angka = list(range(1, 21))
list_genap = [angka for angka in daftar_angka if angka % 2 == 0]
list_kuadrat = [angka ** 2 for angka in daftar_angka]
print("List angka 1-20:", daftar_angka)
print("List genap:", list_genap)
print("List kuadrat:", list_kuadrat)

status_angka = {angka: ("genap" if angka % 2 == 0 else "ganjil") for angka in range(1, 11)}
print("\nDict comprehension {angka: status} untuk 1-10:")
print(status_angka)

kalimat = "Python Data Structures Itu Menarik Sekali"
huruf_unik = {huruf.lower() for huruf in kalimat if huruf.isalpha()}
print("\nKalimat:", kalimat)
print("Huruf unik lowercase:", huruf_unik)

# Keanggotaan & pencarian sederhana
print("\n=== KEANGGOTAAN & PENCARIAN SEDERHANA ===")
item_list = "sate"
print(f"Apakah '{item_list}' ada di list awal?", item_list in angka_campuran)

item_set = 6
print(f"Apakah {item_set} ada di set B?", item_set in set_b)

cari_item = 10
if cari_item in angka_campuran:
    print(f"Angka {cari_item} ditemukan di list awal pada indeks ke-{angka_campuran.index(cari_item)}")
else:
    print(f"Angka {cari_item} tidak ditemukan di list awal")

cek_buku = "Deep Work"
if any(buku["judul"] == cek_buku for buku in daftar_buku):
    print(f"Buku '{cek_buku}' tersedia di daftar_buku")
else:
    print(f"Buku '{cek_buku}' tidak tersedia di daftar_buku")