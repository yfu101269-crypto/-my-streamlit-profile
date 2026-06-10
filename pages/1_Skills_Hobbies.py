# 放在每个分页最顶部 set_page_config 下方
lang = st.session_state.get("lang", "English")
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Skills & Message", page_icon="💻", layout="wide")

# sidebar
with st.sidebar:
    st.title("🧭 Page Navigation")
    st.page_link("Home.py", label="🏠 Back to About Me")
    st.page_link("pages/1_Skills_Hobbies.py", label="💻 Skills & Message Board", disabled=True)
    st.page_link("pages/2_Gallery_Download.py", label="📸 Gallery & BGM")

st.title("💻 Skills & Hobbies Interactive Area")
st.divider()

# 1. skills
st.header("My Learning Skills")
skill_data = {
    "Skill Name": ["Python", "Data Visualization", "Streamlit", "Psychology"],
    "Proficiency": ["Intermediate", "Basic", "Basic", "Hobby Learner"]
}
skill_df = pd.DataFrame(skill_data)
st.table(skill_df)

# 2. hobbies more select
st.header("My Favorite Hobbies")
hobby_list = ["Animals", "Music", "Psychology", "Badminton", "Cycling", "Food"]
selected_hobby = st.multiselect("Pick your favorite hobby same as me", hobby_list, ["Animals", "Music"])
if selected_hobby:
    st.success(f"Great! We share these hobbies: {', '.join(selected_hobby)}")
else:
    st.warning("Please select at least one hobby option")

# 3. leave a message
st.header("Leave A Message To Me")
input_name = st.text_input("Your Name")
input_msg = st.text_area("Write your message here")
submit_btn = st.button("Submit Message")
if submit_btn:
    if input_name and input_msg:
        st.success(f"Thanks {input_name}! Your message has been received successfully.")
    else:
        st.error("Warning: Please fill your name and complete message before submit!")
