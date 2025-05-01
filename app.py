import streamlit as st
import random

st.title("おみくじアプリ")

if st.button("おみくじを引く"):
    fortunes = ["大吉", "中吉", "小吉", "吉", "末吉", "凶"]
    result = random.choice(fortunes)
    st.write(f"あなたの運勢は **{result}** です！")