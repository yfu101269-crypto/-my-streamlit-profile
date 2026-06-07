import streamlit as st

# Page config
st.set_page_config(
    page_title="Fu Yuanxin | Personal Profile",
    page_icon="🌟",
    layout="wide"
)

# Sidebar
st.sidebar.title("🧭 Navigation")
st.sidebar.success("Permanent Online Profile")

# Main title
st.title("👋 Personal Profile — Fu Yuanxin")
st.divider()

# 1. Name
st.header("👤 Name")
st.write("Fu Yuanxin (Alison)")

# 2. Major
st.header("🎓 Major")
st.write("Data Science and Artificial Intelligence")

# 3. Study status
st.header("🏫 Study Status")
st.write("Freshman (Year 1)")

# 4. Personality
st.header("😊 Personality")
st.write("Friendly, sincere, and proactive.")

# 5. Hobbies
st.header("🎯 Hobbies & Interests")
st.write("""
- Love animals
- Listening to music
- Psychology
- Food lover
""")

# 6. Sports
st.header("🏃 Sports")
st.write("""
- Badminton
- Cycling
""")

# 7. Tech & Study
st.header("💻 Tech & Learning")
st.write("""
- Focus: Data Science & AI
- Daily learning: Python programming
- Data visualization
- Hands‑on, self‑motivated, always learning new tech
""")

# 8. Life photos
st.header("📸 Life Moments")
col1, col2 = st.columns(2)
with col1:
    st.image("photo1.jpg", caption="With my cute cat", use_column_width=True)
with col2:
    st.image("photo2.jpg", caption="Sunflower day", use_column_width=True)

# 9. Sports photo
st.header("🏸 Sports")
st.image("photo3.jpg", caption="On the badminton court", use_column_width=True)

# 10. Full bio
st.header("📝 About Me")
st.write("""
I’m a first‑year student majoring in Data Science and Artificial Intelligence.
I study Python programming, data visualization, and related topics every day.
I’m hands‑on, self‑motivated, and always eager to learn new technologies.
I’m friendly and sincere to people around me.

In my free time, I love animals, listen to music, and learn about psychology.
I also enjoy playing badminton, cycling, and being outdoors.
I’m a food lover too.

I’m always positive and looking forward to growing together with others.
""")

st.divider()
st.caption("✅ Built with Streamlit · Permanent Online")
