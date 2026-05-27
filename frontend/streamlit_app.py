import streamlit as st
import requests

# Title
st.title("Financial Risk Analysis System")

# Inputs
age = st.number_input("Age")

income = st.number_input("Income")

loan_amount = st.number_input("Loan Amount")

credit_score = st.number_input("Credit Score")

years_exp = st.number_input("Years of Experience")

employment = st.selectbox(
    "Employment Type",
    ["Employed", "Self-Employed", "Unemployed"]
)

# Predict button
if st.button("Predict"):

    # Input data
    data = {
        "Age": age,
        "Income": income,
        "LoanAmount": loan_amount,
        "CreditScore": credit_score,
        "YearsExperience": years_exp,
        "EmploymentType": employment
    }

    # Send request to deployed FastAPI backend
    response = requests.post(
        "https://loan-risk-prediction-rwvi.onrender.com/predict",
        json=data
    )

    # Convert response to JSON
    result = response.json()

    # Show prediction
    st.success(
        f"Loan Status: {result['prediction']}"
    )

    # Show probability
    st.write(
        f"Approval Probability: {result['probability']:.2f}"
    )