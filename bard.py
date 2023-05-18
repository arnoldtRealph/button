import streamlit as st
from streamlit_lottie import st_lottie
import requests
import streamlit.components.v1 as components

st.set_page_config(page_title= "TECHSCI", layout= "wide")

#load lottie files
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
lottie_science = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_nzw3czxk.json")

# Web title
st.title(" Technical Sciences")
st.header("Resource Page")
st.subheader("This space is reserved for all Grade 12 Technical Sciences learners")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
         st.subheader("Follow the following instructions to save the files to your tablet:")
         st.subheader(":red[You must save the files to your tablet so that it is always available offline, so you don't need data once you have downloaded the files]")
         st.markdown("""
         - :green[**Click on the button below**]
         - :green[**Once you arive at the folder section, open the folder and select the file you want to download**]
         - :green[**Click on the three vertical dots right next to the file and select download**]
         - :green[**The files will now be stored on your tablet**]
            """)
         
         #CODE FOR THE BUTTON
button_html = '''
<style>
button {
  border-radius: .25rem;
  text-transform: uppercase;
  font-style: normal;
  font-weight: 400;
  padding-left: 25px;
  padding-right: 25px;
  color: #fff;
  -webkit-clip-path: polygon(0 0,0 0,100% 0,100% 0,100% calc(100% - 15px),calc(100% - 15px) 100%,15px 100%,0 100%);
  clip-path: polygon(0 0,0 0,100% 0,100% 0,100% calc(100% - 15px),calc(100% - 15px) 100%,15px 100%,0 100%);
  height: 50px;
  font-size: 0.8rem;
  line-height: 14px;
  letter-spacing: 1.2px;
  transition: .2s .1s;
  background-image: linear-gradient(90deg,#1c1c1c,#6220fb);
  border: 0 solid;
  overflow: hidden;
}

button:hover {
  cursor: pointer;
  transition: all .3s ease-in;
  padding-right: 30px;
  padding-left: 30px;
}
</style>
<button onclick="window.open('https://drive.google.com/drive/folders/1-OdRq6OwkDopuIZsSknbD9ipvRwFm1LJ?usp=share_link&utm_source=Google+Drive&utm_medium=Shared+link&utm_campaign=Grade+11+Streamlit&utm_id=G-QQREF8Y40R')" type="button">CLICK HERE</button>
'''

components.html(button_html)
    
with right_column:
    st_lottie(lottie_science, height = 350 , key="coding")

st.write("---")

st.write("Created by Mr Visagie @ Saul Damon High School :wave:")













