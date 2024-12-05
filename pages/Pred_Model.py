import joblib
import streamlit as st
import requests
from io import BytesIO

# Function to download a model from a GitHub URL
def load_model_from_github(url):
    response = requests.get(url)
    model = joblib.load(BytesIO(response.content))
    return model

# GitHub raw file URLs for the models
rf_model_url = "https://github.com/PrasadCoding/CMSE-830-Project/blob/master/models/heart_disease_rf_model.joblib"
xgb_model_url = "https://github.com/PrasadCoding/CMSE-830-Project/blob/master/models/heart_disease_xgb_model.joblib"

# Load the models from GitHub
rf_model = load_model_from_github(rf_model_url)
xgb_model = load_model_from_github(xgb_model_url)

# Function to make prediction with RandomForest
def predict_rf(features):
    return rf_model.predict([features])[0]

# Function to make prediction with XGBoost
def predict_xgb(features):
    return xgb_model.predict([features])[0]

# Streamlit UI
st.title("Heart Disease Prediction")

# Input fields for user input (make sure these match your training features)
age = st.number_input("Age", min_value=1, max_value=100)
sex_male = st.selectbox("Sex (Male)", options=[0, 1])  # 0 for Female, 1 for Male
cigs_per_day = st.number_input("Cigarettes per Day", min_value=0, max_value=100)
sys_bp = st.number_input("Systolic Blood Pressure", min_value=0, max_value=300)
dia_bp = st.number_input("Diastolic Blood Pressure", min_value=0, max_value=200)
bmi = st.number_input("BMI", min_value=10, max_value=50)
heart_rate = st.number_input("Heart Rate (BPM)", min_value=40, max_value=200)
glucose = st.number_input("Glucose Level", min_value=40, max_value=300)

# Combine inputs into a list
features = [age, sex_male, cigs_per_day, sys_bp, dia_bp, bmi, heart_rate, glucose]

# Radio buttons to choose between RandomForest and XGBoost
model_choice = st.radio("Select a Model", ("Random Forest", "XGBoost"))

# Button to make prediction
if st.button("Predict"):
    if model_choice == "Random Forest":
        prediction = predict_rf(features)
    else:
        prediction = predict_xgb(features)
    
    # Display result
    if prediction == 1:
        st.write("The model predicts that you will develop heart disease in 10 years.")
    else:
        st.write("The model predicts that you will not develop heart disease in 10 years.")
