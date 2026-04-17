"""
Modul perbandingan algoritma pencarian (Linear Search vs Binary Search).
Mengukur waktu eksekusi setiap metode pada data nilai mahasiswa.
"""

import time

# --- Konstanta (menghindari magic numbers/hardcoded values) ---
nilai_mahasiswa = [78, 85, 90, 67, 88, 92, 76, 81, 95, 70]
cari_nilai = 88
JUMLAH_ITERASI = 10


# --- Algoritma Pencarian ---

def linear_search(data: list, target: int) -> int:
    """
    Mencari target dalam list secara sekuensial (berurutan).
    Mengembalikan indeks target jika ditemukan, -1 jika tidak.
    Kompleksitas: O(n)
    """
    for index in range(len(data)):
        if data[index] == target:
            return index
    return -1


def binary_search(sorted_data: list, target: int) -> int:
    """
    Mencari target dalam list yang sudah terurut menggunakan Binary Search.
    Mengembalikan indeks target jika ditemukan, -1 jika tidak.
    Kompleksitas: O(log n) — memerlukan data  yang sudah terurut sebagai prasyarat.
    """
    low, high = 0, len(sorted_data) - 1

    while low <= high:
        mid = (low + high) // 2
        if sorted_data[mid] == target:
            return mid
        elif sorted_data[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


# --- Pengukuran Waktu ---

def measure_execution_time(search_func, data: list, target: int, label: str) -> None:
    """
    Mengukur dan mencetak waktu eksekusi sebuah fungsi pencarian.
    Menghilangkan duplikasi blok timing yang berulang.
    """
    start_time = time.time()
    search_func(data, target)
    elapsed_time = time.time() - start_time
    print(f"  {label:<30}: {elapsed_time:.10f} detik")


def run_builtin_search(data: list, target: int) -> None:
    """Wrapper untuk built-in 'in' operator agar bisa diukur secara seragam."""
    _ = target in data


# --- Program Utama ---

def main():
    # Binary search memerlukan data terurut; gunakan sorted() agar data asli tidak berubah
    sorted_grades = sorted(nilai_mahasiswa)

    print("=== Analisis Waktu Eksekusi Big-O ===\n")

    for iteration in range(1, JUMLAH_ITERASI + 1):
        print(f"Iterasi ke-{iteration}")
        measure_execution_time(run_builtin_search, sorted_grades, cari_nilai, "Built-in Search")
        measure_execution_time(linear_search,      sorted_grades, cari_nilai, "Linear Search")
        measure_execution_time(binary_search,      sorted_grades, cari_nilai, "Binary Search")
        print()

    print("=== Notasi Big-O dari Algoritma ===")
    print("  Built-in Search (in list)  : O(n)")
    print("  Linear Search              : O(n)")
    print("  Binary Search              : O(log n)  — memerlukan data terurut")


if __name__ == "__main__":
    main()
