# 放在每个分页最顶部 set_page_config 下方
lang = st.session_state.get("lang", "English")

import streamlit as st

st.set_page_config(page_title="Gallery & BGM", page_icon="📸", layout="wide")

# sidebar
with st.sidebar:
    st.title("🧭 Page Navigation")
    st.page_link("Home.py", label="🏠 Back to About Me")
    st.page_link("pages/1_Skills_Hobbies.py", label="💻 Skills & Message Board")
    st.page_link("pages/2_Gallery_Download.py", label="📸 Gallery & BGM", disabled=True)

st.title("📸 Life Gallery & Background Music")
st.divider()

# 1. daily life photo desplay
st.header("My Daily Life Photos")
col1, col2 = st.columns(2)
with col1:
    st.image("photo1.jpg", caption="Play with my cat", use_column_width=True)
with col2:
    st.image("photo3.jpg", caption="Badminton sport time", use_column_width=True)



# 3. TXT download
st.header("📥 Download My Profile Document")
profile_text = """
Fu Yuanxin (Alison)
Data Science and AI Freshman
Personality: Friendly, sincere, proactive
Hobbies: Animals, Music, Badminton
"""
st.download_button(
    label="Download Profile as TXT File",
    data=profile_text,
    file_name="Fu_Yuanxin_Profile.txt",
    mime="text/plain"
)

st.divider()
st.caption("All pages are built by Streamlit")
