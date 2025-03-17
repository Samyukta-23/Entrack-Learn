import streamlit as st
import google.generativeai as genai

st.title("Welcome to Entracklearn Bot")

genai.configure(api_key="AIzaSyBDWHjTHHASRRq8535FpIbp2VZ3AoFq2Vw")
text=st.text_input("Enter your queries")
model=genai.GenerativeModel('gemini-pro')
chat=model.start_chat(history=[])

if st.button("Click"):
    response=chat.send_message(text)
    st.write(response.text)