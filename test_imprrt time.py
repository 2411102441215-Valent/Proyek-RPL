import time

# Data Nilai Mahasiswa
nilai_mahasiswa = [78, 85, 90, 67, 88, 92, 76, 81, 95, 70]
cari_nilai = 88

# Implementasi Linear Search
def linear_search(lst, target):
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1

# Implementasi Binary Search (Memerlukan data terurut)
def binary_search(lst, target):
    left, right = 0, len(lst) - 1
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Sorting untuk Binary Search
nilai_mahasiswa.sort()

# Uji Efisiensi dengan Perulangan 10 kali
print("\n=== Analisis Waktu Eksekusi Big-O ===")

for i in range(10):
    print(f"\nIterasi ke-{i+1}")

    # Built-in Python Search
    start = time.time()
    _ = cari_nilai in nilai_mahasiswa
    end = time.time()
    print(f"Built-in Search: {end - start:.10f} detik")

    # Linear Search
    start = time.time()
    _ = linear_search(nilai_mahasiswa, cari_nilai)
    end = time.time()
    print(f"Linear Search: {end - start:.10f} detik")

    # Binary Search
    start = time.time()
    _ = binary_search(nilai_mahasiswa, cari_nilai)
    end = time.time()
    print(f"Binary Search: {end - start:.10f} detik")

# Notasi Big-O dari setiap metode pencarian
print("\n=== Notasi Big-O dari Algoritma ===")
print("Built-in Search (in list)  : O(n)")
print("Linear Search              : O(n)")
print("Binary Search              : O(log n) (butuh data terurut)")
