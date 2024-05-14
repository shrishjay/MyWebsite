import streamlit as st
from PIL import Image
import requests
from streamlit_lottie import st_lottie

st.set_page_config(page_title="My Website", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# ---LOAD ASSETS
lottie_animation = load_lottieurl(
    'https://lottie.host/adf3f8cd-5449-4422-825a-069a201f9448/owSd28AUWi.json')
brain_image = Image.open('images/brain.png')
tree_image = Image.open('images/tree.png')

# ---HEADER---
with st.container():
    st.subheader("Hi, I am Shrishjay :wave:")
    st.title("I am a student studying Computer Science")
    st.write(
        "I am passionate about Data Science and I am interested in Cyber Security as well")
    st.write("[My github page >](https://github.com/shrishjay)")

# ---WHAT DO I DO---
with st.container():
    st.write("---")
    st.header("About Me")
    st.write("##")
    col1, col2 = st.columns(2)
    with col1:
        st.write('''
        - I am currently pursuing B.Tech in Computer Science Engineering
        - I am an aspiring Data Science student as well, pursuing BS Degree in Data Science and applications from IIT Madras
        - I am a Smart India Hackathon(2023) Grand Finalist
        - I love the concept of FOSS (Free and Open Source Software)
        - I am a Linux enthusiast, I use Arch BTW ;)
                ''')
    with col2:
        st_lottie(lottie_animation, height=300, key="coding")

# ---PROJECTS---
with st.container():
    st.write("---")
    col1, col2 = st.columns(2)
    st.write("##")
    with col1:
        st.header("My Projects")
        st.subheader("Plant Identification Model")
        st.write('''
        - This Machine Learning model is trained to identify different species of plants
        - This was a part of my Smart India Hackathon project
        - I have used multiple neural layers to train this model
        - This model is still under development and isn't super accurate
        - The github link is [here](https://github.com/shrishjay/Plant_Identification)
                ''')
    with col2:
        st.image(tree_image, width=200)

with st.container():
    st.write("---")
    col1, col2 = st.columns(2)
    st.write("##")
    with col1:
        st.subheader("Harmony - A mental health tracking application")
        st.write('''
        - This web application is used to track your mental health
        - We have created this application to help you out when you are having a bad day
        - This application keep record of your everyday feelings via a journal system
        - This journal is then sent to your email automatically
        - The github link is [here(https://github.com/shrishjay/Harmony)]
                ''')
    with col2:
        st.image(brain_image, width=200)
