import streamlit as st

# 1. 網頁配置
st.set_page_config(page_title="3490地區年會", layout="wide")

# 2. 強制 2 欄併排的 CSS 樣式
st.markdown("""
    <style>
    /* 隱藏原生按鈕，只保留我們自定義的樣式 */
    .main-container {
        width: 100%;
        max-width: 500px;
        margin: auto;
    }
    .custom-table {
        width: 100%;
        border-collapse: separate;
        border-spacing: 8px; /* 按鈕之間的間距 */
    }
    .custom-table td {
        width: 50%;
    }
    .nav-button {
        display: flex;
        align-items: center;
        justify-content: center;
        background-color: #ffffff;
        border: 2px solid #004d99;
        border-radius: 12px;
        height: 85px;
        color: #004d99;
        font-weight: bold;
        text-decoration: none;
        font-size: 16px;
        box-shadow: 0px 2px 4px rgba(0,0,0,0.1);
        text-align: center;
        line-height: 1.2;
    }
    .nav-button:active {
        background-color: #004d99;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. 頁面狀態管理
if 'page' not in st.session_state:
    st.session_state.page = 'home'

# --- 處理點擊事件 ---
# 因為 HTML 按鈕無法直接觸發 Python，我們用 Streamlit 原生 button 放在裡面
# 但為了強制併排，我們使用極簡化的 columns 並限制寬度

# A. 主選單頁面
if st.session_state.page == 'home':
    st.markdown("<h2 style='text-align: center;'>🧩 第 36 屆地區年會</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>時光迴響，記憶約定</p>", unsafe_allow_html=True)

    # 這是核心技巧：使用對齊容器
    st.write("---")
    
    # 這裡我們用 Python 手動計算 2 欄，並用兩兩一組的方式強制呈現
    # 為了防止跳行，我們將每一個 row 都寫死在同一個容器裡
    
    col1, col2 = st.columns(2, gap="small")
    
    with col1:
        if st.button("📅 年會流程", key="b1", use_container_width=True):
            st.session_state.page = 'page1'
            st.rerun()
        if st.button("🧩 分組名單", key="b3", use_container_width=True):
            st.session_state.page = 'page3'
            st.rerun()
        if st.button("🏆 得獎名單", key="b5", use_container_width=True):
            st.session_state.page = 'page5'
            st.rerun()
            
    with col2:
        if st.button("📂 社務資料", key="b2", use_container_width=True):
            st.session_state.page = 'page2'
            st.rerun()
        if st.button("🍽️ 晚會桌次", key="b4", use_container_width=True):
            st.session_state.page = 'page4'
            st.rerun()
        if st.button("🤝 贊助商資料", key="b6", use_container_width=True):
            st.session_state.page = 'page6'
            st.rerun()

# B. 子頁面內容 (iframe 效果)
else:
    # 頂部固定返回按鈕
    if st.button("⬅️ 返回主選單", use_container_width=True):
        st.session_state.page = 'home'
        st.rerun()
        
    st.divider()

    # 內容根據頁面切換
    if st.session_state.page == 'page1':
        st.subheader("📅 年會流程")
        st.write("這裡是詳細流程...")
    elif st.session_state.page == 'page2':
        st.subheader("📂 社務資料")
    elif st.session_state.page == 'page3':
        st.subheader("🧩 分組名單")
        st.text_input("搜尋姓名")
    elif st.session_state.page == 'page4':
        st.subheader("🍽️ 晚會桌次表")
    elif st.session_state.page == 'page5':
        st.subheader("🏆 得獎名單")
    elif st.session_state.page == 'page6':
        st.subheader("🤝 贊助商資料")

    st.divider()
    if st.button("⬅️ 返回主選單 ", key="bottom_back"):
        st.session_state.page = 'home'
        st.rerun()
