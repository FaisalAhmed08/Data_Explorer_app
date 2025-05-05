import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📊 Data Explorer App")

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.subheader("Raw Data")
    if st.checkbox("Show Raw Data"):
        st.write(df)
    st.subheader("Data Summary")
    st.write(df.describe())
    st.subheader("Missing Values")
    st.write(df.isnull().sum())
    st.subheader("Column Filter")
    selected_columns = st.multiselect("Select columns to view", df.columns.tolist())
    if selected_columns:
        st.write(df[selected_columns])
    st.subheader("Histogram")
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
    col_to_plot = st.selectbox("Select a numeric column", numeric_cols)
    if col_to_plot:
        fig, ax = plt.subplots()
        ax.hist(df[col_to_plot], bins=20)
        ax.set_xlabel(col_to_plot)
        ax.set_ylabel("Frequency")
        st.pyplot(fig)

