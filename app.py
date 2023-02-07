import streamlit as st
import requests
import json

st.set_page_config(page_title="Hesap Makinesi", layout="wide")

st.markdown("<h1 style='text-align: center; font-size: 40px;'>Hesap Makinesi!</h1>", unsafe_allow_html=True)
st.markdown("---")

option = st.selectbox(label = 'Ne işlemi yapmak istiyorsunuz?', options = ("Toplama", "Çıkarma", "Çarpma", "Bölme"))

if option == "Toplama":
    operation_option = "Addition"
elif option == "Çıkarma":
    operation_option = "Subtraction"
elif option == "Çarpma":
    operation_option = "Multiplication"
elif option == "Bölme":
    operation_option = "Divison"

st.markdown("<h1 style='text-align: center; font-size: 40px;'>Sizden istenilen rakamları giriniz:!</h1>", unsafe_allow_html=True)

number_x = st.number_input('İlk rakamı giriniz:')
st.write('İlk rakam ', number_x)

number_y = st.number_input('İkinci rakamı giriniz:')
st.write('İkinci rakam ', number_y)

input = {"operation": operation_option, "x": number_x, "y": number_y}

if st.button("Hesapla"):
    response_ = requests.post(url = "http://127.0.0.1:8000/calculate", data = json.dumps(input))
    st.subheader(f"Sonuç = {response_.text}")

# ---- STREAMLIT STİLİNİ SAKLA ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)