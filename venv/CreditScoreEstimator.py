# resources employed:
# 1. https://www.myfico.com/fico-credit-score-estimator/estimator
# 2. https://www.creditkarma.com/credit-cards/i/vantagescore-30
# 3. https://www.moneyunder30.com/credit-score-estimator
# 4. https://www.banks.com/articles/credit/credit-score/credit-score-range/


import streamlit as st
import requests
from streamlit_lottie import st_lottie


def get_url(url):
    request = requests.get(url)
    return request.json()

# default values for answers
answer1 = -1
condition = True

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

placeholder = st.empty()

with placeholder.container():  # Questions
    # Question 1: Credit Diversity --> the more credit cards, the better
    st.write("1. How many credit cards do you currently have?")
    left_column, right_column = st.columns((1, 2))
    with left_column:
        resultZero = st.button("None", "zero")
        if resultZero:
            answer1 = 0
            condition = False
        resultThree = st.button("Two to Four", 3)
        if resultThree:
            answer1 = 3
    with right_column:
        resultOne = st.button("One", 1)
        if resultOne:
            answer1 = 1
        resultFive = st.button("Five or More", 5)
        if resultFive:
            answer1 = 5

    if (answer1 == 0):
        st.subheader("Your estimated credit is: Limited")
        st.text("""
                Based on the information given, we are unable to make an estimate on your credit score. 
                In order to receive an estimate, you must have at least one account which has been open 
                for 6 or more months.
                    """)
    if(answer1 != 0):
        # Question 2: Credit History - The longer, the better (input, round up to the nearest 0.25 year)
        #                  i.e. 2 months = 0.25, 5 months = 0.5, 1 yr and 3 months = 1.25, etc...)
        age_of_card = st.number_input(
            "How long have you had your oldest active credit card? (round to the nearest 0.25 years)",
            0.00)

        # Question 3: Payment History (input of number of late payments. calculate as ratio with credit history)
        num_late_payments = st.number_input("What is the total number of late credit card payments you have incurred, if any?", 0)

        # Question 4: Calculating Credit Utlization - finding out debt-to-credit ratio (the lower, the better)
        #   Experts generally recommend a credit utilization ratio of below 30%.
        #   ratio calculation = used credit(what the consumer owes) / available credit (credit limit)

        #   1. getting user input monthly total credit limit
        credit_limit = st.number_input("What is the total credit limit for all of your credit cards?", 1.00)

        #   2. getting user estimate of total monthly spending
        monthly_spending = st.number_input("What is your total amount of credit card debt?", 0.00)

        #   3. calculating debt ratio and seeing if the percentage is below 30%. use if-elif-else
        debt_ratio = (monthly_spending / credit_limit)

        submit = st.button("Submit")


if(submit):
    placeholder.empty()

    credit_score = 0
    # calculating credit score
    # caculating payment history(42%)
    payment_history = (num_late_payments / age_of_card)
    credit_score += (357 * (1 - payment_history))

    # credit utlization (22%)
    if (debt_ratio < 30):
        credit_score += 187
    else:
        credit_score += (187 * (1 - debt_ratio))

        # balances
    if (monthly_spending <= (credit_limit / 3)):
        credit_score += 110.5
    elif (monthly_spending < (credit_limit / 2)):
        credit_score += 98
    elif (monthly_spending >= (credit_limit / 2)):
        credit_score += 85.5

        # number of cards
    credit_score += (answer1 * 5)

    # credit age
    credit_score += 170.5

    credit_score = int(credit_score)
    # minimum value is 300
    if (credit_score < 300):
        credit_score = 300

    st.subheader("Your estimated credit is: " + str(credit_score))




















