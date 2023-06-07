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
lottie_science = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_Bh4I41.json")




st.success("Congratulations on receiving the tablet! May you effectively employ this valuable tool to further your educational achievements.")
# Web title
st.title(" Technical Sciences")
st.header("Resource Page")
st.subheader("_This space is reserved for all Grade 12 Technical Sciences learners_")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
         st.subheader("Please follow the instructions below to save the files to your tablet:")
         st.subheader(":blue[Make sure to save the files to your tablet so that you always have them offline. That way, you won't need data once you've downloaded the files.]")
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

with st.container():
    left_column, right_column = st.columns(2)

    with left_column:
        st.subheader("More resources from :green[**_Nambane Academy_**]")
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
        <button onclick="window.open('https://www.nambaneacademy.com')" type="button">CLICK HERE</button>
        '''

        components.html(button_html)

    with right_column:
            st.subheader("Question Papers and Memoranda :blue[**_Per Province_**]")
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
            <button onclick="window.open('https://onedrive.live.com/?authkey=%21ALfjqh56bwzceVA&id=BBDC32500678CC7D%213528&cid=BBDC32500678CC7D')" type="button">CLICK HERE</button>
            '''

            components.html(button_html)


st.write("---")

st.subheader("Created by Mr A.R Visagie @ Saul Damon High School :wave:")
with st.container():
            st.subheader("You can also visit my official website for :blue[**Technical Sciences**] by clicking the button below")
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
            <button onclick="window.open('https://visagiescience.com')" type="button">CLICK HERE</button>
            '''

            components.html(button_html)


















