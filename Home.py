import streamlit as st

st.set_page_config(page_title="About Me", page_icon="👋", layout="wide")

# sidebar
with st.sidebar:
    st.title("🧭 Page Navigation")
    st.page_link("Home.py", label="🏠 About Me (Home)", disabled=True)
    st.page_link("pages/1_Skills_Hobbies.py", label="💻 Skills & Message Board")
    st.page_link("pages/2_Gallery_Download.py", label="📸 Gallery & BGM")

# home content
st.title("👋 Personal Profile — Fu Yuanxin")
st.divider()

col1, col2 = st.columns([1, 2])
with col1:
    st.image("photo2.jpg", use_column_width=True, caption="My profile photo")
with col2:
    st.header("Basic Information")
    st.write("""
    - Full Name: Fu Yuanxin (Alison)
    - Major: Data Science and Artificial Intelligence
    - Grade: Freshman (Year 1)
    - Character: Friendly, sincere, proactive and eager to learn.
    """)

# Language select
st.subheader("🌐 Language Select")
lang = st.selectbox("Select Display Language", ["English", "中文"])
st.info(f"Current selected language: {lang}")

st.divider()
st.caption("Jump to other pages via the left sidebar menu")
