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

# --- 設定網頁整體樣式 (模仿 PyCon 質感與背景) ---
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
            background-color: rgba(255, 255, 255, 0.9);
            padding: 25px;
            border-radius: 15px;
            color: #1f1f1f;
            box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        }}
        /* 讓 Tabs 標籤看起來更有質感 */
        .stTabs [data-baseweb="tab-list"] {{
            gap: 10px;
        }}
        .stTabs [data-baseweb="tab"] {{
            height: 50px;
            background-color: rgba(255, 255, 255, 0.5);
            border-radius: 10px 10px 0px 0px;
            padding: 0px 20px;
            font-weight: bold;
        }}
        .stTabs [aria-selected="true"] {{
            background-color: #004d99 !important;
            color: white !important;
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
            white-space: pre-wrap;
        }}
        div.stButton > button:active, div.stButton > button:hover {{
            background-color: #004d99 !important;
            color: white !important;
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
    if st.button("⬅️ 返回主選單", key="back_btn", use_container_width=True):
        st.session_state.page = 'home'
        st.rerun()
    
    st.markdown('<div class="content-card">', unsafe_allow_html=True)
    
    # 1. 年會流程 (仿 PyCon 分頁設計)
    if st.session_state.page == 'schedule':
        st.subheader("📅 典禮議程")
        
        # 使用 Tabs 區分第一天與第二天
        tab1, tab2 = st.tabs(["5月2日 (Sat)", "5月3日 (Sun)"])
        
        with tab1:
            st.markdown("### **Day 1: 時光迴響**")
            df1 = pd.DataFrame({
                "時間": ["13:00-13:30", "13:30-14:00", "14:00-17:00", "17:00-17:30", "17:30-19:00", "19:00-21:00", "21:00-22:30"],
                "項目": ["行李寄放 & 註冊聯誼", "歡迎扶輪長輩及 D2700", "記憶拼圖活動 (地區服)", "Check in", "晚宴 (復古風)", "DISCO大舞廳", "聯誼會後會"],
                "地點": ["C棟1/2樓", "C棟2樓國際廳", "C棟2樓國際廳", "-", "A棟3樓富貴廳", "C棟1樓金龍廳", "C棟1樓金龍廳"]
            })
            st.dataframe(df1, use_container_width=True, hide_index=True)
        
        with tab2:
            st.markdown("### **Day 2: 記憶約定**")
            df2 = pd.DataFrame({
                "時間": ["09:00-09:30", "09:30-12:30", "12:30-"],
                "項目": ["註冊聯誼 + 退房", "第三十六屆年會典禮 (正式)", "歡送 D2700 地區 & 場復"],
                "地點": ["B棟1樓西餐廳", "C棟2樓國際廳", "-"]
            })
            st.dataframe(df2, use_container_width=True, hide_index=True)

    # 2~6 子頁面 (省略其餘邏輯，保持跟之前一樣)
    elif st.session_state.page == 'data':
        st.subheader("📂 3490 扶青社社務資料")
        st.info("資料整理中。")
    elif st.session_state.page == 'group':
        st.subheader("🧩 記憶拼圖分組查詢")
        name = st.text_input("搜尋姓名：")
    elif st.session_state.page == 'table':
        st.subheader("🍽️ 晚會桌次")
    elif st.session_state.page == 'awards':
        st.subheader("🏆 晚會得獎名單")
        st.balloons()
    elif st.session_state.page == 'sponsor':
        st.subheader("🤝 贊助商資料")

    st.markdown('</div>', unsafe_allow_html=True)
