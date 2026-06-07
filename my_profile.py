import streamlit as st
import pandas as pd

# 设置页面
st.set_page_config(
    page_title="Fu Yuanxin | Personal Profile",
    page_icon="🌟",
    layout="wide"
)

# 1. 定义中英文两套文本
text = {
    "en": {
        "lang_select": "Select Language",
        "nav_title": "Navigation",
        "nav_line1": "Permanent Online Profile",
        "nav_line2": "Use the sidebar to explore interactive features",
        "title": "👋 Personal Profile — Fu Yuanxin",
        "about_me": "About Me",
        "skills": "💻 Skills & Learning",
        "hobbies": "🎯 Hobbies & Interests",
        "hobbies_q": "What are your hobbies?",
        "message": "💬 Leave a Message",
        "name": "Your Name",
        "msg": "Your Message",
        "submit": "Submit Message",
        "download": "📥 Download My Profile",
        "download_btn": "Download as TXT",
        "photos": "📸 Life Moments",
        "footer": "✅ Built with Streamlit · Permanent Online"
    },
    "zh": {
        "lang_select": "选择语言",
        "nav_title": "导航栏",
        "nav_line1": "永久在线个人主页",
        "nav_line2": "使用侧边栏探索互动功能",
        "title": "👋 个人简介 — 付远鑫",
        "about_me": "关于我",
        "skills": "💻 技能与学习",
        "hobbies": "🎯 爱好与兴趣",
        "hobbies_q": "你的爱好是什么？",
        "message": "💬 留言区",
        "name": "你的姓名",
        "msg": "你的留言",
        "submit": "提交留言",
        "download": "📥 下载我的简介",
        "download_btn": "下载为 TXT 文件",
        "photos": "📸 生活瞬间",
        "footer": "✅ 使用 Streamlit 搭建 · 永久在线"
    }
}

# 2. 语言选择框（核心）
lang = st.selectbox(text["en"]["lang_select"], ["English", "中文"])
t = text["en"] if lang == "English" else text["zh"]

# 3. 侧边栏
with st.sidebar:
    st.title(t["nav_title"])
    st.success(t["nav_line1"])
    st.info(t["nav_line2"])

# 4. 主页面
st.title(t["title"])
st.divider()

# 基本信息
col1, col2 = st.columns([1, 2])
with col1:
    st.image("photo2.jpg", use_column_width=True, caption=t["about_me"])
with col2:
    st.header(t["about_me"])
    if lang == "English":
        st.write("""
        - **Name**: Fu Yuanxin (Alison)
        - **Major**: Data Science and Artificial Intelligence
        - **Study Status**: Freshman (Year 1)
        - **Personality**: Friendly, sincere, and proactive.
        """)
    else:
        st.write("""
        - **姓名**: 付远鑫 (Alison)
        - **专业**: 数据科学与人工智能
        - **在读阶段**: 大一新生
        - **性格**: 开朗真诚，积极上进。
        """)

# 技能表格
st.header(t["skills"])
if lang == "English":
    skills_data = {
        "Skill": ["Python", "Data Visualization", "Streamlit", "Psychology"],
        "Level": ["Intermediate", "Basic", "Basic", "Enthusiast"]
    }
else:
    skills_data = {
        "技能": ["Python", "数据可视化", "Streamlit", "心理学"],
        "水平": ["中等", "基础", "基础", "爱好者"]
    }
skills_df = pd.DataFrame(skills_data)
st.table(skills_df)

# 爱好选择
st.header(t["hobbies"])
if lang == "English":
    hobby_list = ["Animals", "Music", "Psychology", "Badminton", "Cycling", "Food"]
    success = "Great choices! Your selected hobbies: {}"
    warning = "Please select at least one hobby to continue"
else:
    hobby_list = ["小动物", "音乐", "心理学", "羽毛球", "骑行", "美食"]
    success = "很棒的选择！你选中的爱好：{}"
    warning = "请至少选择一项爱好"

hobbies = st.multiselect(t["hobbies_q"], hobby_list, hobby_list[:2])
if hobbies:
    st.success(success.format(", ".join(hobbies)))
else:
    st.warning(warning)

# 留言区
st.header(t["message"])
user_name = st.text_input(t["name"])
user_msg = st.text_area(t["msg"])
if st.button(t["submit"]):
    if user_name and user_msg:
        if lang == "English":
            st.success(f"Thank you, {user_name}! Your message has been received.")
        else:
            st.success(f"谢谢你，{user_name}！留言已提交。")
    else:
        if lang == "English":
            st.error("Please fill in both name and message before submitting")
        else:
            st.error("请完整填写姓名和留言后再提交")

# 下载
st.header(t["download"])
if lang == "English":
    download_text = """Fu Yuanxin (Alison)
Data Science and AI Freshman
Friendly, proactive, and eager to learn new technologies."""
else:
    download_text = """付远鑫（Alison）
数据科学与人工智能专业大一学生
性格开朗真诚，热爱学习新技术。"""

st.download_button(
    label=t["download_btn"],
    data=download_text,
    file_name="fu_yuanxin_profile.txt",
    mime="text/plain"
)

# 照片
st.header(t["photos"])
col1, col2 = st.columns(2)
with col1:
    st.image("photo1.jpg", use_column_width=True, caption="Cat" if lang == "English" else "猫咪")
with col2:
    st.image("photo3.jpg", use_column_width=True, caption="Badminton" if lang == "English" else "羽毛球")

# 页脚
st.divider()
st.caption(t["footer"])
