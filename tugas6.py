import numpy as np
import pandas as pd
import os

np.random.seed(42)


class GradeBook:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def average(self) -> float:
        return round(float(self.df["nilai"].mean()), 2)

    def pass_rate(self, threshold: float = 70.0) -> float:
        if len(self.df) == 0:
            return 0.0
        jumlah_lulus = (self.df["nilai"] >= threshold).sum()
        return round((float(jumlah_lulus) / len(self.df)) * 100, 2)

    def save_summary(self, path: str) -> None:
        jumlah_baris = len(self.df)
        jumlah_lulus = int((self.df["status"] == "LULUS").sum())
        jumlah_tidak_lulus = int((self.df["status"] == "TIDAK LULUS").sum())

        with open(path, "a", encoding="utf-8") as file:
            file.write("\n=== RINGKASAN GRADEBOOK ===\n")
            file.write(f"Jumlah data        : {jumlah_baris}\n")
            file.write(f"Rata-rata nilai    : {self.average()}\n")
            file.write(f"Persentase lulus   : {self.pass_rate()}%\n")
            file.write(f"Jumlah lulus       : {jumlah_lulus}\n")
            file.write(f"Jumlah tidak lulus : {jumlah_tidak_lulus}\n")

    def __str__(self) -> str:
        return f"GradeBook(jumlah_data={len(self.df)}, rata_rata={self.average()})"


def tulis_ringkasan_awal(path: str, statistik: dict, df: pd.DataFrame) -> None:
    jumlah_baris = len(df)
    jumlah_lulus = int((df["status"] == "LULUS").sum())
    jumlah_tidak_lulus = int((df["status"] == "TIDAK LULUS").sum())

    with open(path, "w", encoding="utf-8") as file:
        file.write("=== RINGKASAN STATISTIK NUMPY ===\n")
        file.write(f"Rata-rata         : {statistik['mean']}\n")
        file.write(f"Median            : {statistik['median']}\n")
        file.write(f"Standar deviasi   : {statistik['std']}\n")
        file.write(f"Nilai minimum     : {statistik['min']}\n")
        file.write(f"Nilai maksimum    : {statistik['max']}\n")

        file.write("\n=== RINGKASAN DATAFRAME ===\n")
        file.write(f"Jumlah baris      : {jumlah_baris}\n")
        file.write(f"Jumlah lulus      : {jumlah_lulus}\n")
        file.write(f"Jumlah tidak lulus: {jumlah_tidak_lulus}\n")


if __name__ == "__main__":
    print("=== NUMPY ===")
    nilai_ujian = np.random.randint(55, 101, size=10)
    print("Array nilai:", nilai_ujian)

    statistik = {
        "mean": round(float(np.mean(nilai_ujian)), 2),
        "median": round(float(np.median(nilai_ujian)), 2),
        "std": round(float(np.std(nilai_ujian)), 2),
        "min": int(np.min(nilai_ujian)),
        "max": int(np.max(nilai_ujian)),
    }

    print(f"Rata-rata       : {statistik['mean']}")
    print(f"Median          : {statistik['median']}")
    print(f"Standar deviasi : {statistik['std']}")
    print(f"Nilai minimum   : {statistik['min']}")
    print(f"Nilai maksimum  : {statistik['max']}")

    print("\n=== PANDAS ===")
    data = {
        "nama": ["Budi", "Siti", "Andi", "Rina", "Dewi"],
        "nim": ["A001", "A002", "A003", "A004", "A005"],
        "nilai": nilai_ujian[:5],
    }

    df = pd.DataFrame(data)
    df["status"] = np.where(df["nilai"] >= 70, "LULUS", "TIDAK LULUS")
    print(df.head())

    path_ringkasan = "ringkasan_tugas6.txt"
    tulis_ringkasan_awal(path_ringkasan, statistik, df)

    print("\n=== OOP: GRADEBOOK ===")
    gradebook = GradeBook(df)
    print(gradebook)
    print(f"Average   : {gradebook.average()}")
    print(f"Pass rate : {gradebook.pass_rate()}%")
    gradebook.save_summary(path_ringkasan)

    print(f"Ringkasan berhasil disimpan ke: {os.path.abspath(path_ringkasan)}")