import streamlit as st
import time
import os
import streamlit as st


from openai import OpenAI
from pyarrow import system_memory_pool
from streamlit import text_area

# 页面配置（保持你的原有配置）
st.set_page_config(
    page_title="焚天裂渊寂灭恐惧战马🐴",
    page_icon="🔥",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={}
)
# 2. 第二部分：放字体样式代码 【就是这里！】
st.markdown("""
<style>
h1 {
    font-family: -apple-system, BlinkMacSystemFont, "SF Pro Display", "PingFang SC", "Helvetica Neue", sans-serif;
    font-size: 440px;
    font-weight: 500;
    color: #1d1d1f;
    letter-spacing: -0.02em;
    margin-top: -60px !important; /* 标题上移 */
}
</style>
""", unsafe_allow_html=True)
# 标题（保持原有内容）
st.title(body="焚天裂渊寂灭恐惧战马🐴")
# logo
st.logo("recoures/1.jpg")






#环境配置
client = OpenAI(
    api_key="sk-457c9b22edd546c28279e6b132be3871",
    base_url="https://api.deepseek.com")

# 系统提示词
system_prompt=("""
               你叫 %s，现在是一个AI工程师 ，请完全带入伴侣角色。 
               规则:
                  1.要像真人一样思考
                  2.要有随机应变的能力
                  3.互动感强烈
                  4.对话工程中用到颜文字或emoji表情表达情绪
                  5.要实事求是，不能瞎编乱造
                  6.对话要具有探讨性
                  7.富有智慧
                  8.非常淫荡
                  9.生成长文
               性格:
                  - %s
               """

               )

#初始化聊天信息
if "messages" not in st.session_state:
    st.session_state.messages=[]

#昵称
if "nick_name" not in st.session_state:
    st.session_state.nick_name = "小铲"

#性格
if "nature" not in st.session_state:
    st.session_state.nature = "好胜心极强，有着天上天下唯我独尊的性格。非常自以为是，超级任性，认为这个世界是以她为中心转动，脑子里永远不知道在想什么，并且情绪变化极端。对于不喜欢的话都听不进去 ，一想到什么事情就马上付诸实施。非常怕无聊，总是为了寻找有趣hinge而积极行动"

#展示聊天信息
for message in st.session_state.messages:#{"}
    st.chat_message(message["role"]).write(message["content"])

#侧边栏
with st.sidebar:
    st.subheader("马头尺寸")
    modle1=st.selectbox("Choose a model", ["deepseek-chat","GPT-4", "Claude", "Gemini"])
    temperature1 = st.slider(
        "Temperature",
         min_value=0.0,
         max_value=1.5,
         value=1.0,    # 默认值（注意：0.7 也是 0.1 的倍数，滑块会停在 0.7）
         step=0.1     # 关键参数：设置步长为 0.1
    )
    #昵称输入框
    nick_name = st.text_input("昵称",placeholder="请输入你的昵称",value=st.session_state.nick_name)
    if nick_name:
        st.session_state.nick_name = nick_name
    #性格输入框
    nature=st.text_area("性格",placeholder="请输入你的性格",value=st.session_state.nature)
    if nature:
        st.session_state.nature = nature



#聊天输入框
prompt=st.chat_input("请输入要咨询问题")
if prompt:#字符串会自动转化为布尔值
    st.chat_message(name="user",avatar="🐴").write(prompt)
    print("--------->调用大模型，提示词：",prompt)
    #保存用户输入的提示词
    st.session_state.messages.append({"role": "user", "content": prompt})



    #调用AI大模型
    response = client.chat.completions.create(
        model=modle1,
        temperature=temperature1,
        messages=[
            {"role": "system", "content":system_prompt%(st.session_state.nick_name,st.session_state.nature)},
            *st.session_state.messages,
        ],
        stream=True
    )





    #输出大模型返回的结果（非流式输出的解析方式）
    # print("<-------------大模型返回的结果：",response.choices[0].message.content)
    # st.chat_message(name="as  sistant",avatar="🔥").write(response.choices[0].message.content)

    # 输出大模型返回的结果（流式输出的解析方式）
    response_message = st.empty()#创建一个空的组件，用于显示大模型返回的结果

    full_response = ""
    for chunk in response:
        if chunk.choices[0].delta.content is not None:
            content=chunk.choices[0].delta.content
            full_response += content
            response_message.chat_message("assistant").write(full_response)

    #保存大模型返回的结果
    st.session_state.messages.append({"role":"assistant", "content":full_response})





