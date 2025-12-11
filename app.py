import streamlit as st
import pandas as pd
import requests
import base64

st.title("Auto-Append Demo (GitHub Actions → Streamlit)")

RAW_URL = "https://raw.githubusercontent.com/corneliuskarel/BitcoinForecasting_/main/data.csv"

st.subheader("Current CSV content")
df = pd.read_csv(RAW_URL)
st.dataframe(df)

st.divider()
st.subheader("Run GitHub Actions Manually")

if "GH_TOKEN" not in st.secrets:
    st.error("❌ GH_TOKEN not found in Streamlit Secrets!")
else:
    GH_TOKEN = st.secrets["GH_TOKEN"]

    if st.button("🚀 Run Append Workflow Now"):
        headers = {
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {GH_TOKEN}",
        }

        url = "https://api.github.com/repos/corneliuskarel/BitcoinForecasting_/actions/workflows/auto_append.yml/dispatches"

        payload = {"ref": "main"}

        response = requests.post(url, headers=headers, json=payload)

        if response.status_code == 204:
            st.success("✅ Workflow triggered successfully!")
        else:
            st.error(f"❌ Error: {response.status_code}")
            st.code(response.text)
