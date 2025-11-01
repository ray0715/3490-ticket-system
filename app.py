import streamlit as st
import pandas as pd
import os

# -----------------------------
# 檔案與初始設定
# -----------------------------
DATA_FILE = "signup_data.csv"
CONFIG_FILE = "config.txt"

# 如果資料檔不存在，建立空 CSV
if not os.path.exists(DATA_FILE):
    pd.DataFrame(columns=["姓名", "Email", "電話", "序號"]).to_csv(DATA_FILE, index=False)

# 如果設定檔不存在，建立預設設定
if not os.path.exists(CONFIG_FILE):
    with open(CONFIG_FILE, "w") as f:
        f.write("limit=5\npassword=123456")

# -----------------------------
# 讀取/寫入設定
# -----------------------------
def read_config():
    cfg = {"limit": 5, "password": "123456"}
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE) as f:
            for line in f:
                k, v = line.strip().split("=")
                if k == "limit":
                    cfg[k] = int(v)
                else:
                    cfg[k] = v
    return cfg

def save_config(limit, password):
    with open(CONFIG_FILE, "w") as f:
        f.write(f"limit={limit}\npassword={password}")

cfg = read_config()

# -----------------------------
# 側邊欄選單
# -----------------------------
page = st.sidebar.selectbox("選擇頁面", ["前台報名", "後台管理"])

# -----------------------------
# 前台報名頁
# -----------------------------
if page == "前台報名":
    st.title("3490第36屆年會報名系統")

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
                    serial = f"{count + 1:03d}"
                    new_row = pd.DataFrame([[name, email, phone, serial]], columns=df.columns)
                    df = pd.concat([df, new_row], ignore_index=True)
                    df.to_csv(DATA_FILE, index=False)
                    st.success(f"報名成功！您的序號是：{serial}")
                    st.balloons()

# -----------------------------
# 後台管理頁
# -----------------------------
elif page == "後台管理":
    st.title("🔐 後台管理")
    pwd = st.text_input("請輸入管理密碼", type="password")

    if pwd == cfg["password"]:
        st.success("登入成功 ✅")

        # 顯示報名資料
        df = pd.read_csv(DATA_FILE)
        st.subheader("報名名單")
        st.dataframe(df)

        # 下載 CSV
        csv = df.to_csv(index=False).encode("utf-8")
        st.download_button("下載報名資料 (CSV)", csv, "signup_data.csv", "text/csv")

        # 設定報名上限與修改密碼
        st.subheader("設定報名限制與後台密碼")
        new_limit = st.number_input("報名上限", value=cfg["limit"], min_value=1, max_value=999)
        new_pwd = st.text_input("修改後台密碼（可留空不改）")

        if st.button("儲存設定"):
            save_config(new_limit, new_pwd if new_pwd else cfg["password"])
            st.success("設定已更新！請重新整理生效。")

    elif pwd:
        st.error("密碼錯誤 ❌")
