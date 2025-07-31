import pandas as pd
import pickle
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder

# Load data
data = pd.read_csv('Salary_Data.csv')

# Drop rows with missing values
data = data.dropna()

# Encode categorical variables
le_gender = LabelEncoder()
le_education = LabelEncoder()
le_job = LabelEncoder()

data['Gender'] = le_gender.fit_transform(data['Gender'])
data['Education Level'] = le_education.fit_transform(data['Education Level'])
data['Job Title'] = le_job.fit_transform(data['Job Title'])

# Save the label encoders
with open('encoders.pkl', 'wb') as f:
    pickle.dump({
        'gender': le_gender,
        'education': le_education,
        'job': le_job
    }, f)

# Define features and target
X = data[['Age', 'Gender', 'Education Level', 'Job Title', 'Years of Experience']]
y = data['Salary']

# Train model
model = LinearRegression()
model.fit(X, y)

# Save model
with open('salary_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("✅ Model training complete and saved.")
