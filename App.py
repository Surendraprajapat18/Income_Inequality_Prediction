import streamlit as st
import numpy as np
import pandas as pd
from zipfile import ZipFile
import joblib

# Page Title, Description, and Problem Statement
st.title("Income Inequality Prediction APP💵")
st.markdown("""
## About
This web app predicts the income inequality of a person based on their demographics. 

## 🧾Description: 
Income inequality - when income is distributed in an uneven manner among a population - is a growing problem in developing nations across the world. With the rapid rise of AI and worker automation, this problem could continue to grow if steps are not taken to address the issue. This solution can potentially reduce the cost and improve the accuracy of monitoring key population indicators such as income level in between census years. This information will help policymakers to better manage and avoid income inequality globally.

## 🧭 Problem Statement: 
The target feature is income_above_limit, which is a binary-class variable. The objective of this challenge is to create a machine learning model to predict whether an individual earns above or below a certain amount. Your metric for evaluation will be f1-score.
""")

# Load Model and Encoder
model = joblib.load(r"models\ML_Model.joblib")
ohe_encoder = joblib.load(r"models\OHE_enc.joblib")

# Input features unique values
education_opt = [' Bachelors degree(BA AB BS)', ' Masters degree(MA MS MEng MEd MSW MBA)',
                 ' Associates degree-occup /vocational', ' Some college but no degree',
                 ' Associates degree-academic program', ' Children', ' High school graduate',
                 ' Prof school degree (MD DDS DVM LLB JD)', ' 11th grade', ' 9th grade', ' 7th and 8th grade',
                 ' 10th grade', ' 12th grade no diploma', ' Doctorate degree(PhD EdD)',
                 ' 5th or 6th grade', ' 1st 2nd 3rd or 4th grade', ' Less than 1st grade']

marital_status_opt = [' Married-civilian spouse present', ' Never married', ' Divorced',
                      ' Married-spouse absent', ' Widowed', ' Separated', ' Married-A F spouse present']
is_hispanic_opt = [' All other', ' Mexican-American', ' Puerto Rican', ' Other Spanish', ' Central or South American',
                   ' Mexican (Mexicano)', ' Chicano', ' Cuban', ' NA', ' Do not know']
tax_status_opt = [' Joint both under 65', ' Single', ' Nonfiler', ' Joint one under 65 & one 65+',
                  ' Head of household', ' Joint both 65+']

vet_benefit_opt = ["Yes", "No", "Not interested in sharing"]

# Streamlit Form for Predictions
with st.form("Predictions"):
    st.subheader("Enter the Information")

    # User Input Fields
    education = st.selectbox("Education", options=education_opt)
    marital_status = st.selectbox("Marital Status", options=marital_status_opt)
    is_hispanic = st.selectbox("Is Hispanic", options=is_hispanic_opt)
    tax_status = st.selectbox("Tax Status", options=tax_status_opt)
    age = st.number_input("Age")
    gender = st.radio("Gender", [' Male', ' Female'])
    working_week_per_year = st.number_input("Working Week Per Year")
    total_employed = st.number_input("Total Employed", value=0, step=1)
    vet_benefit = st.selectbox("Vet Benefit", options=vet_benefit_opt)

    submit = st.form_submit_button("Predict")

if submit:
    # Convert vet_benefit to numerical
    if vet_benefit == "Yes":
        vet_benefit = 1
    elif vet_benefit == "No":
        vet_benefit = 0
    else:
        vet_benefit = 2

    # Transform categorical features
    encoded = ohe_encoder.transform(np.array([gender, education, marital_status, is_hispanic, tax_status]).reshape(1, -1))

    # Prepare numerical features
    num_array = np.array([age, working_week_per_year, int(total_employed), vet_benefit]).reshape(1, -1)

    # Concatenate numerical and encoded features
    inp_data = np.concatenate((num_array, encoded), axis=1)

    # Make Prediction
    pred = model.predict(inp_data)

    # Display Prediction Result
    if pred == 1:
        st.title("Your Income is Above Limit")
    else:
        st.title("Your Income is Below Limit")
