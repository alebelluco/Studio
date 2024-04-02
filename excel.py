from io import BytesIO
import streamlit as st
import pandas  as pd

def scarica_excel(df, filename):
    output = BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')
    df.to_excel(writer, sheet_name='Sheet1')
    writer.close()
    st.download_button(
        label="Download Excel workbook",
        data=output.getvalue(),
        file_name=filename,
        mime="application/vnd.ms-excel"
    )

