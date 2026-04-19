import streamlit as st
import base64
import pandas as pd

# 1. 網頁基礎配置
st.set_page_config(
    page_title="3490地區年會資訊站",
    page_icon="🧩",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- 背景圖處理函數 ---
def get_base64_of_bin_file(bin_file):
    try:
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except:
        return None

def set_page_style(bin_file):
    bin_str = get_base64_of_bin_file(bin_file)
    bg_css = ""
    if bin_str:
        bg_css = f'background-image: url("data:image/jpg;base64,{bin_str}");'
    
    st.markdown(f"""
        <style>
        .stApp {{
            {bg_css}
            background-size: cover;
            background-attachment: fixed;
            background-position: center;
        }}
        /* 內容區塊半透明底色 */
        .content-card {{
            background-color: rgba(255, 255, 255, 0.85);
            padding: 20px;
            border-radius: 15px;
            border: 1px solid #ddd;
            color: #1f1f1f;
        }}
        /* 強制手機併排的按鈕樣式 */
        div.stButton > button {{
            width: 100%;
            height: 90px;
            font-size: 18px;
            font-weight: bold;
            border-radius: 12px;
            background-color: rgba(255, 255, 255, 0.95);
            color: #004d99;
            border: 2px solid #004d99;
            margin-bottom: 5px;
            box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
        }}
        div.stButton > button:active {{
            background-color: #004d99 !important;
            color: white !important;
        }}
        #MainMenu {{visibility: hidden;}}
        footer {{visibility: hidden;}}
        </style>
        """, unsafe_allow_html=True)

# 執行樣式設定
set_page_style('BG.JPG')

# 2. 頁面狀態管理 (Session State)
if 'page' not in st.session_state:
    st.session_state.page = 'home'

def go_home():
    st.session_state.page = 'home'

# --- 主程式邏輯 ---

# A. 主選單頁面 (強制 2 欄併排)
# --- 請將這段代碼複製並貼到 app.py 中需要顯示標題的位置 ---

# 淨化版標題圖片的 Base64 編碼数据 (已移除雜圖和數字)
cleansed_title_b64 = """
data:image/png;base64,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"
"""

# 使用 markdown 和 HTML 將圖片水平居中並設定 RWD 寬度
st.markdown(
    f"""
    <div style="text-align: center;">
        <img src="{cleansed_title_b64}" style="max-width: 100%; height: auto; margin-bottom: 20px;">
    </div>
    """,
    unsafe_allow_html=True
)
    
    col1, col2 = st.columns(2, gap="small")
    
    with col1:
        if st.button("📅\n年會流程", key="btn1", use_container_width=True):
            st.session_state.page = 'schedule'
            st.rerun()
        if st.button("🧩\n分組名單", key="btn3", use_container_width=True):
            st.session_state.page = 'group'
            st.rerun()
        if st.button("🏆\n得獎名單", key="btn5", use_container_width=True):
            st.session_state.page = 'awards'
            st.rerun()
            
    with col2:
        if st.button("📂\n社務資料", key="btn2", use_container_width=True):
            st.session_state.page = 'data'
            st.rerun()
        if st.button("🍽️\n晚會桌次", key="btn4", use_container_width=True):
            st.session_state.page = 'table'
            st.rerun()
        if st.button("🤝\n贊助商", key="btn6", use_container_width=True):
            st.session_state.page = 'sponsor'
            st.rerun()

# B. 子頁面顯示區
else:
    # 只保留頂部這一個返回按鈕
    if st.button("⬅️ 返回主選單", key="back_top", use_container_width=True):
        go_home()
        st.rerun()
    
    st.markdown('<div class="content-card">', unsafe_allow_html=True)
    
    # --- 1. 年會流程頁面 ---
    if st.session_state.page == 'schedule':
        st.subheader("📅 典禮議程表")
        st.markdown("#### **05月02日 (六)**")
        day1 = {
            "時間": ["13:00-13:30", "13:30-14:00", "14:00-17:00", "17:00-17:30", "17:30-19:00", "19:00-21:00", "21:00-22:30"],
            "流程項目": ["行李寄放 & 註冊聯誼", "歡迎扶輪長輩及 D2700", "記憶拼圖活動", "Check in", "晚宴 (復古風)", "DISCO大舞廳", "聯誼會後會"],
            "地點": ["C棟1/2樓", "C棟2樓國際廳", "C棟2樓國際廳", "-", "A棟3樓富貴廳", "C棟1樓金龍廳", "C棟1樓金龍廳"]
        }
        st.table(pd.DataFrame(day1))
        
        st.markdown("#### **05月03日 (日)**")
        day2 = {
            "時間": ["09:00-09:30", "09:30-12:30", "12:30-"],
            "流程項目": ["註冊聯誼 + 退房", "第三十六屆年會典禮 (正式)", "歡送 D2700 地區 & 場復"],
            "地點": ["B棟1樓西餐廳", "C棟2樓國際廳", "-"]
        }
        st.table(pd.DataFrame(day2))

    # --- 2. 3490社務資料 ---
    elif st.session_state.page == 'data':
        st.subheader("📂 3490 扶青社社務資料")
        st.info("社務資料整理中。")

    # --- 3. 記憶拼圖分組名單 ---
    elif st.session_state.page == 'group':
        st.subheader("🧩 記憶拼圖分組查詢")
        search_name = st.text_input("請輸入姓名查詢：")
        if search_name:
            st.write(f"正在搜尋： {search_name}")

    # --- 4. 晚會桌次表 ---
    elif st.session_state.page == 'table':
        st.subheader("🍽️ 晚會桌次表")
        st.write("請洽現場服務台領取桌次圖。")

    # --- 5. 晚會得獎名單 ---
    elif st.session_state.page == 'awards':
        st.subheader("🏆 晚會得獎名單")
        st.balloons()

    # --- 6. 贊助商資料 ---
    elif st.session_state.page == 'sponsor':
        st.subheader("🤝 贊助商資料")
        st.write("感謝您的支持！")

    st.markdown('</div>', unsafe_allow_html=True)
