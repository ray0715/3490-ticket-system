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

# --- 設定網頁整體樣式 (含手機強制併排 CSS) ---
def set_design(bg_file):
    bg_base64 = get_base64(bg_file)
    bg_style = f'background-image: url("data:image/jpg;base64,{bg_base64}");' if bg_base64 else ""
    
    st.markdown(f"""
        <style>
        .stApp {{
            {bg_style}
            background-size: cover;
            background-attachment: fixed;
            background-position: center;
        }}
        /* 強制按鈕兩欄併排的容器設定 */
        [data-testid="column"] {{
            width: 48% !important;
            flex: 1 1 45% !important;
            min-width: 45% !important;
        }}
        .content-card {{
            background-color: rgba(255, 255, 255, 0.92);
            padding: 20px;
            border-radius: 15px;
            color: #1f1f1f;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        }}
        /* 按鈕樣式優化 */
        div.stButton > button {{
            width: 100%;
            height: 90px;
            font-size: 16px;
            font-weight: bold;
            border-radius: 12px;
            background-color: rgba(255, 255, 255, 0.95);
            color: #004d99;
            border: 1px solid #ddd;
            margin-bottom: 10px;
            line-height: 1.3;
        }}
        .stTabs [aria-selected="true"] {{
            background-color: #004d99 !important;
            color: white !important;
        }}
        #MainMenu {{visibility: hidden;}}
        footer {{visibility: hidden;}}
        </style>
        """, unsafe_allow_html=True)

set_design('BG.JPG')

if 'page' not in st.session_state:
    st.session_state.page = 'home'

# --- 主程式邏輯 ---

if st.session_state.page == 'home':
    # 注意：這裡檔名必須與 GitHub 上的 image_44758d.PNG 完全一致
    title_img = get_base64("image_44758d.PNG")
    if title_img:
        st.markdown(
            f'<div style="text-align: center;"><img src="data:image/png;base64,{title_img}" style="max-width: 90%; height: auto; margin-bottom: 20px;"></div>',
            unsafe_allow_html=True
        )
    
    # 使用兩欄佈局
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("📅\n年會流程"):
            st.session_state.page = 'schedule'
            st.rerun()
        if st.button("🧩\n記憶拼圖\n分組名單"):
            st.session_state.page = 'group'
            st.rerun()
        if st.button("🏆\n晚會\n得獎名單"):
            st.session_state.page = 'awards'
            st.rerun()
            
    with col2:
        if st.button("📂\n3490扶青社\n社務資料"):
            st.session_state.page = 'data'
            st.rerun()
        if st.button("🍽️\n晚會桌次表"):
            st.session_state.page = 'table'
            st.rerun()
        if st.button("🤝\n贊助商資料"):
            st.session_state.page = 'sponsor'
            st.rerun()

else:
    if st.button("⬅️ 返回主選單", use_container_width=True):
        st.session_state.page = 'home'
        st.rerun()
    
    st.markdown('<div class="content-card">', unsafe_allow_html=True)
    
    if st.session_state.page == 'schedule':
        st.subheader("典禮議程")
        t1, t2 = st.tabs(["05月02日 (六)", "05月03日 (日)"])
        with t1:
            st.markdown("**當日服裝：地區服 / 晚宴：復古服裝**")
            df1 = pd.DataFrame([
                ["13:00-13:30", "行李寄放 & 註冊聯誼", "C棟1樓金鳳廳/2樓國際廳"],
                ["13:30-14:00", "歡迎扶輪長輩及 D2700", "C棟2樓國際廳"],
                ["14:00-17:00", "記憶拼圖活動", "C棟2樓國際廳"],
                ["17:00-17:30", "Check in", "-"],
                ["17:30-19:00", "晚宴", "A棟3樓富貴廳"],
                ["19:00-21:00", "DISCO大舞廳", "C棟1樓金龍廳"],
                ["21:00-22:30", "聯誼會後會", "C棟1樓金龍廳"]
            ], columns=["時間", "內容", "地點"])
            st.table(df1)
        with t2:
            st.markdown("**當日服裝：正式服裝**")
            df2 = pd.DataFrame([
                ["09:00-09:30", "註冊聯誼 + 退房", "早餐:B棟1樓波根第"],
                ["09:30-12:30", "第三十六屆年會典禮", "C棟2樓國際廳"],
                ["12:30-", "歡送 D2700 地區 & 場復", "-"]
            ], columns=["時間", "內容", "地點"])
            st.table(df2)
    # 其他頁面 placeholder...
    st.markdown('</div>', unsafe_allow_html=True)
