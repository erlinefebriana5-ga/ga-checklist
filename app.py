import streamlit as st
import csv
from datetime import datetime

st.title("GA Daily Checklist System")

ga_list = ["Eno", "Ayana", "Ali", "Vani", "Afifah", "Dwi", "Awen"]

shift_data = {
    "Opening": "05:00 AM - 04:00 PM",
    "Split": "07:00 AM - 12:00 PM & 04:00 PM - 09:00 PM",
    "Morning": "07:00 AM - 06:00 PM",
    "Closing Townsite": "11:00 AM - 10:00 PM",
    "Closing": "10:00 AM - 09:00 PM",
}

tasks = [
    "Masuk kerja",
    "Standby di Meja Reception",
    "Checklist Area (Kebersihan & Kerapian)",
    "Balas Email",
    "Report Cardax",
    "Lapor kerusakan ke Maintenance",
    "Administrasi (LTF / Timesheet / Exit Permit / Power BI)",
    "Membuat Weekly Schedule",
    "Membuat Jadwal Onsite",
    "Persiapan Opening / Closing",
]

nama_ga = st.selectbox("Pilih Nama GA", ga_list)
shift = st.selectbox("Pilih Shift", list(shift_data.keys()))
st.write(f"Jam Kerja: {shift_data[shift]}")

st.write("### Checklist Tugas")

checked_tasks = []
for t in tasks:
    if st.checkbox(t):
        checked_tasks.append(t)

if st.button("Simpan Data"):
    tanggal = datetime.now().strftime("%Y-%m-%d")

    with open("report_ga.csv", mode="a", newline="") as file:
        writer = csv.writer(file)

        for t in tasks:
            status = "Done" if t in checked_tasks else "Pending"
            writer.writerow([tanggal, nama_ga, shift, t, status])

    st.success("Data berhasil disimpan!")