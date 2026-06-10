# 第一步：先导入库（必须放最顶部）
import streamlit as st

# 第二步：页面配置
st.set_page_config(page_title="Gallery & BGM", page_icon="📸", layout="wide")

# 第三步：读取全局语言（放在set_page_config下方，顺序正确）
lang = st.session_state.get("lang", "English")

# 侧边栏导航
with st.sidebar:
    st.title("🧭 Page Navigation")
    st.page_link("Home.py", label="🏠 Back to About Me")
    st.page_link("pages/1_Skills_Hobbies.py", label="💻 Skills & Message Board")
    st.page_link("pages/2_Gallery_Download.py", label="📸 Gallery & BGM", disabled=True)

# 中英文文本切换逻辑
if lang == "中文":
    page_title = "📸 生活相册与个人档案下载"
    photo_header = "我的日常照片"
    pic1_caption = "和小猫玩耍"
    pic2_caption = "羽毛球运动时刻"
    download_header = "📥 下载我的个人档案文档"
    download_btn_text = "下载个人档案 TXT 文件"
    footer_tip = "所有页面均使用 Streamlit 搭建"
    profile_text_cn = """
付远鑫（Alison）
数据科学与人工智能专业大一新生
性格：友善真诚、积极上进
爱好：小动物、音乐、羽毛球
"""
else:
    page_title = "📸 Life Gallery & Background Music"
    photo_header = "My Daily Life Photos"
    pic1_caption = "Play with my cat"
    pic2_caption = "Badminton sport time"
    download_header = "📥 Download My Profile Document"
    download_btn_text = "Download Profile as TXT File"
    footer_tip = "All pages are built by Streamlit"
    profile_text_en = """
Fu Yuanxin (Alison)
Data Science and AI Freshman
Personality: Friendly, sincere, proactive
Hobbies: Animals, Music, Badminton
"""

# 根据语言选择对应档案文本
profile_text = profile_text_cn if lang == "中文" else profile_text_en

# 页面主体渲染
st.title(page_title)
st.divider()

# 1. 生活照片展示
st.header(photo_header)
col1, col2 = st.columns(2)
with col1:
    st.image("photo1.jpg", caption=pic1_caption, use_column_width=True)
with col2:
    st.image("photo3.jpg", caption=pic2_caption, use_column_width=True)

# 2. TXT档案下载
st.header(download_header)
st.download_button(
    label=download_btn_text,
    data=profile_text,
    file_name="Fu_Yuanxin_Profile.txt",
    mime="text/plain"
)

st.divider()
st.caption(footer_tip)
