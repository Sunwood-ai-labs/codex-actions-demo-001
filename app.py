import streamlit as st
import random

st.set_page_config(page_title="おみくじアプリ", layout="centered")
st.title("おみくじアプリ")

if st.button("おみくじを引く"):
    fortunes = ["大吉", "中吉", "小吉", "末吉", "凶", "大凶"]
    result = random.choice(fortunes)
    st.subheader(f"あなたの運勢は: {result}")