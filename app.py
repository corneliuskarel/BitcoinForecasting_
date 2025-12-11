import streamlit as st
import pandas as pd
import requests

st.title("Auto-Append Demo (GitHub Actions → Streamlit)")

RAW_URL = "https://raw.githubusercontent.com/corneliuskarel/BitcoinForecasting_/main/data.csv"
REPO = "corneliuskarel/BitcoinForecasting_"
WORKFLOW = "auto_append.yml"

st.subheader("🔹 Current CSV Content from GitHub")

try:
    df = pd.read_csv(RAW_URL, on_bad_lines="skip")
    st.dataframe(df)
except Exception as e:
    st.error(f"Gagal membaca CSV: {e}")

st.subheader("🔹 Trigger manual append (workflow_dispatch)")

if st.button("Run cronjob sekarang"):
    try:
        token = st.secrets["GH_TOKEN"]  # PAT disimpan di Streamlit secrets
        url = f"https://api.github.com/repos/{REPO}/actions/workflows/{WORKFLOW}/dispatches"

        headers = {
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {token}"
        }

        payload = {"ref": "main"}

        r = requests.post(url, headers=headers, json=payload)

        if r.status_code == 204:
            st.success("Workflow berhasil dijalankan!")
        else:
            st.error(f"Error trigger: {r.text}")

    except Exception as e:
        st.error(f"Error: {e}")
