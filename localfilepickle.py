

import pandas as pd
import streamlit as st
import pickle

st.set_page_config(page_title="test", layout='wide')

path = st.text_input('incollare il percorso')

if not path:
    st.stop()

filename = 'prova.pickle'
percorso = f'{path}/{filename}'


data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [28, 33, 45, 41],
    'City': ['New York', 'Paris', 'Berlin', 'London']
}

df = pd.DataFrame(data)

if st.button('salva'):
    pickle.dump(df,  open(percorso,'wb'))