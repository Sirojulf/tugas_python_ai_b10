def greet(nama: str) -> str:
    return f"Halo, {nama}!"


def tambah(a: float, b: float = 0.0) -> float:
    return a + b


def rata_rata(angka: list[float]) -> float:
    if not angka:
        return 0.0
    return round(sum(angka) / len(angka), 2)


class Student:
    def __init__(self, nama: str, nim: str, nilai: list[float] | None = None) -> None:
        self.nama = nama
        self.nim = nim
        self.nilai = nilai if nilai is not None else []

    def tambah_nilai(self, skor: float) -> None:
        self.nilai.append(skor)

    def rata_nilai(self) -> float:
        return rata_rata(self.nilai)

    def status(self, threshold: float = 70.0) -> str:
        return "LULUS" if self.rata_nilai() >= threshold else "TIDAK LULUS"

    def __str__(self) -> str:
        return (
            f"Student(nama='{self.nama}', nim='{self.nim}', "
            f"rata={self.rata_nilai()}, status={self.status()})"
        )


if __name__ == "__main__":
    print("=== FUNCTIONS ===")
    print(greet("Arifian"))
    print(f"tambah(5, 7) = {tambah(5, 7)}")
    print(f"tambah(10) = {tambah(10)}")
    print(f"rata_rata([80, 90, 100]) = {rata_rata([80, 90, 100])}")
    print(f"rata_rata([]) = {rata_rata([])}")

    print("\n=== CLASS STUDENT ===")

    mahasiswa1 = Student("Budi", "A123")
    mahasiswa1.tambah_nilai(80)
    mahasiswa1.tambah_nilai(85)
    mahasiswa1.tambah_nilai(90)

    mahasiswa2 = Student("Siti", "B456")
    mahasiswa2.tambah_nilai(60)
    mahasiswa2.tambah_nilai(65)
    mahasiswa2.tambah_nilai(70)

    print(mahasiswa1)
    print(f"Rata-rata {mahasiswa1.nama} = {mahasiswa1.rata_nilai()}")
    print(f"Status {mahasiswa1.nama} = {mahasiswa1.status()}")

    print()

    print(mahasiswa2)
    print(f"Rata-rata {mahasiswa2.nama} = {mahasiswa2.rata_nilai()}")
    print(f"Status {mahasiswa2.nama} = {mahasiswa2.status()}")
