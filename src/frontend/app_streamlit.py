import streamlit as st
import requests

st.title("Prediction interface")

features = st.text_input("Enter caracteristics separated by comas:")

if st.button("Predict"):
    url = "http://127.0.0.1:8000/predict/"
    response = requests.post(url, json={"features": [float(x) for x in features.split(",")]})
    st.write(f"Prediction : {response.json()['prediction']}")
