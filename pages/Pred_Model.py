import streamlit as st
import pandas as pd
import requests
from io import BytesIO
import joblib  # Use joblib to load models if they are saved in joblib format

# Set background image
def set_bg_image(image_url):
    """
    Set background image for the Streamlit app using a raw GitHub URL
    """
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("{image_url}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            height: 100vh;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )

# Path to your background image file on GitHub (use the raw URL)
image_url = 'https://raw.githubusercontent.com/PrasadCoding/CMSE-830-Project/refs/heads/master/images/bg43.png'  # Replace with your raw URL
set_bg_image(image_url)

# Function to load model from a GitHub URL using joblib
def load_model_from_github(url):
    response = requests.get(url)
    model = joblib.load(BytesIO(response.content))  # Use joblib for loading models
    return model

# URLs to your models on GitHub (use raw URLs for the pickle files)
xgb_model_url = "https://github.com/PrasadCoding/CMSE-830-Project/raw/refs/heads/master/models/xgb_model.pkl"
gb_model_url = "https://github.com/PrasadCoding/CMSE-830-Project/raw/refs/heads/master/models/gb_model.pkl"

# Load the models from GitHub
xgb_model = load_model_from_github(xgb_model_url)
gb_model = load_model_from_github(gb_model_url)

# Set up the page title and description
st.markdown("<h1 style='color: #FF4B4B;'>Heart Disease Prediction</h1>", unsafe_allow_html=True)
st.write("Provide the following information to predict the likelihood of heart disease:")

# Collect user input for the prediction (all inputs in one column)
gender = st.selectbox("Gender", options=["Male", "Female"])
age = st.number_input("Age", min_value=1, max_value=120, value=50)
smoking_history = st.selectbox("Smoking History", options=["Yes", "No"])
bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, value=25.0)
blood_glucose_level = st.number_input("Blood Glucose Level", min_value=50, max_value=300, value=100)
hypertension = st.selectbox("Hypertension", options=["Yes", "No"])
diabetes = st.selectbox("Diabetes", options=["Yes", "No"])

# Convert categorical inputs to binary values
gender = 1 if gender == "Male" else 0
smoking_history = 1 if smoking_history == "Yes" else 0
hypertension = 1 if hypertension == "Yes" else 0
diabetes = 1 if diabetes == "Yes" else 0

# Prepare the input data as a DataFrame
user_data = {
    "gender": [gender],
    "age": [age],
    "hypertension": [hypertension],
    "smoking_history": [smoking_history],
    "bmi": [bmi],
    "blood_glucose_level": [blood_glucose_level],
    "diabetes": [diabetes]
}

input_data = pd.DataFrame(user_data)

# Dropdown to select the model
model_choice = st.selectbox("Choose a Model", options=["XGBoost", "Gradient Boosting"])

# Prediction on button click
if st.button("Predict Heart Disease Risk"):
    try:
        if model_choice == "XGBoost":
            prediction = xgb_model.predict(input_data)
        elif model_choice == "Gradient Boosting":
            prediction = gb_model.predict(input_data)

        # Display the prediction result
        if prediction[0] == 1:
            st.write("**Prediction Result:** You are at high risk of heart disease.")
        else:
            st.write("**Prediction Result:** You are at low risk of heart disease.")
    
    except Exception as e:
        st.error(f"An error occurred: {e}")
