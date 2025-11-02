import streamlit as st
import pandas as pd
import os
import random
import datetime

# === 設定基本參數 ===
DATA_FILE = "signup_data.csv"

# === 初始化 CSV ===
if not os.path.exists(DATA_FILE):
    df = pd.DataFrame(columns=["姓名", "Email", "電話", "報名序號", "報名時間"])
    df.to_csv(DATA_FILE, index=False, encoding="utf-8-sig")

# === Streamlit 主介面 ===
st.set_page_config(page_title="3490地區年會報名系統", layout="centered")
st.title("🧾 3490地區年會報名系統")
st.write("請填寫以下資料完成報名。")

# === 清空資料按鈕 ===
st.markdown("---")
if st.button("⚠️ 清空所有報名資料"):
    df = pd.DataFrame(columns=["姓名", "Email", "電話", "報名序號", "報名時間"])
    df.to_csv(DATA_FILE, index=False, encoding="utf-8-sig")
    st.success("✅ 已清空所有報名資料")

st.markdown("---")
st.write("### 報名表單")

# === 表單輸入 ===
with st.form("signup_form"):
    name = st.text_input("姓名")
    email = st.text_input("Email")
    phone = st.text_input("電話")
    submit = st.form_submit_button("送出報名")

    if submit:
        if not name or not email or not phone:
            st.error("請完整填寫所有欄位！")
        else:
            # 讀取現有 CSV
            df = pd.read_csv(DATA_FILE, encoding="utf-8-sig")

            # 產生報名序號
            serial = "R" + str(random.randint(10000, 99999))
            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # 新增報名
            new_row = pd.DataFrame([[name, email, phone, serial, now]], columns=df.columns)
            df = pd.concat([df, new_row], ignore_index=True)
            df.to_csv(DATA_FILE, index=False, encoding="utf-8-sig")

            st.success(f"報名成功！您的序號是：{serial}")
            st.balloons()

# === 顯示目前報名清單 ===
st.markdown("---")
st.write("### 目前報名清單")
df = pd.read_csv(DATA_FILE, encoding="utf-8-sig")
st.dataframe(df)
