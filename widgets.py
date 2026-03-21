import streamlit as st

st.title("Widgets")

name=st.text_input("Enter your name")

age = st.slider("Enter your age:",0,100,25)

st.write(f"Your age is {age}")

options = ["Python","Java","C","C++","C#"]
option = st.selectbox("Choose your language:",options)
st.write(f"You chose {option}")

if name:
    st.write(f"Hello, {name}")
