import pickle
import numpy as np
import pandas as pd

# Load model
with open('salary_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Load encoders
with open('encoders.pkl', 'rb') as f:
    encoders = pickle.load(f)

le_gender = encoders['gender']
le_education = encoders['education']
le_job = encoders['job']

def predict_salary(age, gender, education, job_title, experience):
    gender_enc = le_gender.transform([gender])[0]
    education_enc = le_education.transform([education])[0]
    job_enc = le_job.transform([job_title])[0]

    features = pd.DataFrame([{
        "Age": age,
        "Gender": gender_enc,
        "Education Level": education_enc,
        "Job Title": job_enc,
        "Years of Experience": experience
    }])
    
    return model.predict(features)[0]