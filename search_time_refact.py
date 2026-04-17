"""
Modul perbandingan algoritma pencarian (Linear Search vs Binary Search).
Mengukur waktu eksekusi setiap metode pada data nilai mahasiswa.
"""

import time

# --- Konstanta ---
NILAI_MAHASISWA = [78, 85, 90, 67, 88, 92, 76, 81, 95, 70]
NILAI_YANG_DICARI = 88
JUMLAH_ITERASI = 10


# --- Algoritma Pencarian ---

def linear_search (data: list, target: int) -> int:
    """
    Mencari target dalam list secara berurutan dari awal hingga akhir.
    Mengembalikan indeks target jika ditemukan, -1 jika tidak ditemukan.
    Kompleksitas waktu: O(n)
    """
    for indeks in range(len(data)):
        if data[indeks] == target:
            return indeks
    return -1


def binary_search (data_terurut: list, target: int) -> int:
    """
    Mencari target dalam list yang sudah terurut menggunakan metode bagi-dua.
    Mengembalikan indeks target jika ditemukan, -1 jika tidak ditemukan.
    Kompleksitas waktu: O(log n) — data wajib sudah terurut sebelum digunakan.
    """
    batas_kiri, batas_kanan = 0, len(data_terurut) - 1

    while batas_kiri <= batas_kanan:
        tengah = (batas_kiri + batas_kanan) // 2
        if data_terurut[tengah] == target:
            return tengah
        elif data_terurut[tengah] < target:
            batas_kiri = tengah + 1
        else:
            batas_kanan = tengah - 1

    return -1


def pencarian_bawaan(data: list, target: int) -> None:
    """
    Wrapper untuk operator 'in' bawaan Python,
    agar bisa diukur waktunya secara seragam dengan metode lain.
    """
    _ = target in data


# --- Pengukuran Waktu ---

def ukur_waktu_eksekusi(fungsi_cari, data: list, target: int, label: str) -> None:
    """
    Mengukur dan mencetak waktu eksekusi sebuah fungsi pencarian.
    Dibuat sebagai fungsi tersendiri untuk menghindari pengulangan kode (DRY).
    """
    waktu_mulai = time.time()
    fungsi_cari(data, target)
    waktu_selesai = time.time() - waktu_mulai
    print(f"  {label:<30}: {waktu_selesai:.10f} detik")


# --- Program Utama ---

def utama():
    # Buat salinan data yang sudah terurut menggunakan sorted(),
    # agar data asli NILAI_MAHASISWA tidak berubah (menghindari side effect)
    data_terurut = sorted(NILAI_MAHASISWA)

    print("=== Analisis Waktu Eksekusi Big-O ===\n")

    for iterasi in range(1, JUMLAH_ITERASI + 1):
        print(f"Iterasi ke-{iterasi}")
        ukur_waktu_eksekusi(pencarian_bawaan, data_terurut, NILAI_YANG_DICARI, "Pencarian Bawaan Python")
        ukur_waktu_eksekusi(linear_search, data_terurut, NILAI_YANG_DICARI, "linear_search")
        ukur_waktu_eksekusi(binary_search,  data_terurut, NILAI_YANG_DICARI, "binary_searchr")
        print()

    print("=== Notasi Big-O dari Setiap Algoritma ===")
    print("  Pencarian Bawaan Python  : O(n)")
    print("  Linear Search        : O(n)")
    print("  Binary Search          : O(log n)  — memerlukan data terurut")


if __name__ == "__main__":
    utama()
