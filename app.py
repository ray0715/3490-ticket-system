import streamlit as st
import base64

# 1. 網頁配置 (放在最頂端)
st.set_page_config(page_title="3490地區年會", layout="wide")

# --- 背景圖處理函數 ---
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_png_as_page_bg(bin_file):
    try:
        bin_str = get_base64_of_bin_file(bin_file)
        page_bg_img = f'''
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{bin_str}");
            background-size: cover;
            background-attachment: fixed;
        }}
        /* 設定內容區塊背景稍微透明，確保文字清晰 */
        .main-block {{
            background-color: rgba(255, 255, 255, 0.7);
            padding: 20px;
            border-radius: 15px;
            color: #333333;
        }}
        /* 強制按鈕併排樣式 */
        div.stButton > button {{
            width: 100%;
            height: 90px;
            font-size: 18px;
            font-weight: bold;
            border-radius: 12px;
            background-color: rgba(255, 255, 255, 0.9);
            color: #004d99;
            border: 2px solid #004d99;
        }}
        </style>
        '''
        st.markdown(page_bg_img, unsafe_allow_html=True)
    except Exception as e:
        st.warning(f"背景圖加載失敗，請檢查檔名是否為 BG.JPG。錯誤原因: {e}")

# 執行背景設定
set_png_as_page_bg('BG.JPG')

# 2. 頁面狀態管理
if 'page' not in st.session_state:
    st.session_state.page = 'home'

# --- 主程式邏輯 ---

# A. 主選單 (強制併排版)
if st.session_state.page == 'home':
    st.markdown("<h2 style='text-align: center; color: #004d99;'>🧩 第 36 屆地區年會</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #555;'>時光迴響，記憶約定</p>", unsafe_allow_html=True)

    # 手機版強制併排的核心：使用兩欄佈局並搭配 use_container_width
    col1, col2 = st.columns(2, gap="small")
    
    with col1:
        if st.button("📅 年會流程", key="n1", use_container_width=True):
            st.session_state.page = 'p1'
            st.rerun()
        if st.button("🧩 分組名單", key="n3", use_container_width=True):
            st.session_state.page = 'p3'
            st.rerun()
        if st.button("🏆 得獎名單", key="n5", use_container_width=True):
            st.session_state.page = 'p5'
            st.rerun()
            
    with col2:
        if st.button("📂 社務資料", key="n2", use_container_width=True):
            st.session_state.page = 'p2'
            st.rerun()
        if st.button("🍽️ 晚會桌次", key="n4", use_container_width=True):
            st.session_state.page = 'p4'
            st.rerun()
        if st.button("🤝 贊助商資料", key="n6", use_container_width=True):
            st.session_state.page = 'p6'
            st.rerun()

# B. 子頁面 (點擊後直接覆蓋)
else:
    # 頂部返回按鈕
    if st.button("⬅️ 返回主選單", key="top_back", use_container_width=True):
        st.session_state.page = 'home'
        st.rerun()
    
    st.divider()
    
    # 內容容器
    with st.container():
        # 使用 markdown 包裝一個透明層讓文字好讀
        st.markdown('<div class="main-block">', unsafe_allow_html=True)
        
        if st.session_state.page == 'p1':
            st.header("📅 年會流程")
            st.write("這裡是詳細流程內容...")
        elif st.session_state.page == 'p2':
            st.header("📂 社務資料")
            st.write("3490 地區相關文件...")
        elif st.session_state.page == 'p3':
            st.header("🧩 分組名單")
            st.text_input("輸入姓名快速查詢")
        elif st.session_state.page == 'p4':
            st.header("🍽️ 晚會桌次表")
            st.write("請依照編號入座")
        elif st.session_state.page == 'p5':
            st.header("🏆 晚會得獎名單")
            st.write("恭喜得獎社友")
        elif st.session_state.page == 'p6':
            st.header("🤝 贊助商資料")
            st.write("感謝您的熱情贊助")
            
        st.markdown('</div>', unsafe_allow_html=True)

    st.divider()
    # 底部返回按鈕
    if st.button("⬅️ 返回主選單 ", key="back_bot", use_container_width=True):
        st.session_state.page = 'home'
        st.rerun()
