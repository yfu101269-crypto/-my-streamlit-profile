# 1. 先导入库（必须放在最顶部）
import streamlit as st
import pandas as pd

# 2. 页面配置
st.set_page_config(page_title="Skills & Message", page_icon="💻", layout="wide")

# 3. 再读取全局语言（放在set_page_config下方，顺序正确）
lang = st.session_state.get("lang", "English")

# 侧边栏导航
with st.sidebar:
    st.title("🧭 Page Navigation")
    st.page_link("Home.py", label="🏠 Back to About Me")
    st.page_link("pages/1_Skills_Hobbies.py", label="💻 Skills & Message Board", disabled=True)
    st.page_link("pages/2_Gallery_Download.py", label="📸 Gallery & BGM")

# 中英文文字区分
if lang == "中文":
    page_title = "💻 技能与爱好交互区"
    skill_header = "我的学习技能"
    hobby_header = "我喜爱的爱好"
    hobby_tip = "选择和我相同的爱好"
    success_tip = "太棒啦！我们有共同爱好："
    warn_tip = "请至少选择一项爱好"
    msg_header = "给我留言"
    name_input = "你的名字"
    msg_input = "在此写下留言"
    submit_btn_text = "提交留言"
    submit_success = "感谢你！留言已成功接收。"
    submit_error = "提示：填写姓名和完整留言后再提交！"
else:
    page_title = "💻 Skills & Hobbies Interactive Area"
    skill_header = "My Learning Skills"
    hobby_header = "My Favorite Hobbies"
    hobby_tip = "Pick your favorite hobby same as me"
    success_tip = "Great! We share these hobbies: "
    warn_tip = "Please select at least one hobby option"
    msg_header = "Leave A Message To Me"
    name_input = "Your Name"
    msg_input = "Write your message here"
    submit_btn_text = "Submit Message"
    submit_success = "Thanks! Your message has been received successfully."
    submit_error = "Warning: Please fill your name and complete message before submit!"

# 页面主体渲染
st.title(page_title)
st.divider()

# 1. 技能表格
st.header(skill_header)
skill_data = {
    "Skill Name": ["Python", "Data Visualization", "Streamlit", "Psychology"],
    "Proficiency": ["Intermediate", "Basic", "Basic", "Hobby Learner"]
}
skill_df = pd.DataFrame(skill_data)
st.table(skill_df)

# 2. 爱好多选
st.header(hobby_header)
hobby_list = ["Animals", "Music", "Psychology", "Badminton", "Cycling", "Food"]
selected_hobby = st.multiselect(hobby_tip, hobby_list, ["Animals", "Music"])
if selected_hobby:
    st.success(f"{success_tip}{', '.join(selected_hobby)}")
else:
    st.warning(warn_tip)

# 3. 留言板块
st.header(msg_header)
input_name = st.text_input(name_input)
input_msg = st.text_area(msg_input)
submit_btn = st.button(submit_btn_text)
if submit_btn:
    if input_name and input_msg:
        st.success(f"{submit_success} {input_name}!")
    else:
        st.error(submit_error)
