import streamlit as st
import pandas as pd

st.title("Ручной загрузчик Excel файлов")
input_file = st.file_uploader("Загрузить файл:", type="xlsx")

if input_file is not None:
    st.write("Файл загружен. Выполняется проверка...")
    pd_object = pd.read_excel(input_file)
    st.write(pd_object)
else:
    st.write("Укажите имя файла или перетащите сюда файл.")

