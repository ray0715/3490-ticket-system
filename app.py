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

# --- 工具函數：讀取圖片並轉為 Base64 ---
def get_base64(file_path):
    try:
        with open(file_path, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except:
        return None

# --- CSS 強制樣式優化 (核心美化) ---
def set_design(bg_file):
    bg_base64 = get_base64(bg_file)
    bg_style = f'background-image: url("data:image/jpg;base64,{bg_base64}");' if bg_base64 else ""
    
    st.markdown(f"""
        <style>
        /* 全域背景 */
        .stApp {{
            {bg_style}
            background-size: cover;
            background-attachment: fixed;
            background-position: center;
        }}
        
        /* 移除 Streamlit 預設間距，讓內容靠上且滿版 */
        .block-container {{
            padding-top: 2rem !important;
            padding-bottom: 0rem !important;
            max-width: 95% !important;
        }}

        /* --- 兩欄式按鈕核心美化 --- */
        [data-testid="column"] {{
            width: 50% !important;
            flex: 1 1 calc(50% - 10px) !important;
            padding: 5px !important;
        }}

        div.stButton > button {{
            width: 100% !important;
            height: 110px !important; /* 增加高度更像 App */
            border-radius: 20px !important; /* 更圓潤 */
            background-color: rgba(255, 255, 255, 0.95) !important;
            color: #2c3e50 !important;
            border: none !important;
            box-shadow: 0 8px 20px rgba(0,0,0,0.1) !important; /* 增加漂浮陰影感 */
            display: flex !important;
            flex-direction: column !important;
            align-items: center !important;
            justify-content: center !important;
            transition: all 0.3s ease !important;
            margin-bottom: 10px !important;
        }}
        
        div.stButton > button p {{
            font-size: 18px !important;
            font-weight: 700 !important;
            line-height: 1.5 !important;
            white-space: pre-wrap !important;
        }}

        div.stButton > button:hover {{
            transform: translateY(-5px) !important;
            box-shadow: 0 12px 25px rgba(0,0,0,0.15) !important;
            background-color: #ffffff !important;
        }}

        /* 內容卡片優化 */
        .content-card {{
            background-color: rgba(255, 255, 255, 0.95);
            padding: 25px;
            border-radius: 20px;
            margin-top: 10px;
        }}

        #MainMenu, footer {{visibility: hidden;}}
        </style>
        """, unsafe_allow_html=True)

set_design('BG.JPG')

if 'page' not in st.session_state:
    st.session_state.page = 'home'

# --- 主選單頁面 ---
if st.session_state.page == 'home':
    # 顯示主視覺標題圖 (使用 GitHub 上對應的檔名)
    # 如果你的標題圖檔名是 PNG 就用 PNG，是 PNG 就用 PNG
    title_img = get_base64("image_44758d.PNG")
    if title_img:
        st.markdown(
            f'<div style="text-align: center;"><img src="data:image/png;base64,{title_img}" style="max-width: 95%; height: auto; margin-bottom: 30px; filter: drop-shadow(0 5px 15px rgba(0,0,0,0.2));"></div>',
            unsafe_allow_html=True
        )
    
    # 建立強制的兩欄選單
    c1, c2 = st.columns(2)
    
    with c1:
        if st.button("📅\n年會流程", key="btn1"):
            st.session_state.page = 'schedule'
            st.rerun()
        if st.button("🧩\n分組名單", key="btn3"):
            st.session_state.page = 'group'
            st.rerun()
        if st.button("🏆\n得獎名單", key="btn5"):
            st.session_state.page = 'awards'
            st.rerun()
            
    with c2:
        if st.button("📂\n社務資料", key="btn2"):
            st.session_state.page = 'data'
            st.rerun()
        if st.button("🍽️\n晚會桌次", key="btn4"):
            st.session_state.page = 'table'
            st.rerun()
        if st.button("🤝\n贊助商", key="btn6"):
            st.session_state.page = 'sponsor'
            st.rerun()

# --- 子頁面內容 ---
else:
    if st.button("⬅️ 返回主選單", use_container_width=True):
        st.session_state.page = 'home'
        st.rerun()
    
    st.markdown('<div class="content-card">', unsafe_allow_html=True)
    
    if st.session_state.page == 'schedule':
        st.subheader("📅 典禮議程")
        t1, t2 = st.tabs(["5月2日 (六)", "5月3日 (日)"])
        
        with t1:
            st.info("💡 地區服 / 晚宴：復古服裝")
            df1 = pd.DataFrame([
                ["13:00-13:30", "行李寄放 & 註冊聯誼", "C棟1/2樓"],
                ["13:30-14:00", "歡迎扶輪長輩及 D2700", "C棟2樓國際廳"],
                ["14:00-17:00", "記憶拼圖活動", "C棟2樓國際廳"],
                ["17:00-17:30", "Check in", "-"],
                ["17:30-19:00", "晚宴 (復古風)", "A棟3樓富貴廳"],
                ["19:00-21:00", "DISCO大舞廳", "C棟1樓金龍廳"],
                ["21:00-22:30", "聯誼會後會", "C棟1樓金龍廳"]
            ], columns=["時間", "項目", "地點"])
            st.table(df1)
        
        with t2:
            st.info("💡 正式服裝")
            df2 = pd.DataFrame([
                ["09:00-09:30", "註冊聯誼 + 退房", "B棟1樓西餐廳"],
                ["09:30-12:30", "第三十六屆年會典禮", "C棟2樓國際廳"],
                ["12:30-", "歡送 & 場復", "-"]
            ], columns=["時間", "項目", "地點"])
            st.table(df2)

    elif st.session_state.page == 'group':
        st.subheader("🧩 分組名單查詢")
        st.write("資料上傳中...")
    
    st.markdown('</div>', unsafe_allow_html=True)
