import streamlit as st
import folium
from streamlit_folium import st_folium
import requests

# 網頁基本設定
st.set_page_config(page_title="🇰🇷 首爾 8月炎之旅", page_icon="✈️", layout="centered")

# --- 🎨 深度自訂米色主題 (修正白色遮擋/看不清問題) ---
st.markdown("""
<style>
    /* 1. 強制將整個網頁底色設為米色 */
    .stApp {
        background-color: #FAF0E6 !important; 
    }
    
    /* 2. 強制所有主要文字顯示為深灰色，避免與淺底色衝突 */
    h1, h2, h3, h4, h5, h6, p, li, span, label {
        color: #333333 !important;
    }
    
    /* 3. 清除所有可能的預設白色容器底色 (例如頁面外框、區塊) */
    .stMainBlockContainer, .stDecoration, div[data-testid="stVerticalBlock"] {
        background-color: transparent !important;
    }

    /* 4. 優化頂部 Tabs 頁籤的顏色 */
    .stTabs [data-baseweb="tab-list"] {
        background-color: transparent !important;
        gap: 4px;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: #F5F5DC !important; /* 稍微深一點點的米色作分頁標籤 */
        border-radius: 6px 6px 0px 0px;
        color: #555555 !important;
    }
    .stTabs [aria-selected="true"] {
        background-color: #EEDC82 !important; /* 被選中的 Tab 顏色稍微加深 */
        color: #000000 !important;
        font-weight: bold !important;
    }

    /* 5. 修正下拉選單 (Selectbox) 與輸入框的底色，防止它變成死白 */
    div[data-baseweb="select"], div[data-baseweb="input"], .stSelectbox, .stNumberInput input {
        background-color: #F5F5DC !important;
        border: 1px solid #D2B48C !important;
        color: #333333 !important;
    }
    
    /* 6. 修正航班資訊等 Info 卡片區塊，不要用預設的亮藍色/白色背景 */
    .stAlert {
        background-color: #F5F5DC !important;
        border-left: 5px solid #D2B48C !important;
    }
    
    /* 7. 修正購物清單 Checkbox 文字顏色 */
    div[data-testid="stCheckbox"] p {
        color: #333333 !important;
    }
</style>
""", unsafe_allow_html=True)

# 頂部橫幅 - 維基百科穩定圖源
st.image("https://en.wikipedia.org/wiki/Special:FilePath/Seoul_Skyline_from_Namsan_Tower.jpg", caption="Seoul Trip 2026 🇰🇷", use_container_width=True)

st.title("🇰🇷 首爾 8月炎之旅｜🛍️")
st.caption("📅 8月17日 - 8月21日 ｜ ✈️ 香港快運 UO614 / UO615")

# 導覽頁籤 (Tabs)
tab1, tab2, tab3, tab4, tab5 = st.tabs(["🗓️ 每日行程", "🗺️ 行程地圖", "✈️ 航班/住宿", "💱 即時匯率", "🛒 購物清單"])

# --- Tab 1: 每日行程 ---
with tab1:
    day = st.selectbox("選擇日期：", [
        "Day 1 - 8/17 (一) : 合井，弘大，延南洞",
        "Day 2 - 8/18 (二) : 聖水洞",
        "Day 3 - 8/19 (三) : 明洞，東大門",
        "Day 4 - 8/20 (四) : 奉恩寺，星空圖書館",
        "Day 5 - 8/21 (五) : 昌信洞玩具街，弘大"
    ])
    
    st.markdown("---")
    if "Day 1" in day:
        st.subheader("📍 Day 1: 合井，弘大，延南洞")
        st.write("**首爾弘大清單來了🥳**")
        st.markdown("""
        * **🍳 早餐**：[Hippo (點擊開啟地圖)](https://www.google.com/maps/search/?api=1&query=Hippo+Cafe+Yeonnam)
        * **🥩 午餐**：[吃草的豬 (點擊開啟地圖)](https://www.google.com/maps/search/?api=1&query=풀뜯는돼지+Hongdae)
        * **🐟 晚餐**：[風川鰻魚 (點擊開啟地圖)](https://www.google.com/maps/search/?api=1&query=風川鰻魚+Hongdae)
        """)
    elif "Day 2" in day:
        st.subheader("📍 Day 2: 聖水洞")
        st.write("**2026最新｜首爾聖水一日遊攻略**")
        st.markdown("""
        * **🍜 早餐**：[朝朝刀削麵 (點擊開啟地圖)](https://www.google.com/maps/search/?api=1&query=조조칼국수+Seongsu)
        * **🍽️ 午餐**：*(待定)*
        * **🦪 晚餐**：[贝壳Do (點擊開啟地圖)](https://www.google.com/maps/search/?api=1&query=贝壳Do+Seongsu)
        """)
    elif "Day 3" in day:
        st.subheader("📍 Day 3: 明洞，東大門")
        st.write("**明洞**")
        st.markdown("""
        * **🥣 早餐**：[鮑魚粥](https://www.google.com/maps/search/?api=1&query=明洞+鮑魚粥)
        * **🦀 午餐**：[醬油蟹](https://www.google.com/maps/search/?api=1&query=明洞+醬油蟹)
        * **🥩 晚餐**：[燒肉](https://www.google.com/maps/search/?api=1&query=明洞+燒肉)
        """)
        st.info("**東大門**\n參觀[設計廣場 DDP](https://www.google.com/maps/search/?api=1&query=Dongdaemun+Design+Plaza)、購物中心（Doota、Migliore等）。東大門市場／夜市晚上更熱鬧（很多店開很晚），街頭小吃豐富。")
    elif "Day 4" in day:
        st.subheader("📍 Day 4: 奉恩寺，星空圖書館")
        st.write("**奉恩寺 + 星空圖書館（江南COEX，傳統+現代）**\n兩地極近（步行可達）。")
        st.markdown("""
        * **⛩️ 上午（較涼快）：[奉恩寺](https://www.google.com/maps/search/?api=1&query=Bongeunsa+Temple)**
          地鐵2號線三成站或9號線奉恩寺站。開放約05:00–22:00（全年無休，免費）。巨大佛像、寧靜庭園與高樓對比強烈，適合1–1.5小時參訪。
        * **📚 中午後：[星空圖書館 @ COEX Mall](https://www.google.com/maps/search/?api=1&query=Starfield+Library+COEX)**
          開放約10:30–22:00，免費。巨型書架超好拍，可坐下休息看書。逛COEX商場（購物、吃飯、可選水族館）。
        """)
    elif "Day 5" in day:
        st.subheader("📍 Day 5: 昌信洞玩具街，弘大")
        st.markdown("""
        * **白天**：[昌信洞玩具街](https://www.google.com/maps/search/?api=1&query=Changsin-dong+Toy+Alley)，弘大
        * **🚨 返程時間軸**：
            * `(五) 22:00` 出發去機場
            * `(五) 23:00` 到機場
            * `(六) 02:35` 飛番香港
        """)

