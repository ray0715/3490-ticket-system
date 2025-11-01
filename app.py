import streamlit as st
import pandas as pd
import os

DATA_FILE = "signup_data.csv"
LIMIT = 5  # 報名上限

if not os.path.exists(DATA_FILE):
    df = pd.DataFrame(columns=["姓名", "Email", "電話", "序號"])
    df.to_csv(DATA_FILE, index=False)

st.title("3490第36屆年會報名系統")

df = pd.read_csv(DATA_FILE)
count = len(df)

if count >= LIMIT:
    st.warning("報名已額滿！")
else:
    st.info(f"目前已有 {count} 人報名（上限 {LIMIT} 人）")

    with st.form("signup_form"):
        name = st.text_input("姓名")
        email = st.text_input("Email")
        phone = st.text_input("電話")
        submitted = st.form_submit_button("送出報名")

        if submitted:
            if not name or not email:
                st.error("請填寫完整資料")
            else:
                serial = f"{count + 1:03d}"
                new_row = pd.DataFrame([[name, email, phone, serial]], columns=df.columns)
                df = pd.concat([df, new_row], ignore_index=True)
                df.to_csv(DATA_FILE, index=False)
                st.success(f"報名成功！您的序號是：{serial}")
                st.balloons()