import streamlit as st
import pandas as pd
import os
from datetime import datetime
import requests
import base64
import io

# -----------------------------
# 從 Streamlit Secrets 讀取 GitHub 設定
# -----------------------------
GITHUB_OWNER = st.secrets["GITHUB_OWNER"]
GITHUB_REPO = st.secrets["GITHUB_REPO"]
GITHUB_FILE_PATH = st.secrets["GITHUB_FILE_PATH"]
GITHUB_TOKEN = st.secrets["GITHUB_TOKEN"]

# -----------------------------
# GitHub 上傳 / 下載功能
# -----------------------------
def read_csv_from_github():
    """從 GitHub 下載 CSV"""
    url = f"https://api.github.com/repos/{GITHUB_OWNER}/{GITHUB_REPO}/contents/{GITHUB_FILE_PATH}"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        content = base64.b64decode(r.json()["content"])
        df = pd.read_csv(io.BytesIO(content))
        return df
    else:
        st.warning("⚠️ 無法從 GitHub 讀取資料，將建立新檔案。")
        return pd.DataFrame(columns=["姓名", "Email", "電話", "序號", "報名時間"])

def push_csv_to_github(local_file, commit_message):
    """將 CSV 上傳到 GitHub"""
    with open(local_file, "r", encoding="utf-8") as f:
        content = f.read()

    url_get = f"https://api.github.com/repos/{GITHUB_OWNER}/{GITHUB_REPO}/contents/{GITHUB_FILE_PATH}"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    r = requests.get(url_get, headers=headers)
    sha = r.json().get("sha") if r.status_code == 200 else None

    data = {
        "message": commit_message,
        "content": base64.b64encode(content.encode("utf-8")).decode("utf-8"),
    }
    if sha:
        data["sha"] = sha

    r = requests.put(url_get, headers=headers, json=data)
    if r.status_code in [200, 201]:
        st.success("✅ CSV 已自動更新到 GitHub")
    else:
        st.error(f"❌ 推送 GitHub 失敗: {r.text}")

# -----------------------------
# 本地暫存設定
# -----------------------------
DATA_FILE = "signup_data.csv"
CONFIG_FILE = "config.txt"

if not os.path.exists(CONFIG_FILE):
    with open(CONFIG_FILE, "w") as f:
        f.write("limit=5\npassword=123456")

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
# Streamlit 頁面設定
# -----------------------------
st.sidebar.title("選單")
page = st.sidebar.selectbox("選擇頁面", ["前台報名", "後台管理", "目前報名清單"])

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
    st.title("📝 3490地區扶青社第36屆年會報名系統")

    df = read_csv_from_github()
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
                    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    new_row = pd.DataFrame([[name, email, phone, serial, now]],
                                           columns=["姓名", "Email", "電話", "序號", "報名時間"])
                    df = pd.concat([df, new_row], ignore_index=True)
                    df.to_csv(DATA_FILE, index=False, encoding="utf-8-sig")
                    st.success(f"報名成功！您的序號是：{serial}")
                    st.balloons()
                    push_csv_to_github(DATA_FILE, f"新增報名: {name} 序號 {serial}")

# -----------------------------
# 後台管理
# -----------------------------
elif page == "後台管理":
    st.title("🔐 後台管理")
    pwd = st.text_input("請輸入管理密碼", type="password")
    if pwd == cfg["password"]:
        st.success("登入成功 ✅")
        df = read_csv_from_github()
        st.subheader("報名名單")
        st.dataframe(df)
        csv = df.to_csv(index=False).encode("utf-8-sig")
        st.download_button("下載報名資料 (CSV)", csv, "signup_data.csv", "text/csv")
        st.subheader("設定報名限制與後台密碼")
        new_limit = st.number_input("報名上限", value=cfg["limit"], min_value=1, max_value=999)
        new_pwd = st.text_input("修改後台密碼（可留空不改）")
        if st.button("儲存設定"):
            save_config(new_limit, new_pwd if new_pwd else cfg["password"])
            st.success("設定已更新！請重新整理生效。")
    elif pwd:
        st.error("密碼錯誤 ❌")

# -----------------------------
# 目前報名清單
# -----------------------------
elif page == "目前報名清單":
    st.title("📋 目前報名清單")
    df = read_csv_from_github()
    st.dataframe(df)
