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
if st.session_state.page == 'home':
    st.markdown("<h2 style='text-align: center; color: #004d99; text-shadow: 1px 1px 2px white;'>🧩 第 36 屆地區年會</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #333; font-weight: bold;'>時光迴響，記憶約定</p>", unsafe_allow_html=True)
    
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
