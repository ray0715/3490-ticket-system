import streamlit as st
import pandas as pd
import os
import random
import datetime
import base64
import json
import requests

# === 設定基本參數 ===
DATA_FILE = "signup_data.csv"
REPO = "ray0715/3490-ticket-system"  # ⚠️改成你的 GitHub repo，例如 "JT-engineer/3490-ticket-system"
BRANCH = "main"

# === 初始化 CSV ===
if not os.path.exists(DATA_FILE):
    df = pd.DataFrame(columns=["姓名", "Email", "電話", "報名序號", "報名時間"])
    df.to_csv(DATA_FILE, index=False, encoding="utf-8-sig")

# === 推送 CSV 到 GitHub ===
def push_csv_to_github(file_path, name, serial):
    token = st.secrets["GITHUB_TOKEN"]  # ⚠️需先在 Streamlit Secrets 加入 GITHUB_TOKEN
    file_name = os.path.basename(file_path)

    with open(file_path, "rb") as f:
        content_base64 = base64.b64encode(f.read()).decode("utf-8")

    url_get = f"https://api.github.com/repos/{REPO}/contents/{file_name}?ref={BRANCH}"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json",
        "User-Agent": "streamlit-app"  # 💡一定要是純英文
    }

    # 嘗試取得檔案 SHA
    r = requests.get(url_get, headers=headers)
    sha = r.json().get("sha") if r.status_code == 200 else None

    # 🔒 改為英文 commit message，避免 UnicodeEncodeError
    commit_message = f"update_{serial}"

    payload = {
        "message": commit_message,
        "content": content_base64,
        "branch": BRANCH
    }
    if sha:
        payload["sha"] = sha

    url_put = f"https://api.github.com/repos/{REPO}/contents/{file_name}"
    r = requests.put(
        url_put,
        headers=headers,
        data=json.dumps(payload, ensure_ascii=False).encode("utf-8")
    )

    if r.status_code in [200, 201]:
        st.success("✅ CSV 已成功推送到 GitHub！")
    else:
        st.error(f"❌ 推送失敗 ({r.status_code})：{r.text}")

# === Streamlit 主介面 ===
st.set_page_config(page_title="3490地區年會報名系統", layout="centered")

st.title("🧾 3490地區年會報名系統")
st.markdown("請填寫以下資料完成報名。")

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
            df = pd.read_csv(DATA_FILE, encoding="utf-8-sig")

            # 產生報名序號
            serial = "R" + str(random.randint(10000, 99999))
            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            new_row = pd.DataFrame(
                [[name, email, phone, serial, now]],
                columns=df.columns
            )
            df = pd.concat([df, new_row], ignore_index=True)
            df.to_csv(DATA_FILE, index=False, encoding="utf-8-sig")

            # 推送 GitHub
            try:
                push_csv_to_github(DATA_FILE, name, serial)
            except Exception as e:
                st.warning(f"⚠️ 資料已存入，但推送 GitHub 失敗：{e}")

            st.success(f"報名成功！您的序號是：{serial}")
            st.balloons()
