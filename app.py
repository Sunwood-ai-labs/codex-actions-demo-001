import streamlit as st
import random

def main():
    st.title("おみくじアプリ")
    if st.button("おみくじを引く"):
        fortunes = ["大吉", "中吉", "小吉", "凶"]
        result = random.choice(fortunes)
        st.subheader(f"結果: {result}")

if __name__ == "__main__":
    main()