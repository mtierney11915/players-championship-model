import streamlit as st
import pandas as pd
data=pd.read_csv(r'C:\Users\Matt Tierney\OneDrive - Bentley University\Sports Analytics Projects\Players Championship Model\ShinyFinal.csv')

st.title('2024 Players Championship Model Results')
st.dataframe(data)

#streamlit run r"C:\Users\MattTierney\OneDrive - BentleyUniversity\Sports Analytics Projects\Players Championship Model\playersstcode.py"
