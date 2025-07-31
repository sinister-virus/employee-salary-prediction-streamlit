# Employee Salary Prediction App

A simple machine learning web application that predicts employee salaries based on features like age, gender, education level, and job title.

## 🔍 Project Overview

This app:
- Trains a Linear Regression model on a sample dataset.
- Encodes categorical variables using `LabelEncoder`.
- Serves a web app via Streamlit for user-friendly prediction.

## 📂 File Structure

- `app.py` – Main Streamlit app
- `model.py` – Prediction logic & model loader
- `model_train.py` – Script to train and save the model
- `Salary_Data.csv` – Sample data
- `salary_model.pkl` – Trained model
- `encoders.pkl` – Saved LabelEncoders
- `requirements.txt` – Python dependencies

## 🚀 How to Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
