import  streamlit as st
import pandas as pd
st.set_page_config(
    page_title="streamlit入门",
    page_icon="😊",
    #布局
    layout="centered",
    #控制的是侧边栏的状态
    initial_sidebar_state ="auto",
    menu_items={}
)
st.title("streamlit入门演示")
st.header("streamlit入门演示")
st.subheader("streamlit二级标题")

#设置页面的配置项

#段落文字
st.write("如果你有具体的想要实现的功能（比如“我想自动下载某网站的图片”或“我想合并多个Excel文件”），请告诉我，我可以为你提供更针对性的代码示例！")
#表格
student_data={
    "姓名":["王林","李李","北洛"],
    "学号":["20000","30000","4000"],
    "语文":[99,99,99],
    "数学":[88,88,88],
    "英语":[77,77,77]
}
st.table(student_data)
#输入框
name=st.text_input("请输入姓名")
st.write(f"您输入的姓名为:{name}")

password=st.text_input("请输入密码")
st.write(f"您输入的密码为:{password}")

