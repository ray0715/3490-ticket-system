import streamlit as st
import pandas as pd

# 1. 網頁基礎配置
st.set_page_config(
    page_title="3490地區年會資訊站",
    page_icon="🧩",
    layout="wide"
)

# 2. 自定義 CSS (增加按鈕美感與手機適配)
st.markdown("""
    <style>
    div.stButton > button {
        width: 100%;
        height: 100px;
        font-size: 20px;
        font-weight: bold;
        border-radius: 15px;
        border: 2px solid #004d99;
        background-color: #ffffff;
        color: #004d99;
        transition: all 0.3s;
    }
    div.stButton > button:hover {
        background-color: #004d99;
        color: #ffffff;
        transform: translateY(-5px);
    }
    .header-style {
        text-align: center;
        padding: 10px;
        color: #004d99;
    }
    </style>
    """, unsafe_allow_html=True)

# 標題區
st.markdown("<h1 class='header-style'>第 36 屆地區年會：時光迴響，記憶約定</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>District 3490 Rotaract Conference</p>", unsafe_allow_html=True)

# 3. 建立六個按鈕的 RWD 佈局
col1, col2, col3 = st.columns(3)
col4, col5, col6 = st.columns(3)

# 初始化 Session State 來切換頁面
if 'page' not in st.session_state:
    st.session_state.page = 'home'

with col1:
    if st.button("📅\n年會流程"): st.session_state.page = 'schedule'
with col2:
    if st.button("📂\n3490社務資料"): st.session_state.page = 'club_info'
with col3:
    if st.button("🧩\n記憶拼圖分組"): st.session_state.page = 'grouping'
with col4:
    if st.button("🍽️\n晚會桌次表"): st.session_state.page = 'tables'
with col5:
    if st.button("🏆\n晚會得獎名單"): st.session_state.page = 'winners'
with col6:
    if st.button("🤝\n贊助商資料"): st.session_state.page = 'sponsors'

st.divider()

# 4. 各功能頁面內容定義
if st.session_state.page == 'schedule':
    st.header("📅 年會流程")
    df = pd.DataFrame({
        "時間": ["09:00", "10:30", "13:30", "18:00"],
        "項目": ["註冊報到", "開幕典禮", "專題演講 / 議事", "記憶晚會"]
    })
    st.table(df)

elif st.session_state.page == 'club_info':
    st.header("📂 3490 扶青社社務資料")
    st.info("此區可放置各社年度計畫下載連結或地區公告。")
    # 範例：下載按鈕
    st.download_button("下載 3490 地區年度手冊", "這是檔案內容", file_name="D3490_Handbook.txt")

elif st.session_state.page == 'grouping':
    st.header("🧩 記憶拼圖分組名單")
    query = st.text_input("輸入姓名查詢分組：", placeholder="例如：阿曾")
    # 這裡可串接你的 Excel 或 CSV 資料
    st.write("請查閱下表或使用上方搜尋框。")
    st.dataframe({"姓名": ["阿曾", "小王"], "組別": ["A組", "B組"]}, use_container_width=True)

elif st.session_state.page == 'tables':
    st.header("🍽️ 晚會桌次表")
    st.image("https://via.placeholder.com/800x400?text=Table+Layout", caption="宴會廳桌次分布圖")
    search_table = st.text_input("輸入所屬社團查詢桌號：")
    st.write("新莊社：第 5 桌 / 泰山社：第 6 桌")

elif st.session_state.page == 'winners':
    st.header("🏆 晚會得獎名單")
    st.balloons()
    st.success("恭喜以下獲獎社團與個人！")
    st.write("🥇 年度卓越社團獎：XXX社")

elif st.session_state.page == 'sponsors':
    st.header("🤝 贊助商資料")
    st.write("感謝以下贊助夥伴對第 36 屆地區年會的支持：")
    # 這裡可以放贊助商 Logo 或連結
    c1, c2 = st.columns(2)
    c1.info("贊助商 A 公司")
    c2.info("贊助商 B 公司")

# 回首頁按鈕
if st.session_state.page != 'home':
    if st.button("⬅️ 返回主選單"):
        st.session_state.page = 'home'
        st.rerun()
