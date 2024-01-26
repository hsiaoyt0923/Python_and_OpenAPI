import requests
import pandas as pd
import streamlit as st
from streamlit_autorefresh import st_autorefresh

st_autorefresh(interval=10000, limit=100)

url = 'https://openapi-pico.onrender.com/pico_w/?count=10'

r = requests.get(url)

if r.status_code == 200:
    print("下載成功")
    data = r.json()

df = pd.DataFrame(data)

st.header('學院雞舍')
st.divider()
st.caption('溫度_光線表')
st.write(df)
st.divider()
st.caption(':blue[光線]')
st.line_chart(df, x='date', y='light')
st.divider()
st.caption(':red[溫度]')
st.line_chart(df, x='date', y='temperature', color='#ff0000')