import streamlit as st

# 1. 網頁配置
st.set_page_config(page_title="3490地區年會DS", layout="wide")

# 2. 強制 2 欄排版的 CSS
st.markdown("""
    <style>
    /* 建立自定義矩陣按鈕樣式 */
    .grid-container {
        display: grid;
        grid-template-columns: repeat(2, 1fr); /* 強制每列 2 個 */
        gap: 10px;
        padding: 10px;
    }
    .grid-item {
        background-color: #f8f9fa;
        border: 2px solid #004d99;
        border-radius: 15px;
        height: 120px;
        display: flex;
        align-items: center;
        justify-content: center;
        text-align: center;
        text-decoration: none;
        color: #004d99;
        font-size: 18px;
        font-weight: bold;
        transition: 0.3s;
    }
    .grid-item:active {
        background-color: #004d99;
        color: white;
        transform: scale(0.95);
    }
    </style>
    """, unsafe_allow_html=True)

# 3. 頁面狀態管理
if 'page' not in st.session_state:
    st.session_state.page = 'home'

# --- 主程式邏輯 ---

# A. 主選單 (強制 2x3 佈局)
if st.session_state.page == 'home':
    st.markdown("<h2 style='text-align: center;'>🧩 第 36 屆地區年會</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>時光迴響，記憶約定</p>", unsafe_allow_html=True)

    # 使用 HTML 建立按鈕矩陣
    # 注意：這裡我們使用 st.button 的原生行為，但包在一個寬度受限的容器裡
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("📅\n年會流程", key="btn1"):
            st.session_state.page = 'page1'
            st.rerun()
        if st.button("🧩\n分組名單", key="btn3"):
            st.session_state.page = 'page3'
            st.rerun()
        if st.button("🏆\n得獎名單", key="btn5"):
            st.session_state.page = 'page5'
            st.rerun()
            
    with col2:
        if st.button("📂\n社務資料", key="btn2"):
            st.session_state.page = 'page2'
            st.rerun()
        if st.button("🍽️\n晚會桌次", key="btn4"):
            st.session_state.page = 'page4'
            st.rerun()
        if st.button("🤝\n贊助商", key="btn6"):
            st.session_state.page = 'page6'
            st.rerun()

# B. 子頁面內容 (iframe 模式，有返回鍵)
else:
    if st.button("⬅️ 返回主選單"):
        st.session_state.page = 'home'
        st.rerun()
        
    st.divider()

    pages = {
        'page1': ("📅 年會流程", "流程內容加載中..."),
        'page2': ("📂 社務資料", "3490 地區資料庫..."),
        'page3': ("🧩 分組名單", "請輸入姓名查詢..."),
        'page4': ("🍽️ 晚會桌次", "晚會桌次圖表..."),
        'page5': ("🏆 得獎名單", "恭喜獲獎社友！"),
        'page6': ("🤝 贊助商", "感謝贊助商支持...")
    }
    
    title, content = pages[st.session_state.page]
    st.header(title)
    st.write(content)

    # 如果是分組名單，可以多加一個搜尋框
    if st.session_state.page == 'page3':
        st.text_input("快速搜尋")

    st.divider()
    if st.button("⬅️ 返回主選單 ", key="back_bottom"):
        st.session_state.page = 'home'
        st.rerun()
