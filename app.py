import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Data EDA Studio")

uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    
    # =========================================================
    # PASTE YOUR CODE RIGHT HERE (BEFORE PLOTTING)
    # =========================================================
    if 'Year' in df.columns and 'Value' in df.columns:
        st.subheader("Financial Metrics Over Time")

        # 1. Clean commas out of string formatted numbers
        df['Value'] = df['Value'].astype(str).str.replace(',', '')

        # 2. Safely convert to numeric
        df['Value'] = pd.to_numeric(df['Value'], errors='coerce')

        # 3. Aggregate by Year
        annual_summary = df.groupby('Year', as_index=False)['Value'].sum()

        # 4. Plot full timeline
        fig = px.bar(
            annual_summary, 
            x='Year', 
            y='Value', 
            title='Total Annual Financial Value Across All Industries'
        )
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.dataframe(df)