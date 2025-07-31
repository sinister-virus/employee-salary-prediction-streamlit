import streamlit as st
from model import predict_salary

st.title("Employee Salary Prediction App")

age = st.number_input("Age", min_value=18, max_value=100, value=30)
gender = st.selectbox("Gender", ["Male", "Female"])
education = st.selectbox("Education Level", ["Bachelor's", "Master's", "PhD"])
job_title = st.selectbox("Job Title", ["Software Engineer", "Data Analyst", "Senior Manager", "Sales Associate", "Director"])
experience = st.number_input("Years of Experience", min_value=0, max_value=50, value=5)

if st.button("Predict Salary"):
    salary = predict_salary(age, gender, education, job_title, experience)
    st.success(f"Predicted Salary: ₹{salary:,.2f}")
