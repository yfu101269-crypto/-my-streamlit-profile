import streamlit as st
import pandas as pd

# set page
st.set_page_config(
    page_title="Fu Yuanxin | Personal Profile",
    page_icon="🌟",
    layout="wide"
)

# sidebar
with st.sidebar:
    st.title("🧭 Navigation")
    st.success("Permanent Online Profile")
    st.info("Use the sidebar to explore interactive features")

# personal title
st.title("👋 Personal Profile — Fu Yuanxin")
st.divider()

# 1. basic message
col1, col2 = st.columns([1, 2])
with col1:
    st.image("photo2.jpg", use_column_width=True, caption="My profile picture")
with col2:
    st.header("About Me")
    st.write("""
    - **Name**: Fu Yuanxin (Alison)
    - **Major**: Data Science and Artificial Intelligence
    - **Study Status**: Freshman (Year 1)
    - **Personality**: Friendly, sincere, and proactive.
    """)

# 2. skills
st.header("💻 Skills & Learning")
skills_data = {
    "Skill": ["Python", "Data Visualization", "Streamlit", "Psychology"],
    "Level": ["Intermediate", "Basic", "Basic", "Enthusiast"]
}
skills_df = pd.DataFrame(skills_data)
st.table(skills_df)

# 3. hobby select
st.header("🎯 Hobbies & Interests")
hobbies = st.multiselect(
    "What are your hobbies?",
    ["Animals", "Music", "Psychology", "Badminton", "Cycling", "Food"],
    ["Animals", "Music"]
)
if hobbies:
    st.success(f"Great choices! Your selected hobbies: {', '.join(hobbies)}")
else:
    st.warning("Please select at least one hobby to continue")

# 4. interactive input
st.header("💬 Leave a Message")
user_name = st.text_input("Your Name")
user_message = st.text_area("Your Message")
if st.button("Submit Message"):
    if user_name and user_message:
        st.success(f"Thank you, {user_name}! Your message has been received.")
    else:
        st.error("Please fill in both name and message before submitting")

# 5. Download My Profile
st.header("📥 Download My Profile")
profile_text = """
Fu Yuanxin (Alison)
Data Science and AI Freshman
Friendly, proactive, and eager to learn new technologies.
"""
st.download_button(
    label="Download as TXT",
    data=profile_text,
    file_name="fu_yuanxin_profile.txt",
    mime="text/plain"
)

# photo display
st.header("📸 Life Moments")
col1, col2 = st.columns(2)
with col1:
    st.image("photo1.jpg", caption="With my cute cat", use_column_width=True)
with col2:
    st.image("photo3.jpg", caption="On the badminton court", use_column_width=True)

# page end...
st.divider()
st.caption("✅ Built with Streamlit · Permanent Online")
