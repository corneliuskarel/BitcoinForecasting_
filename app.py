import streamlit as st
import pandas as pd

st.title("Auto-Append Demo (GitHub Actions → Streamlit)")

RAW_URL = "https://github.com/corneliuskarel/BitcoinForecasting_/blob/main/data.csv"

st.write("Reading CSV from GitHub:")
st.code(RAW_URL)

# Load CSV from GitHub
df = pd.read_csv(RAW_URL)

st.write("Current CSV content:")
st.dataframe(df)
