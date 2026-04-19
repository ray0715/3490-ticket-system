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

# --- 設定網頁整體樣式 ---
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
        /* 內容區塊半透明卡片 */
        .content-card {{
            background-color: rgba(255, 255, 255, 0.92);
            padding: 20px;
            border-radius: 15px;
            color: #1f1f1f;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
            margin-bottom: 20px;
        }}
        /* PyCon 風格 Tabs 調整 */
        .stTabs [data-baseweb="tab-list"] {{ gap: 8px; }}
        .stTabs [data-baseweb="tab"] {{
            height: 45px;
            background-color: rgba(255, 255, 255, 0.6);
            border-radius: 10px 10px 0px 0px;
            padding: 0px 15px;
            font-weight: bold;
            color: #555;
        }}
        .stTabs [aria-selected="true"] {{
            background-color: #004d99 !important;
            color: white !important;
        }}
        /* 兩欄式大按鈕樣式 */
        div.stButton > button {{
            width: 100%;
            height: 100px;
            font-size: 18px;
            font-weight: bold;
            border-radius: 15px;
            background-color: rgba(255, 255, 255, 0.95);
            color: #004d99;
            border: 1px solid #ddd;
            box-shadow: 0 2px 5px rgba(0,0,0,0.05);
            margin-bottom: 5px;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            line-height: 1.4;
        }}
        div.stButton > button:active, div.stButton > button:hover {{
            border: 1px solid #004d99;
            background-color: #f0f7ff;
        }}
        #MainMenu {{visibility: hidden;}}
        footer {{visibility: hidden;}}
        </style>
        """, unsafe_allow_html=True)

# 執行設計
set_design('BG.JPG')

# 2. 頁面狀態管理
if 'page' not in st.session_state:
    st.session_state.page = 'home'

# --- 主程式邏輯 ---

# A. 主選單頁面 (Home)
if st.session_state.page == 'home':
    # 顯示主視覺標題圖
    title_img = get_base64("image_44758d.png")
    if title_img:
        st.markdown(
            f'<div style="text-align: center;"><img src="data:image/png;base64,{title_img}" style="max-width: 85%; height: auto; margin-bottom: 20px;"></div>',
            unsafe_allow_html=True
        )
    
    # 建立 2 欄位按鈕 (仿照你的排版需求)
    col1, col2 = st.columns(2, gap="small")
    
    with col1:
        if st.button("📅\n年會流程", key="m1"):
            st.session_state.page = 'schedule'
            st.rerun()
        if st.button("🧩\n記憶拼圖\n分組名單", key="m3"):
            st.session_state.page = 'group'
            st.rerun()
        if st.button("🏆\n晚會\n得獎名單", key="m5"):
            st.session_state.page = 'awards'
            st.rerun()
            
    with col2:
        if st.button("📂\n3490扶青社\n社務資料", key="m2"):
            st.session_state.page = 'data'
            st.rerun()
        if st.button("🍽️\n晚會桌次表", key="m4"):
            st.session_state.page = 'table'
            st.rerun()
        if st.button("🤝\n贊助商資料", key="m6"):
            st.session_state.page = 'sponsor'
            st.rerun()

# B. 子頁面 (內容區)
else:
    # 頂部單一返回按鈕
    if st.button("⬅️ 返回主選單", use_container_width=True):
        st.session_state.page = 'home'
        st.rerun()
    
    st.markdown('<div class="content-card">', unsafe_allow_html=True)
    
    # --- 1. 年會流程 (PyCon 分頁風格) ---
    if st.session_state.page == 'schedule':
        st.subheader("典禮議程")
        t1, t2 = st.tabs(["05月02日 (六)", "05月03日 (日)"])
        
        with t1:
            st.info("💡 當日服裝：地區服 / 晚宴：復古服裝")
            df1 = pd.DataFrame([
                ["13:00 - 13:30", "行李寄放 & 註冊聯誼", "C棟1樓金鳳廳/2樓國際廳"],
                ["13:30 - 14:00", "歡迎扶輪長輩及 D2700", "C棟2樓國際廳"],
                ["14:00 - 17:00", "記憶拼圖活動", "C棟2樓國際廳"],
                ["17:00 - 17:30", "Check in", "-"],
                ["17:30 - 19:00", "晚宴", "A棟3樓富貴廳"],
                ["19:00 - 21:00", "DISCO大舞廳", "C棟1樓金龍廳"],
                ["21:00 - 22:30", "聯誼會後會", "C棟1樓金龍廳"]
            ], columns=["時間", "流程內容", "地點"])
            st.table(df1)
            
        with t2:
            st.info("💡 當日服裝：正式服裝")
            df2 = pd.DataFrame([
                ["09:00 - 09:30", "註冊聯誼 + 退房", "早餐:B棟1樓波根第"],
                ["09:30 - 12:30", "第三十六屆年會典禮", "C棟2樓國際廳"],
                ["12:30 - ", "歡送 D2700 地區 & 場復", "-"]
            ], columns=["時間", "流程內容", "地點"])
            st.table(df2)

    # --- 2. 社務資料 ---
    elif st.session_state.page == 'data':
        st.subheader("📂 3490 扶青社社務資料")
        st.write("資料上傳中...")

    # --- 3. 分組名單 ---
    elif st.session_state.page == 'group':
        st.subheader("🧩 記憶拼圖分組名單")
        st.write("請輸入您的姓名進行查詢")
        search = st.text_input("姓名：")
        if search: st.success(f"正在為您查詢「{search}」的分組...")

    # --- 4. 晚會桌次 ---
    elif st.session_state.page == 'table':
        st.subheader("🍽️ 晚會桌次表")
        st.write("請對應您的社別入座。")

    # --- 5. 得獎名單 ---
    elif st.session_state.page == 'awards':
        st.subheader("🏆 晚會得獎名單")
        st.balloons()
        st.write("恭喜所有得獎社青！")

    # --- 6. 贊助商 ---
    elif st.session_state.page == 'sponsor':
        st.subheader("🤝 贊助商資料")
        st.write("特別感謝以下贊助夥伴...")

    st.markdown('</div>', unsafe_allow_html=True)
