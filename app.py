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

# --- 設定網頁整體樣式 (背景與按鈕) ---
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
            background-color: rgba(255, 255, 255, 0.88);
            padding: 25px;
            border-radius: 15px;
            border: 1px solid #eee;
            color: #1f1f1f;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        }}
        /* 手機版 2 欄按鈕樣式 */
        div.stButton > button {{
            width: 100%;
            height: 95px;
            font-size: 18px;
            font-weight: bold;
            border-radius: 15px;
            background-color: rgba(255, 255, 255, 0.95);
            color: #004d99;
            border: 2px solid #004d99;
            margin-bottom: 8px;
            white-space: pre-wrap; /* 允許換行顯示 emoji */
        }}
        div.stButton > button:active, div.stButton > button:hover {{
            background-color: #004d99 !important;
            color: white !important;
            border: 2px solid #004d99;
        }}
        #MainMenu {{visibility: hidden;}}
        footer {{visibility: hidden;}}
        </style>
        """, unsafe_allow_html=True)

# 執行樣式設定
set_design('BG.JPG')

# 2. 頁面狀態管理
if 'page' not in st.session_state:
    st.session_state.page = 'home'

# --- 主程式邏輯 ---

# A. 主選單頁面
if st.session_state.page == 'home':
    # 顯示淨化後的標題圖
    title_img = get_base64("image_44758d.png")
    if title_img:
        st.markdown(
            f"""
            <div style="text-align: center;">
                <img src="data:image/png;base64,{title_img}" 
                     style="max-width: 80%; height: auto; margin: 10px auto 30px auto; display: block;">
            </div>
            """, unsafe_allow_html=True
        )
    else:
        st.markdown("<h2 style='text-align: center; color: #004d99;'>第 36 屆地區年會</h2>", unsafe_allow_html=True)

    # 強制 2 欄佈局
    col1, col2 = st.columns(2, gap="small")
    
    with col1:
        if st.button("📅\n年會流程", key="b1", use_container_width=True):
            st.session_state.page = 'schedule'
            st.rerun()
        if st.button("🧩\n分組名單", key="b3", use_container_width=True):
            st.session_state.page = 'group'
            st.rerun()
        if st.button("🏆\n得獎名單", key="b5", use_container_width=True):
            st.session_state.page = 'awards'
            st.rerun()
            
    with col2:
        if st.button("📂\n社務資料", key="b2", use_container_width=True):
            st.session_state.page = 'data'
            st.rerun()
        if st.button("🍽️\n晚會桌次", key="b4", use_container_width=True):
            st.session_state.page = 'table'
            st.rerun()
        if st.button("🤝\n贊助商", key="b6", use_container_width=True):
            st.session_state.page = 'sponsor'
            st.rerun()

# B. 子頁面內容
else:
    # 頂部單一返回按鈕
    if st.button("⬅️ 返回主選單", key="back_btn", use_container_width=True):
        st.session_state.page = 'home'
        st.rerun()
    
    st.markdown('<div class="content-card">', unsafe_allow_html=True)
    
    # 1. 年會流程
    if st.session_state.page == 'schedule':
        st.subheader("📅 典禮議程表")
        st.markdown("---")
        st.markdown("#### **05月02日 (六)**")
        df1 = pd.DataFrame({
            "時間": ["13:00-13:30", "13:30-14:00", "14:00-17:00", "17:00-17:30", "17:30-19:00", "19:00-21:00", "21:00-22:30"],
            "流程項目": ["行李寄放 & 註冊聯誼", "歡迎扶輪長輩及 D2700", "記憶拼圖活動 (地區服)", "Check in", "晚宴 (復古風)", "DISCO大舞廳", "聯誼會後會"],
            "地點": ["C棟1/2樓", "C棟2樓國際廳", "C棟2樓國際廳", "-", "A棟3樓富貴廳", "C棟1樓金龍廳", "C棟1樓金龍廳"]
        })
        st.table(df1)
        
        st.markdown("#### **05月03日 (日)**")
        df2 = pd.DataFrame({
            "時間": ["09:00-09:30", "09:30-12:30", "12:30-"],
            "流程項目": ["註冊聯誼 + 退房", "第三十六屆年會典禮 (正式)", "歡送 D2700 地區 & 場復"],
            "地點": ["B棟1樓西餐廳", "C棟2樓國際廳", "-"]
        })
        st.table(df2)

    # 2. 社務資料
    elif st.session_state.page == 'data':
        st.subheader("📂 3490 扶青社社務資料")
        st.info("社務資料上傳中，請稍後查詢。")

    # 3. 分組名單
    elif st.session_state.page == 'group':
        st.subheader("🧩 記憶拼圖分組查詢")
        name = st.text_input("輸入姓名搜尋：")
        if name:
            st.write(f"正在搜尋「{name}」的分組資訊...")

    # 4. 晚會桌次
    elif st.session_state.page == 'table':
        st.subheader("🍽️ 晚會桌次圖")
        st.write("請依照現場公告之桌次入座。")

    # 5. 得獎名單
    elif st.session_state.page == 'awards':
        st.subheader("🏆 晚會得獎名單")
        st.balloons()
        st.success("名單揭曉中，敬請期待！")

    # 6. 贊助商
    elif st.session_state.page == 'sponsor':
        st.subheader("🤝 贊助商資料")
        st.write("感謝各界贊助商鼎力支持。")

    st.markdown('</div>', unsafe_allow_html=True)
