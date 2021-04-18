import streamlit as st
import numpy as np
import pandas as pd
import time

st.title("Streamlit")

st.write("Progress Bar")
"Start!!"
latest_iteration = st.empty()
bar = st.progress(0)
for i in range(100):
    latest_iteration.text(f"iteration {i+1}")
    bar.progress(i + 1)
    time.sleep(0.1)

"Done!!"
left_col, right_col = st.beta_columns(2)
button = left_col.button("右カラムに文字を表示")
if button:
    right_col.write("Right cols is here.")


expander1 = st.beta_expander("問い合わせ1")
expander1.write("問い合わせ内容を記入してください。")
expander2 = st.beta_expander("問い合わせ2")
expander2.write("問い合わせ内容を記入してください。")
expander3 = st.beta_expander("問い合わせ3")
expander3.write("問い合わせ内容を記入してください。")
# text = st.text_input("あなたの趣味を教えて下さい")
# "あなたの趣味:", text
#
# condition = st.slider("あなたの今のコンディションは？", 0, 100, 50)
# "コンディション:", condition
