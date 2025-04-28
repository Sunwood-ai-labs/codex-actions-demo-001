import streamlit as st
import random

def main():
    st.title("おみくじアプリ")
    st.write("ボタンをクリックしておみくじを引いてください。")

    fortunes = ["大吉", "中吉", "小吉", "吉", "末吉", "凶"]

    if st.button("おみくじを引く"):
        result = random.choice(fortunes)
        st.subheader(f"🎉 あなたの運勢: {result} 🎉")

if __name__ == "__main__":
    main()