import streamlit as st
import pandas as pd

# 1. 網頁配置：啟用寬螢幕模式與標題
st.set_page_config(page_title="3490地區年會資訊站", layout="wide")

# 2. 自定義 CSS：美化按鈕，使其更有質感且高度一致
st.markdown("""
    <style>
    div.stButton > button {
        width: 100%;
        height: 80px;
        font-size: 18px;
        font-weight: bold;
        border-radius: 12px;
        margin-bottom: 10px;
        background-color: #f8f9fa;
        border: 2px solid #004d99;
        color: #004d99;
    }
    div.stButton > button:hover {
        background-color: #004d99;
        color: white;
    }
    .main-title {
        text-align: center;
        color: #004d99;
        margin-bottom: 30px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. 初始化頁面狀態 (Session State)
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'home'

# --- 定義返回功能 ---
def go_home():
    st.session_state.current_page = 'home'

# --- 主程式邏輯 ---

# A. 主選單頁面 (每兩個按鈕一排)
if st.session_state.current_page == 'home':
    st.markdown("<h1 class='main-title'>🧩 第 36 屆地區年會：時光迴響，記憶約定</h1>", unsafe_allow_html=True)
    
    # 建立兩列的佈局 (RWD: 每列兩個按鈕)
    row1_col1, row1_col2 = st.columns(2)
    row2_col1, row2_col2 = st.columns(2)
    row3_col1, row3_col2 = st.columns(2)

    with row1_col1:
        if st.button("📅 1. 年會流程"):
            st.session_state.current_page = 'page1'
            st.rerun()
    with row1_col2:
        if st.button("📂 2. 3490 社務資料"):
            st.session_state.current_page = 'page2'
            st.rerun()
    
    with row2_col1:
        if st.button("🧩 3. 記憶拼圖分組名單"):
            st.session_state.current_page = 'page3'
            st.rerun()
    with row2_col2:
        if st.button("🍽️ 4. 晚會桌次表"):
            st.session_state.current_page = 'page4'
            st.rerun()
            
    with row3_col1:
        if st.button("🏆 5. 晚會得獎名單"):
            st.session_state.current_page = 'page5'
            st.rerun()
    with row3_col2:
        if st.button("🤝 6. 贊助商資料"):
            st.session_state.current_page = 'page6'
            st.rerun()

# B. 各個子頁面內容 (模擬 iframe 效果)
else:
    # 頂部導覽：放一個顯眼的返回按鈕，避免使用者往下滑
    st.button("⬅️ 返回主選單", on_click=go_home)
    st.divider()

    if st.session_state.current_page == 'page1':
        st.header("📅 年會流程")
        st.info("這裡是 5 月份地區年會的詳細時間表。")
        # 範例表格
        st.table({"時間": ["09:00", "12:00", "18:00"], "內容": ["開幕", "午宴", "晚會"]})

    elif st.session_state.current_page == 'page2':
        st.header("📂 3490 扶青社社務資料")
        st.write("點擊下方連結查看最新社務公告。")
        st.link_button("前往雲端資料夾", "https://github.com")

    elif st.session_state.current_page == 'page3':
        st.header("🧩 記憶拼圖分組名單")
        name = st.text_input("輸入姓名快速查詢")
        st.write("目前顯示所有組別...")

    elif st.session_state.current_page == 'page4':
        st.header("🍽️ 晚會桌次表")
        st.warning("晚會地點：[請輸入地點]")
        # 這裡可以放桌次圖或搜尋框

    elif st.session_state.current_page == 'page5':
        st.header("🏆 晚會得獎名單")
        st.balloons()
        st.success("恭喜以下獲獎社友！")

    elif st.session_state.current_page == 'page6':
        st.header("🤝 贊助商資料")
        st.write("感謝以下贊助夥伴...")

    # 底部也放一個返回按鈕，方便閱讀完後直接返回
    st.divider()
    st.button("⬅️ 返回主選單 ", key="bottom_back", on_click=go_home)
