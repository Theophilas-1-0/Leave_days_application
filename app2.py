import streamlit as st
#import pandas as pd

# Title of the app
st.title("Researcher Profile Page")

# Collect basic information
name = "Londolani Theophilas Lethole"
field = "Atmospheric Science"
institution = "South African Weather Service"

# Display basic profile information
st.header("Leave days applications")
choice = st.selectbox('type of leave', ['sick leave', 'Annual leave', 'Already tired for  the year'])
date = st.date_input('start of your leave')
date = st.date_input('end of your leave')

# Reason for your leave
speech = st.audio_input('Record reason for your leave')

#HR requirements
image = st.camera_input('Take a picture of your surroundiing')
choice = st.radio('is it necessary for you to take your leave now', ['yes', 'no'])
number = st.slider('if yes, rate the importantance of your leave out of 10', 0,10)

st.title('submit here')
clicked = st.button('submit')

# Add a contact section
st.header("Contact Information")
email = "Londolani.Lethole@weathersa.co.za"
st.write(f"You can reach {name} at {email}.")

st.feedback('stars')