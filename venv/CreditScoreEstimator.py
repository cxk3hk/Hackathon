# resources employed:
# 1. https://www.myfico.com/fico-credit-score-estimator/estimator
# 2. https://www.creditkarma.com/credit-cards/i/vantagescore-30
# 3. https://www.moneyunder30.com/credit-score-estimator


import streamlit as st
import requests
from streamlit_lottie import st_lottie


def get_url(url):
    request = requests.get(url)
    return request.json()

# default values for answers
answer1 = -1

credit_score_icon = get_url("https://assets10.lottiefiles.com/packages/lf20_d4zpfpou.json")

st.set_page_config(page_title="Credit Score Estimator", page_icon="", layout="wide")

with st.container(): # title and description of website, and an animation
    title_column, animation_column = st.columns(2)
    with title_column:
        st.write(" ")
        st.write(" ")
        st.write(" ")
        st.title("BZ Credit Score Estimator")
        st.write("Answer the following questions to receive an estimate of your credit score!")
    with animation_column:
        st_lottie(credit_score_icon, height = 250, key = "credit score icon")

with st.container(): # Questions
    st.write("1. How many credit cards do you currently have?")
    left_column, right_column = st.columns((1, 2))
    with left_column:
        resultZero = st.button("None")
        if resultZero:
            answer1 = 0
        resultThree = st.button("Two to Four")
        if resultThree:
            answer1 = 3
    with right_column:
        resultOne = st.button("One")
        if resultOne:
            answer1 = 1
        resultFive = st.button("Five or More")
        if resultFive:
            answer1 = 5

    if (answer1 == 0):
        st.subheader("Your estimated credit is: Limited")
        st.text("""
            Based on the information given, we are unable to make an estimate on your credit score. 
            In order to receive an estimate, you must have at least one account which has been open 
            for 6 or more months.
            """)
    #else:










