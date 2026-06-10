import streamlit as st

st.set_page_config(page_title="About Me", page_icon="👋", layout="wide")

# 侧边栏导航
with st.sidebar:
    st.title("🧭 Page Navigation")
    st.page_link("Home.py", label="🏠 About Me (Home)", disabled=True)
    st.page_link("pages/1_Skills_Hobbies.py", label="💻 Skills & Message Board")
    st.page_link("pages/2_Gallery_Download.py", label="📸 Gallery & BGM")

# ========== 关键语言选择代码（你现在缺失这段）==========
st.subheader("🌐 Language Select / 语言选择")
lang = st.selectbox("Select Display Language", ["English", "中文"])
st.session_state["lang"] = lang
# ======================================================

# 中英文文字区分
if lang == "中文":
    page_title = "👋 个人简介 — 付远鑫"
    info_header = "基础信息"
    info_content = """
- 姓名：付远鑫（Alison）
- 专业：数据科学与人工智能
- 年级：大一新生
- 性格：友善真诚，积极好学
"""
    pic_caption = "个人照片"
    bottom_tip = "通过左侧侧边栏菜单跳转其他页面"
else:
    page_title = "👋 Personal Profile — Fu Yuanxin"
    info_header = "Basic Information"
    info_content = """
- Full Name: Fu Yuanxin (Alison)
- Major: Data Science and Artificial Intelligence
- Grade: Freshman (Year 1)
- Character: Friendly, sincere, proactive and eager to learn.
"""
    pic_caption = "My profile photo"
    bottom_tip = "Jump to other pages via the left sidebar menu"

# 页面内容渲染
st.title(page_title)
st.divider()

col1, col2 = st.columns([1, 2])
with col1:
    st.image("photo2.jpg", use_column_width=True, caption=pic_caption)
with col2:
    st.header(info_header)
    st.write(info_content)

st.info(f"Current selected language / 当前选中语言：{lang}")
st.divider()
st.caption(bottom_tip)
