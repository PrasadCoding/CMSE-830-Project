import streamlit as st
import pandas as pd
import requests
import joblib

# Function to download model from GitHub
def download_model_from_github(url, filename):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors
        with open(filename, 'wb') as f:
            f.write(response.content)
        st.write(f"Model downloaded successfully: {filename}")
    except requests.exceptions.RequestException as e:
        st.error(f"Error downloading model: {e}")

# URLs for the models on GitHub (replace with actual raw URLs)
rf_model_url = "https://github.com/PrasadCoding/CMSE-830-Project/raw/refs/heads/master/models_midterm/Random%20Forest_model.pkl"
lr_model_url = "https://github.com/PrasadCoding/CMSE-830-Project/raw/refs/heads/master/models_midterm/Logistic%20Regression_model.pkl"
xgboost_model_url = "https://github.com/PrasadCoding/CMSE-830-Project/raw/refs/heads/master/models_midterm/XGBoost_model.pkl"

# Paths for saving the models locally
rf_model_path = "Random_Forest_model.pkl"
lr_model_path = "Logistic_Regression_model.pkl"
xgboost_model_path = "XGBoost_model.pkl"

# Download models
download_model_from_github(rf_model_url, rf_model_path)
download_model_from_github(lr_model_url, lr_model_path)
download_model_from_github(xgboost_model_url, xgboost_model_path)

# Load pre-trained models
try:
    rf_model = joblib.load(rf_model_path)
    lr_model = joblib.load(lr_model_path)
    xgboost_model = joblib.load(xgboost_model_path)
    st.write("Models loaded successfully.")
except Exception as e:
    st.error(f"Error loading models: {e}")

# Set up the page title and description
st.markdown("<h1 style='color: #FF4B4B;'>Heart Disease Prediction Model</h1>", unsafe_allow_html=True)
st.write("Provide the following information to predict the likelihood of heart disease:")

# Sample DataFrame (replace this with your actual DataFrame)
df = pd.read_csv("dataset/heart_disease.csv")  # Your DataFrame
df = df.drop('education', axis=1)
df.dropna(inplace=True)

# Assuming 'TenYearCHD' is the target variable and all other columns are features
X = df.drop(columns=['TenYearCHD'])
y = df['TenYearCHD']

# Splitting the data into training and testing sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Add a dropdown to select the model
model_choice = st.selectbox("Choose a Model", options=["Random Forest", "Logistic Regression"])

# Add a button to submit and calculate the prediction
if st.button("Predict Heart Disease Risk"):
    try:
        # Collect user input for prediction (same as before)
        # Code for collecting user input...

        # Create a DataFrame from the input data
        user_data = {
            "male": [male],
            "age": [age],
            "currentSmoker": [currentSmoker],
            "cigsPerDay": [cigsPerDay],
            "BPMeds": [BPMeds],
            "prevalentStroke": [prevalentStroke],
            "prevalentHyp": [prevalentHyp],
            "diabetes": [diabetes],
            "totChol": [totChol],
            "sysBP": [sysBP],
            "diaBP": [diaBP],
            "BMI": [BMI],
            "heartRate": [heartRate],
            "glucose": [glucose]
        }

        # Create a DataFrame
        input_data = pd.DataFrame(user_data)

        # Make a prediction using the selected model
        if model_choice == "Random Forest":
            prediction = rf_model.predict(input_data)
        elif model_choice == "Logistic Regression":
            prediction = lr_model.predict(input_data)

        # Display the prediction result
        if prediction[0] == 1:
            st.write("**Prediction Result:** You are at high risk of heart disease.")
        else:
            st.write("**Prediction Result:** You are at low risk of heart disease.")
    
    except Exception as e:
        st.error(f"An error occurred: {e}")
