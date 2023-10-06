import streamlit as st
from PIL import Image
import eda, model



st.sidebar.title("Menu")
page = st.sidebar.selectbox(label='Select Page', options=['Home Page', 'EDA', 'Model'])


if page == 'Home Page':
    st.header('Welcome to Default My Predict Price House Apps')
    st.subheader('Please Select Menu On Side Bar')
    img = Image.open('rumah.jpg')
    st.image(img)

elif page == 'EDA':
    eda.run()

else:
    model.run()



