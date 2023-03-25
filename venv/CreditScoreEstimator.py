import streamlit

streamlit.set_page_config(page_title="Credit Score Estimator", page_icon="", layout="wide")

with streamlit.container(): # title and description of website
    streamlit.title("Credit Score Estimator")
    streamlit.write("Answer the following questions to receive an estimate of your credit score!")