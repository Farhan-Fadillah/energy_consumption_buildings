import streamlit as st
from energy_model import EnergyModel
import datetime
import matplotlib.pyplot as plt
import pandas as pd
import sys

# Load model
model = EnergyModel()
model.train_models()

st.title("Prediksi Konsumsi Energi Gedung")

st.markdown("Masukkan data waktu, suhu, dan aktivitas pengguna:")

# Input
timestamp = st.time_input("Jam (misalnya 14:00)")
temp = st.slider("Suhu (°C)", min_value=15, max_value=40, value=25)
activity = st.slider("Tingkat Aktivitas Pengguna (0.0 - 1.0)", 0.0, 1.0, 0.5)

# Convert timestamp to hour and day of week
now = datetime.datetime.now()
combined_time = datetime.datetime.combine(now.date(), timestamp)
hour = combined_time.hour
dayofweek = combined_time.weekday()

input_data = [temp, activity, hour, dayofweek]

model_choice = st.selectbox("Pilih Model", ["linear", "Decision Tree", "Neural Network"])


MAX_ENERGY_CONSUMPTION = 100.0  

if st.button("Prediksi"):
    result = model.predict(model_choice, input_data)
    energy_consumption = result.item()
    
    # hasil prediksi
    st.success(f"Perkiraan konsumsi energi: {energy_consumption:.2f} kWh")
    
    # Fitur Alert jika konsumsi energi melebihi batas
    if energy_consumption > MAX_ENERGY_CONSUMPTION:
        st.warning("PERINGATAN: Konsumsi energi melebihi batas yang wajar!")
        
        # Rekomendasi aksi untuk mengurangi konsumsi energi
        st.markdown("**Rekomendasi Aksi**:")
        st.markdown("1. **Kurangi suhu AC**: Menurunkan suhu AC dapat mengurangi konsumsi energi.")
        st.markdown("2. **Matikan peralatan elektronik yang tidak diperlukan**: Matikan perangkat yang tidak sedang digunakan.")
        st.markdown("3. **Pengaturan aktivitas pengguna**: Mengurangi aktivitas pengguna atau memindahkan aktivitas ke area lain dengan pengaturan lebih efisien.")
        st.markdown("4. **Periksa sistem pencahayaan**: Pastikan lampu-lampu yang tidak diperlukan dimatikan.")
    else:
        st.success("Konsumsi energi berada dalam batas wajar.")

# Visualisasi history data
if st.checkbox("Tampilkan Grafik Konsumsi Energi Historis"):
    df = model.data.copy()
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df = df.sort_values('timestamp')
    st.line_chart(df.set_index('timestamp')['energy_consumption'])

st.markdown("---")
st.markdown("Made by Farhan Fadillah")
