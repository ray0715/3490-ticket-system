import streamlit as st
import pandas as pd
import os
from datetime import datetime

# -----------------------------
# 檔案與初始設定
# -----------------------------
DATA_FILE = "signup_data.csv"
CONFIG_FILE = "config.txt"

# 建立 CSV，如果不存在
if not os.path.exists(DATA_FILE):
    pd.DataFrame(columns=["姓名","Email","電話","序號","報名時間"]).to_csv(DATA_FILE,index=False)

# 建立設定檔，如果不存在
if not os.path.exists(CONFIG_FILE):
    with open(CONFIG_FILE, "w") as f:
        f.write("limit=5\npassword=123456")

# 讀取設定
def read_config():
    cfg = {"limit": 5, "password": "123456"}
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE) as f:
            for line in f:
                k,v = line.strip().split("=")
                if k == "limit":
                    cfg[k] = int(v)
                else:
                    cfg[k] = v
    return cfg

# 儲存設定
def save_config(limit, password):
    with open(CONFIG_FILE, "w") as f:
        f.write(f"limit={limit}\npassword={password}")

cfg = read_config()

# -----------------------------
# 側邊欄
# -----------------------------
page = st.sidebar.selectbox("選擇頁面", ["前台報名","後台管理","目前報名清單","查詢報名資料"])

# -----------------------------
# 活動資訊
# -----------------------------
st.markdown("### 活動資訊")
st.markdown("""
**活動時間：** 2025/05/03(六)-05/04(日) 13:00 註冊聯誼  
**活動地點：** 群策翡翠灣溫泉飯店 (新北市萬里區海景路一號)  
**活動費用：** 3490地區扶青社員: 3600 元
""")

# -----------------------------
# 前台報名
# -----------------------------
if page == "前台報名":
    st.title("3490地區扶青社第36屆年會報名系統")
    df = pd.read_csv(DATA_FILE)
    count = len(df)

    if count >= cfg["limit"]:
        st.warning("報名已額滿！")
    else:
        st.info(f"目前已有 {count} 人報名（上限 {cfg['limit']} 人）")
        with st.form("signup_form"):
            name = st.text_input("姓名")
            email = st.text_input("Email")
            phone = st.text_input("電話")
            submitted = st.form_submit_button("送出報名")
            if submitted:
                if not name or not email:
                    st.error("請填寫完整資料")
                else:
                    serial = f"{count+1:03d}"
                    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    # 建立新列，避免 df.columns 不一致問題
                    new_row = pd.DataFrame([[name,email,phone,serial,now]],
                                           columns=["姓名","Email","電話","序號","報名時間"])
                    df = pd.concat([df,new_row],ignore_index=True)
                    df.to_csv(DATA_FILE,index=False)
                    st.success(f"報名成功！您的序號是：{serial}")
                    st.balloons()

# -----------------------------
# 後台管理
# -----------------------------
elif page == "後台管理":
    st.title("🔐 後台管理")
    pwd = st.text_input("請輸入管理密碼", type="password")
    if pwd == cfg["password"]:
        st.success("登入成功 ✅")
        df = pd.read_csv(DATA_FILE)
        st.subheader("報名名單")
        st.dataframe(df)
        csv = df.to_csv(index=False).encode("utf-8")
        st.download_button("下載報名資料 (CSV)", csv, "signup_data.csv", "text/csv")

        st.subheader("設定報名限制與後台密碼")
        new_limit = st.number_input("報名上限", value=cfg["limit"], min_value=1,max_value=999)
        new_pwd = st.text_input("修改後台密碼（可留空不改）")
        if st.button("儲存設定"):
            save_config(new_limit,new_pwd if new_pwd else cfg["password"])
            st.success("設定已更新！請重新整理生效。")
    elif pwd:
        st.error("密碼錯誤 ❌")

# -----------------------------
# 目前報名清單
# -----------------------------
elif page == "目前報名清單":
    st.title("📋 目前報名清單")
    df = pd.read_csv(DATA_FILE)
    # 將報名時間轉 datetime，如果格式錯誤或空值就用 NaT
    df["報名時間"] = pd.to_datetime(df["報名時間"], errors="coerce")
    st.dataframe(df)

# -----------------------------
# 查詢報名資料
# -----------------------------
elif page == "查詢報名資料":
    st.title("🔎 查詢報名資料")
    query_email = st.text_input("請輸入您的 Email 查詢")
    if st.button("查詢"):
        df = pd.read_csv(DATA_FILE)
        result = df[df["Email"]==query_email]
        if not result.empty:
            st.success("查詢成功！")
            st.dataframe(result)
        else:
            st.warning("查無資料")
