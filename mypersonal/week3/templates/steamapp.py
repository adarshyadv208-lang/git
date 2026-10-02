import streamlit as st
st.title("My First Steamlit App")
name = st.text_input("Enter name")
if name : st.write(f"Hello, {name}!")
num = st.slider("Pick number", 0, 100)

clicked = st.button("Calculate")
agree = st.checkbox("I agree to the terms")
fruit = st.selectbox("Favorite fruit", ["Apple", "Banana" , "Mango"])
col1 , col2 = st.columns(2)
with col1 :st.write("Left side")

col1 , col2 , col3 = st.columns(3)
with col1:
    st.write("Left side")
with col2 :
    st.write("Right side")
with col3 :
    st.write("middle ")