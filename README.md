# 🚲 Bike Sharing Data Analysis Dashboard

Proyek ini berfokus pada **analisis data penggunaan sepeda** menggunakan **Bike Sharing Dataset**.  
Analisis dilakukan untuk memahami pola peminjaman sepeda berdasarkan **waktu dan kondisi cuaca**, serta menyajikan hasilnya melalui **dashboard interaktif berbasis Streamlit**.

---

## 📂 Dataset

Dataset yang digunakan adalah **Bike Sharing Dataset**, yang terdiri dari dua file:

 📄 `day.csv` → Data peminjaman sepeda harian (**digunakan dalam proyek ini**)

Dataset mencakup informasi seperti:
- Jumlah peminjaman sepeda (`cnt`)
- Kondisi cuaca
- Suhu (`temp`)
- Kelembaban (`hum`)
- Kecepatan angin (`windspeed`)
- Hari kerja & akhir pekan
- Musim

---

## 🎯 Tujuan Proyek

- Memahami pola penggunaan sepeda
- Menganalisis pengaruh cuaca terhadap jumlah peminjaman
- Menyampaikan insight melalui visualisasi data
- Menggunakan **machine learning sederhana (regresi)** sebagai pengayaan analisis

---

## 🛠️ Tahapan Analisis

### 1️⃣ Data Preparation
- Memuat dan memahami struktur dataset
- Mengecek missing value dan duplikasi data
- Melakukan transformasi data (label hari dan musim)

### 2️⃣ Exploratory Data Analysis (EDA)
- Analisis statistik deskriptif
- Eksplorasi pola dan hubungan antar variabel
- Menjawab pertanyaan analisis, seperti:
  - Perbedaan penggunaan sepeda pada hari kerja dan akhir pekan
  - Pengaruh kondisi cuaca terhadap jumlah peminjaman

### 3️⃣ Visualisasi Data
- Membuat visualisasi yang relevan dan informatif
- Grafik digunakan untuk memperkuat jawaban atas pertanyaan analisis

### 4️⃣ Machine Learning (Opsional)
- Menggunakan **regresi linier sederhana**
- Model digunakan untuk melihat hubungan variabel cuaca terhadap jumlah peminjaman
- Fokus pada interpretasi hasil, bukan optimasi model

### 5️⃣ Dashboard (Streamlit)
- Menampilkan visualisasi utama
- Menyajikan ringkasan insight
- Dashboard dapat dijalankan di local environment

---

## 💡 Insight Utama

- 📈 Penggunaan sepeda lebih tinggi pada **hari kerja**
- ☀️ Kondisi cuaca cerah menghasilkan rata-rata peminjaman tertinggi
- 🌡️ Suhu memiliki pengaruh positif terhadap jumlah peminjaman
- 💨 Kelembaban dan kecepatan angin cenderung menurunkan jumlah peminjaman

---

## ▶️ Cara Menjalankan Proyek

### 1️⃣ Clone Repository
```bash
git clone https://github.com/username/bike-sharing-analysis.git
cd bike-sharing-analysis


### 2️⃣ (Opsional) Aktifkan Virtual Environment
Penggunaan virtual environment bertujuan agar library yang digunakan tidak bentrok dengan proyek lain.

```bash
python -m venv .venv
source .venv/bin/activate   # Linux / Mac
.venv\Scripts\activate      # Windows
