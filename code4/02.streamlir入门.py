import streamlit as st

#设置页面的配置项
st.set_page_config(
    page_title="Streamlit入门",
    page_icon=":🤖:",
    #布局
    layout="wide",
    #控制的是侧边栏的状态
    initial_sidebar_state="expanded",
    menu_items={}
)

# 大标题
st.title("Streamlist 入门演示")
st.header("Streamlist 一级标题")
st.subheader("Streamlist 二级标题")

#段落文字
st.write("原产地：美国加州，1960 年代由繁育者安・贝克培育，奠基母猫名为约瑟芬")
st.write("成熟周期：生长缓慢，3–4 岁才完全长成型，成年体型才算稳定")
st.write("体重：成年公猫 4.5–6.8 公斤，成年母猫 3.2–5.4 公斤")
st.write("身高：成年公猫 51–61 公分，成年母猫 46–57 公分")

#图片
# st.image("./resourse/msct.jpg")

#音频
# st.audio("./resourse/msct.mp3")

#Logo
# st.logo("resourse/logo.png")

#表格
student_data = {
    "姓名": ["张三", "李四", "王五"],
    "年龄": [18, 19, 20],
    "语文": [90, 80, 75],
    "数学": [85, 90, 88],
    "英语": [88, 92, 85]
}
st.table(student_data)

#输入框
name = st.text_input("请输入你的姓名")
st.write("你输入的姓名为:",name)

#密码输入框
password = st.text_input("请输入你的密码", type="password")
st.write(f"你输入的密码为:{password}")

#单选按钮
gender = st.radio("请输入您的性别为:",["男","女","未知"],index=2)
st.write(f"您的性别为:{gender}")
