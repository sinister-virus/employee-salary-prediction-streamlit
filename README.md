# Employee Salary Prediction App
A simple machine learning web application that predicts employee salaries based on features like age, gender, education level, and job title.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)](https://www.python.org/)
[![Colab](https://img.shields.io/badge/Run%20in-Colab-orange?logo=googlecolab)](https://colab.research.google.com/drive/1w4GqMjBsPD17KayIksLO37s291ta4gsw?usp=sharing)
[![Streamlit App](https://img.shields.io/badge/Streamlit-View_App-blue?logo=streamlit)](https://employee-salary-prediction-stlit.streamlit.app/)
[![Made with ❤️](https://img.shields.io/badge/Made%20with-%E2%9D%A4-red)](#)


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
- `LICENSE` – MIT License

## 🚀 How to Run Locally

```bash
git clone https://github.com/sinister-virus/employee-salary-prediction-streamlit.git
cd employee-salary-prediction-streamlit
pip install -r requirements.txt
streamlit run app.py
```

# 📘 License
This project is licensed under the [MIT License](LICENSE) and is intended for **educational and demonstration purposes only**. Use at your own risk.
