import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
matplotlib.use("Agg")
import seaborn as sns

# Konfigurasi halaman
st.set_page_config(page_title="Bike Sharing Dashboard", layout="wide")

# Judul
st.title("🚲 Bike Sharing Data Analysis Dashboard")
st.write("Dashboard ini menyajikan hasil Exploratory Data Analysis (EDA) dari Bike Sharing Dataset.")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("day.csv")
    return df

df = load_data()

# Transformasi data
df['day_type'] = df['weekday'].apply(lambda x: 'Weekend' if x in [0, 6] else 'Weekday')

weather_map = {
    1: 'Clear',
    2: 'Mist/Cloudy',
    3: 'Light Rain/Snow',
    4: 'Heavy Rain/Snow'
}
df['weather_label'] = df['weathersit'].map(weather_map)

# Preview data
st.subheader("📊 Dataset Preview")
st.dataframe(df.head())

# Visualisasi 1: Cuaca vs jumlah peminjaman
st.subheader("🌦️ Rata-rata Peminjaman Berdasarkan Kondisi Cuaca")

fig1, ax1 = plt.subplots()
sns.barplot(
    data=df,
    x='weather_label',
    y='cnt',
    estimator='mean',
    ax=ax1
)
ax1.set_xlabel("Kondisi Cuaca")
ax1.set_ylabel("Rata-rata Jumlah Peminjaman")
ax1.set_title("Pengaruh Kondisi Cuaca terhadap Peminjaman Sepeda")
st.pyplot(fig1)

# Visualisasi 2: Hari kerja vs akhir pekan
st.subheader("📅 Peminjaman Sepeda: Hari Kerja vs Akhir Pekan")

fig2, ax2 = plt.subplots()
sns.barplot(
    data=df,
    x='day_type',
    y='cnt',
    estimator='mean',
    ax=ax2
)
ax2.set_xlabel("Tipe Hari")
ax2.set_ylabel("Rata-rata Jumlah Peminjaman")
ax2.set_title("Perbandingan Peminjaman Sepeda")
st.pyplot(fig2)

# Insight
st.subheader("💡 Insight Utama")
st.markdown("""
- Rata-rata peminjaman sepeda tertinggi terjadi saat kondisi cuaca cerah.
- Cuaca buruk cenderung menurunkan jumlah pengguna sepeda.
- Hari kerja memiliki tingkat peminjaman yang lebih tinggi dibandingkan akhir pekan, 
  yang mengindikasikan penggunaan sepeda sebagai sarana transportasi rutin.
""")

