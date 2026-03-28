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
    try:
        import gspread
        from google.oauth2.service_account import Credentials

        scope = [
            "https://www.googleapis.com/auth/spreadsheets",
            "https://www.googleapis.com/auth/drive"
        ]

        creds = Credentials.from_service_account_info(
            st.secrets["gcp_service_account"], scopes=scope
        )

        client = gspread.authorize(creds)
        sheet = client.open("GA Time Management").sheet1

        wita = pytz.timezone("Asia/Makassar")
        now = datetime.now(wita)

        for task in checked_tasks:
            sheet.append_row([
                now.strftime("%Y-%m-%d"),
                now.strftime("%H:%M:%S"),
                nama_ga,
                shift,
                task,
                "Done"
            ])

        st.success("Data berhasil disimpan ke Google Sheet!")

    except Exception as e:
        st.error(f"Error: {e}")
