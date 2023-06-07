import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as html

st.set_page_config(page_title="微信公众号Streamlit", page_icon="💖", layout="wide")

sysmenu = '''
<style>
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
'''
st.markdown(sysmenu, unsafe_allow_html=True)

with st.sidebar:
    choose = option_menu("公众号Streamlit", ["介绍", "图片/音乐/视频", "数据可视化", "翻译", "地理", "其他应用"],
                         icons=['house', 'file-earmark-music', 'bar-chart', 'translate', 'brightness-high'],
                         menu_icon="broadcast", default_index=0)

if choose == "介绍":
    col1, col2 = st.columns(2)
    with col1:
        st.image("个人二维码.jpg", caption="微信公众号Streamlit作者微信")
    with col2:
        st.image("公众号二维码.png", caption="微信公众号Streamlit二维码")
        st.write("微信公众号Streamlit由作者创建已由半年多。\n\n\n\n"
                 "主题就是为大家分享Python与Streamlit结合的各种案例，用于提高大家的办公效率。\n\n\n\n"
                 "一个人可以走的很快，一群人可以走的更远。\n\n\n"
                 "为了让大家一起进步，由此创建了一个微信讨论群，可以扫下方二维码添加作者微信\n\n\n"
                 "验证信息：我来自公众号Streamlit")

elif choose == "图片/音乐/视频":
    selecte1 = option_menu(None, ["图片", "音乐", "视频"],
                           icons=['house', 'cloud-upload', "list-task"],
                           menu_icon="cast", default_index=0, orientation="horizontal")
    if selecte1 == "图片":
        with st.container():
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.image("./图片/1.jpg")
            with col2:
                st.image("./图片/2.jpg")
            with col3:
                st.image("./图片/3.jpg")
            with col4:
                st.image("./图片/4.jpg")
        with st.container():
            st.image("./图片/5.jpg")
    elif selecte1 == "音乐":
        st.audio("./音乐/music.mp3")
    elif selecte1 == "视频":
        st.video("./视频/地震.mp4")

elif choose == "数据可视化":
    selecte2 = option_menu(None, ["Echarts", "Plotly", "Streamlit-apex-charts"],
                           icons=['house', 'cloud-upload', "list-task"],
                           menu_icon="cast", default_index=0, orientation="horizontal")
    if selecte2 == "Echarts":
        html.iframe("https://mp.weixin.qq.com/s/5VDGsnpgx8iF90aF7p1yMg")

    elif selecte2 == "Plotly":
        html.iframe("https://mp.weixin.qq.com/s/ckcDXhoRmxlxswOviQUbFg")

    elif selecte2 == "Streamlit-apex-charts":
        st.components.v1.iframe("https://mp.weixin.qq.com/s/Sm3UifwoxVKTsMD-rsyovA")

elif choose == "翻译":
    selecte3 = option_menu(None, ["单词翻译", "谷歌翻译"],
                           icons=['house', 'cloud-upload'],
                           menu_icon="cast", default_index=0, orientation="horizontal")
    if selecte3 == "单词翻译":
        html.iframe("https://mp.weixin.qq.com/s/6lYXgMLlkELETB4YAIScFQ")

    elif selecte3 == "谷歌翻译":
        html.iframe("https://mp.weixin.qq.com/s/8V72xwGWcdIk4G_d_pLPTQ")


elif choose == "地理":
    selecte4 = option_menu(None, ["地震数据", "KML", "Mapinfo TAB"],
                           icons=['house', 'cloud-upload', 'cloud-upload'],
                           menu_icon="cast", default_index=0, orientation="horizontal")

    if selecte4 == "地震数据":
        html.iframe("https://mp.weixin.qq.com/s/HwYQXotuyZAtecOY6SBYKw")

    elif selecte4 == "KML":
        html.iframe("https://mp.weixin.qq.com/s/-z3dLVE-K0ejB6Sye0EOhg")

    elif selecte4 == "Mapinfo TAB":
        html.iframe("https://mp.weixin.qq.com/s/kP731l40Rf61CTWfyqbQmg")


elif choose == "其他应用":
    selecte5 = option_menu(None, ["Javascript", "展示PPT", "嵌入PDF"],
                           icons=['house', 'cloud-upload', "list-task"],
                           menu_icon="cast", default_index=0, orientation="horizontal")

    if selecte5 == "Javascript":
        html.iframe("https://mp.weixin.qq.com/s/Sr4_IAK3pGWRLgjO51i8Mw")

    elif selecte5 == "展示PPT":
        html.iframe("https://mp.weixin.qq.com/s/i0VcKUHBCEHjoOYvoiGolQ")


    elif selecte5 == "嵌入PDF":
        html.iframe("https://mp.weixin.qq.com/s/W8DX74LZYdosDUXUIpoa1g")