# --- Tab 2: 互動地圖 ---
with tab2:
    st.subheader("🗺️ 景點、餐廳與住宿總覽")
    m = folium.Map(location=[37.5500, 127.0000], zoom_start=12)
    
    # 🏨 住宿
    folium.Marker([37.5575, 126.9245], popup="🏨 民宿 (GS25 弘大公园店附近)", icon=folium.Icon(color="red", icon="home")).add_to(m)
    
    # 🍽️ Day 1 餐廳
    folium.Marker([37.5630, 126.9245], popup="🍳 Hippo (早餐)", icon=folium.Icon(color="orange", icon="cutlery")).add_to(m)
    folium.Marker([37.5550, 126.9220], popup="🥩 吃草的豬 (午餐)", icon=folium.Icon(color="orange", icon="cutlery")).add_to(m)
    folium.Marker([37.5615, 126.9240], popup="🐟 風川鰻魚 (晚餐)", icon=folium.Icon(color="orange", icon="cutlery")).add_to(m)

    # 🍽️ Day 2 餐廳
    folium.Marker([37.5450, 127.0550], popup="🍜 朝朝刀削麵", icon=folium.Icon(color="orange", icon="cutlery")).add_to(m)
    folium.Marker([37.5435, 127.0570], popup="🦪 贝壳Do", icon=folium.Icon(color="orange", icon="cutlery")).add_to(m)

    # 🍽️ Day 3 餐廳 & 景點
    folium.Marker([37.5636, 126.9827], popup="🦀 明洞商圈", icon=folium.Icon(color="orange", icon="cutlery")).add_to(m)
    folium.Marker([37.5683, 127.0097], popup="🏛️ 東大門 DDP", icon=folium.Icon(color="purple", icon="info-sign")).add_to(m)
    
    # 📍 Day 4 & 5 其他景點
    folium.Marker([37.5143, 127.0573], popup="📚 奉恩寺 / 星空圖書館", icon=folium.Icon(color="blue", icon="info-sign")).add_to(m)
    folium.Marker([37.5700, 127.0140], popup="🧸 昌信洞玩具街", icon=folium.Icon(color="blue", icon="info-sign")).add_to(m)
    
    st_folium(m, width="100%", height=450)
    st.caption("💡 提示：呢度可以一次過睇晒全部位置分佈。紅色係住宿、橙色係餐廳🍽️、藍/紫色係景點📍。")

# --- Tab 3: 航班與住宿 ---
with tab3:
    st.subheader("✈️ 航班資訊：香港快運航空")
    col1, col2 = st.columns(2)
    with col1:
        st.info("**8月17日（一）：去程 UO614**\n\n香港 T2｜HKG 21:00\n➡️ 仁川 T1｜ICN 01:40")
    with col2:
        st.info("**8月21日（五）：回程 UO615**\n\n仁川 T1｜ICN 02:35\n➡️ 香港 T1｜HKG 05:25")
    
    st.markdown("---")
    st.subheader("🏨 住宿")
    st.write("**首尔特别市 麻浦区 东桥洞 170-27**")
    st.code("170-27 Donggyo-dong, Mapo-gu, Seoul", language="text")
    st.caption("📌 GS25弘大公园店｜民宿")

# --- Tab 4: 即時匯率 ---
with tab4:
    st.subheader("💱 實時匯率換算 (HKD ↔ KRW)")
    try:
        response = requests.get("https://api.exchangerate-api.com/v4/latest/HKD")
        data = response.json()
        krw_rate = data['rates']['KRW']
        st.success(f"✅ 實時匯率：1 HKD = {krw_rate:.2f} KRW")
        
        krw_input = st.number_input("輸入韓元 (KRW)：", value=10000, step=1000)
        hkd_result = krw_input / krw_rate
        st.metric(label="折合港幣約", value=f"HKD ${hkd_result:.2f}")
    except:
        st.warning("⚠️ 暫時無法獲取即時匯率，使用預設參考匯率 (1 HKD ≈ 175 KRW)")
        krw_input = st.number_input("輸入韓元 (KRW)：", value=10000, step=1000)
        st.metric(label="折合港幣約", value=f"HKD ${(krw_input / 175):.2f}")

# --- Tab 5: 購物清單 ---
with tab5:
    st.subheader("🛒 購物清單")
    st.checkbox("Olive Young (化妝品、保養品)")
    st.checkbox("弘大服飾 / 配件")
    st.checkbox("東大門批發市場小物")
    st.checkbox("樂天超市零食伴手禮")
