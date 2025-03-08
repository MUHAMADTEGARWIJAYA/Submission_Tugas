#INI KODE MILIK MUHAMAD TEGAR WIJAYA 
#MEMULAI MENERJAKAN PADA TANGGAL 7 MARET 20:30 WIB SAMPAI 8 MARET 15:23
#MOHON UNTUK DI CEK TERIMAKASIH

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df_day = pd.read_csv("day.csv")  
df_hour = pd.read_csv("hour.csv")  

st.title("Dashboard Analisis Bike Sharing")

# Scatter plot - Pengaruh Suhu terhadap Penyewaan
st.subheader("Pengaruh Suhu terhadap Penyewaan Sepeda")
fig, ax = plt.subplots(figsize=(10, 5))
sns.scatterplot(x=df_day["temp"], y=df_day["cnt"], ax=ax)
ax.set_xlabel("Suhu")
ax.set_ylabel("Jumlah Penyewaan")
ax.set_title("Pengaruh Suhu terhadap Penyewaan Sepeda")
st.pyplot(fig)

# Bar plot - Penyewaan berdasarkan Musim
st.subheader("Jumlah Penyewaan Sepeda Berdasarkan Musim")
fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(x=df_day["season"], y=df_day["cnt"], ax=ax)
ax.set_xlabel("Musim")
ax.set_ylabel("Jumlah Penyewaan")
ax.set_title("Jumlah Penyewaan Sepeda Berdasarkan Musim")
st.pyplot(fig)

# Opsional - Penyewaan per jam jika dataset 'hour' tersedia
if "hr" in df_hour.columns:
    st.subheader("Pola Penyewaan Sepeda per Jam")
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.lineplot(x=df_hour["hr"], y=df_hour["cnt"], ax=ax)
    ax.set_xlabel("Jam")
    ax.set_ylabel("Jumlah Penyewaan")
    ax.set_title("Pola Penyewaan Sepeda sepanjang Hari")
    st.pyplot(fig)

st.write("**Kesimpulan:**")
st.write("- Penyewaan sepeda meningkat seiring kenaikan suhu.")
st.write("- Musim panas (season 3) memiliki jumlah penyewaan tertinggi.")
st.write("- (Jika ada data jam) Pola penyewaan tinggi saat jam kerja (pagi & sore).")
