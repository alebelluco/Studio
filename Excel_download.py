import pandas as pd
import streamlit as st
#import xlsxwriter
#from io import BytesIO
from excel import scarica_excel

st.set_page_config(page_title="Test excel", layout='wide')

path = st.file_uploader('carica excel')

if  not path:
    st.stop()
df = pd.read_excel(path)
st.write(df[0:10])
scarica_excel(df, 'Download_excel.xlsx')

# dsadhbssdfhsbs