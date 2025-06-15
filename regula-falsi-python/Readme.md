# Laporan Praktikum Komputasi Numerik  
## Metode Regula Falsi

### Informasi Umum
- **Mata Kuliah**: Komputasi Numerik  
- **Tanggal Praktikum**: 14 Juni 2025  
- **Kelompok**:
  - Farikh Muhammad Fauzan – 5025241135  
  - Brave Juliada – 5025241140  
  - Lyonel Oliver Dwiputra – 5025241145  

---

## 📌 Tujuan Praktikum
- Mengimplementasikan algoritma Regula Falsi dalam bahasa Python.  
- Menganalisis proses iterasi dan konvergensi metode.  
- Memvisualisasikan hasil secara grafis.  
- Memvalidasi hasil dengan perhitungan manual.  

---

## 🧠 Latar Belakang  
Metode **Regula Falsi** (False Position) adalah metode pencarian akar non-linear yang menggabungkan kelebihan metode **Biseksi** (konvergensi terjamin) dan **Secant** (konvergensi cepat). Metode ini memanfaatkan nilai-nilai fungsi pada batas interval untuk mendekati akar dengan interpolasi linear.

---

## 🛠️ Tools dan Library
- **Bahasa**: Python 3.x  
- **IDE**: VS Code  
- **Library**:
  - SymPy (untuk parsing ekspresi simbolik)  
  - NumPy (perhitungan numerik)  
  - Matplotlib (visualisasi fungsi)  

---

## 🧪 Algoritma Regula Falsi  
### Input:
- Fungsi f(x)  
- Interval [a, b]  
- Toleransi error `tol`  
- Maksimum iterasi `max_iter`  

### Langkah-langkah:
1. Pastikan f(a) * f(b) < 0  
2. Hitung nilai c:  
   `c = (a*f(b) - b*f(a)) / (f(b) - f(a))`  
3. Evaluasi f(c):  
   - Jika |f(c)| < tol → akar ditemukan  
   - Jika f(a)*f(c) < 0 → update `b = c`, else `a = c`  
4. Ulangi hingga konvergen atau mencapai iterasi maksimal  

---

## 💻 Implementasi Program

File utama: `False_Position_Method_In_Python.py`

```python
def regula_falsi(f_expr, a, b, tol=1e-6, max_iter=100):
    ...
