# 🧪 Praktikum Komputasi Numerik  
## Metode Integrasi Romberg (C)

### 👥 Anggota Kelompok
| Nama                     | NRP         | Tugas                                      |
|--------------------------|-------------|---------------------------------------------|
| Farikh Muhammad Fauzan  | 5025241135  | Pembuatan laporan dan analisis hasil        |
| Brave Juliada           | 5025241140  | Verifikasi manual dan optimisasi            |
| Lyonel Oliver Dwiputra  | 5025241145  | Implementasi algoritma utama dan debugging  |

### 📅 Tanggal Praktikum
07 Juni 2025

---

## 📚 Pendahuluan

### 🔎 Latar Belakang
Metode Trapezoidal merupakan pendekatan numerik sederhana untuk integrasi, namun memiliki keterbatasan akurasi ketika jumlah interval masih kecil. **Integrasi Romberg** memperbaiki kelemahan ini dengan menerapkan **ekstrapolasi Richardson** secara berulang terhadap hasil Trapezoidal, sehingga akurasi meningkat secara eksponensial.

### 🎯 Tujuan Praktikum
- Mengimplementasikan integrasi Romberg menggunakan bahasa C.
- Membandingkan akurasi metode Romberg dan Trapezoidal.
- Menganalisis pengaruh tingkat iterasi (`n`) terhadap hasil akhir.

---

## 🛠️ Metodologi

### 📌 Alat & Bahan
- Bahasa C
- `math.h` untuk fungsi `sin(x)`
- Compiler (GCC/Clang)
- IDE seperti VS Code / Dev-C++

### 🧮 Algoritma Romberg
- Input: fungsi `f(x)`, batas `a`, `b`, dan tingkat iterasi `n`
- Proses:
  - Hitung aproksimasi Trapezoidal: `R[i][0]`
  - Lakukan ekstrapolasi Richardson:
    ```
    for j from 1 to n:
        for i from j to n:
            R[i][j] = (4^j * R[i][j-1] - R[i-1][j-1]) / (4^j - 1)
    ```
  - Kembalikan `R[n][n]` sebagai hasil akhir

---

## 💻 Implementasi Program

### 🔗 File:
[`romberg.c`](./Romberg_Integration_In_C.c)

### 🚀 Cara Menjalankan
```bash
gcc romberg.c -o romberg -lm
./romberg
