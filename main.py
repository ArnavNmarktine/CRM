import streamlit as st 
import pandas as pd 
import random
import matplotlib.pyplot as plt
import warnings
# Ignore all warnings (Not recommended in most cases)
warnings.filterwarnings("ignore")


st.set_page_config(page_title="Marktine", 
                   page_icon=":M:", 
                   layout="wide")


st.sidebar.image("https://marktine.com/wp-content/uploads/2022/01/logo.svg", use_column_width=True)

with st.sidebar:
    st.write("129, Shri Hans Marg, Usha Vihar, Keshav Vihar, Arjun Nagar, Jaipur, Rajasthan 302018")



st.sidebar.header("Please Filter Here:")


product = ["Vriti","Generative_AI_Solutions","Vriddhi","UnifID_IAM","Parse_Connect"]
product = st.sidebar.selectbox("Select Product",options=product)


region = ["North","South","East","West"]
region = st.sidebar.selectbox("Region",options=region)







