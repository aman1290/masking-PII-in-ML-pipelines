import streamlit as st
import pandas as pd
from modules.PII_masker import mask_pii

st.title("🔐 PII Masking Demo")

uploaded_file = st.file_uploader("Upload CSV", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.subheader("Original Data")
    st.dataframe(df.head())

    pii_cols = st.multiselect("Select PII columns to mask", df.columns.tolist())

    if st.button("Mask PII"):
        masked_df = mask_pii(df.copy(), pii_cols)
        st.subheader("Masked Data")
        st.dataframe(masked_df.head())
