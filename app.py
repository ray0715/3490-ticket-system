import streamlit as st

# 1. 網頁配置
st.set_page_config(page_title="3490地區年會資訊站", layout="wide")

# 2. 強制排版與按鈕美化的 CSS
st.markdown("""
    <style>
    /* 隱藏預設的按鈕邊框，讓自定義按鈕更美觀 */
    .stButton > button {
        width: 100%;
        height: 100px;
        border-radius: 10px;
        background-color: #f0f2f6;
        color: #004d99;
        font-weight: bold;
        font-size: 18px;
        border: 2px solid #004d99;
    }
    .stButton > button:hover {
        background-color: #004d99 !important;
        color: white !important;
    }
    /* 移除表格預設間距，確保併排美觀 */
    table {
        width: 100%;
        border-collapse: collapse;
    }
    td {
        width: 50%;
        padding: 5px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. 初始化頁面狀態
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'home'

# --- 返回主選單函數 ---
def go_back():
    st.session_state.current_page = 'home'

# --- 主程式邏輯 ---

# A. 主選單頁面 (使用表格邏輯強制併排)
if st.session_state.current_page == 'home':
    st.markdown("<h2 style='text-align: center;'>🧩 第 36 屆地區年會DDD</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>時光迴響，記憶約定</p>", unsafe_allow_html=True)

    # 這裡我們用 Streamlit 的 columns 但控制在非常窄的範圍內，
    # 或者直接使用 Button。在移動端強制 2x3 的最好方式是連續的 columns 呼叫：
    
    # 第一排
    c1, c2 = st.columns(2)
    with c1:
        if st.button("📅\n年會流程"):
            st.session_state.current_page = 'page1'
            st.rerun()
    with c2:
        if st.button("📂\n社務資料"):
            st.session_state.current_page = 'page2'
            st.rerun()

    # 第二排
    c3, c4 = st.columns(2)
    with c3:
        if st.button("🧩\n分組名單"):
            st.session_state.current_page = 'page3'
            st.rerun()
    with c4:
        if st.button("🍽️\n晚會桌次"):
            st.session_state.current_page = 'page4'
            st.rerun()

    # 第三排
    c5, c6 = st.columns(2)
    with c5:
        if st.button("🏆\n得獎名單"):
            st.session_state.current_page = 'page5'
            st.rerun()
    with c6:
        if st.button("🤝\n贊助商"):
            st.session_state.current_page = 'page6'
            st.rerun()

# B. 各個子頁面內容 (進入 iframe 模式)
else:
    # 頂部固定返回按鈕
    st.button("⬅️ 返回主選單", on_click=go_back)
    st.divider()

    if st.session_state.current_page == 'page1':
        st.subheader("📅 年會詳細流程")
        st.write("這裡是詳細的時間表內容...")
        
    elif st.session_state.current_page == 'page2':
        st.subheader("📂 3490 扶青社社務資料")
        st.info("資料上傳中...")

    elif st.session_state.current_page == 'page3':
        st.subheader("🧩 記憶拼圖分組名單")
        st.text_input("輸入姓名查詢")
        # 這裡未來可以放查詢結果表

    elif st.session_state.current_page == 'page4':
        st.subheader("🍽️ 晚會桌次表")
        st.write("請對號入座")

    elif st.session_state.current_page == 'page5':
        st.subheader("🏆 晚會得獎名單")
        st.balloons()

    elif st.session_state.current_page == 'page6':
        st.subheader("🤝 贊助商資料")
        st.write("感謝您的支持")

    st.divider()
    st.button("⬅️ 返回主選單 ", key="bottom_back", on_click=go_back)
