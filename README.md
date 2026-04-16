# Search Algorithm Audit — Misi Minggu 5

**Project:** INDIVIDUAL TASK · Code Audit  
**Nama:** Nikon Valent Sakaesa
**NIM:** 2411102441215

---

Repository ini berisi tugas **Code Audit** pada algoritma pencarian (Linear Search & Binary Search).  
Kode diaudit menggunakan prinsip **Clean Code**, kemudian diperbaiki dan dibandingkan hasilnya.

---

## Isi Struktur File

| File | Keterangan |
|------|-----------|
| `search_time_ori.py` | Kode asli sebelum di-refactor |
| `search_time_refact.py` | Kode setelah diterapkan prinsip Clean Code |
| `laporan_code_audit.pdf` | Laporan singkat hasil audit |

---

## Pelanggaran Clean Code yang Ditemukan

| # | Prinsip | Masalah |
|---|---------|---------|
| 1 | **Naming** | Parameter fungsi tidak deskriptif (`lst`, `left`, `right`) |
| 2 | **DRY** | Magic number `10` di-hardcode langsung di loop |
| 3 | **DRY** | Blok timing diulang 3× secara identik |
| 4 | **Comments** | Komentar hanya parafrase kode, tidak menjelaskan *mengapa* |
| 5 | **SRP** | `.sort()` mengubah data global secara implisit (side effect) |
| 6 | **Naming** | Nilai literal `88` tidak diberi nama konstanta |

---

## Perbaikan yang Diterapkan

- **Meaningful Names** — Ganti nama variabel agar lebih deskriptif dan jelas
- **DRY** — Ekstrak blok timing ke fungsi `measure_execution_time()`
- **SRP** — Pisahkan logika ke fungsi tersendiri, tambahkan `main()` sebagai entry point
- **Avoid Side Effects** — Ganti `.sort()` dengan `sorted()` agar data asli tidak berubah
- **Named Constants** — Hardcoded values diganti konstanta (`ITERATION_COUNT`, `TARGET_GRADE`, dll)
- **Useful Comments** — Tambahkan docstring + keterangan kompleksitas O(n) pada setiap fungsi

---

## View File

```bash
python search_time_refact.py
```

---

## Kompleksitas

| Metode | Big-O | Keterangan |
|--------|-------|-----------|
| Built-in Search | O(n) | Operator `in` pada list |
| Linear Search | O(n) | Pencarian sekuensial |
| Binary Search | O(log n) | Memerlukan data terurut |
