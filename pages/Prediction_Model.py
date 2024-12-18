import streamlit as st
import pandas as pd
import joblib  # To load pre-trained models

# Function to load the models from GitHub (adjusted from your original code)
def download_model_from_github(url, filename):
    response = requests.get(url)
    with open(filename, 'wb') as f:
        f.write(response.content)

# URLs to download the pre-trained models
rf_model_url = "https://github.com/PrasadCoding/CMSE-830-Project/raw/refs/heads/master/models_midterm/Random%20Forest_model.pkl"
lr_model_url = "https://github.com/PrasadCoding/CMSE-830-Project/raw/refs/heads/master/models_midterm/Logistic%20Regression_model.pkl"
xgboost_model_url = "https://github.com/PrasadCoding/CMSE-830-Project/raw/refs/heads/master/models_midterm/XGBoost_model.pkl"

# Download model files
rf_model_path = "Random_Forest_model.pkl"
lr_model_path = "Logistic_Regression_model.pkl"
xgboost_model_path = "XGBoost_model.pkl"

download_model_from_github(rf_model_url, rf_model_path)
download_model_from_github(lr_model_url, lr_model_path)
download_model_from_github(xgboost_model_url, xgboost_model_path)

# Load the pre-trained models using joblib
rf_model = joblib.load(rf_model_path)
lr_model = joblib.load(lr_model_path)
xgboost_model = joblib.load(xgboost_model_path)

# Set background image
def set_bg_image(image_url):
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

# Background image URL
image_url = 'https://raw.githubusercontent.com/PrasadCoding/CMSE-830-Project/refs/heads/master/images/bg43.png'
set_bg_image(image_url)

# Load sample DataFrame (replace this with actual data)
df = pd.read_csv("dataset/heart_disease.csv")  # Your DataFrame
df = df.drop('education', axis=1)
df.dropna(inplace=True)

# Define features and target
X = df.drop(columns=['TenYearCHD'])
y = df['TenYearCHD']

# Set up the page title
st.markdown("<h1 style='color: #FF4B4B;'>Heart Disease Prediction Model</h1>", unsafe_allow_html=True)
st.write("Provide the following information to predict the likelihood of heart disease:")

# Collect user input for the prediction model
col1, col2 = st.columns(2)

with col1:
    sex = st.selectbox("Sex", options=["Male", "Female"], help="Select your gender")
    age = st.number_input("Age", min_value=1, max_value=120, value=39)
    currentSmoker = st.selectbox("Current Smoker", options=["Yes", "No"], help="Select 'Yes' if you smoke currently")
    cigsPerDay = st.number_input("Cigarettes Per Day", min_value=0, max_value=100, value=0)
    BPMeds = st.selectbox("On Blood Pressure Medication", options=["Yes", "No"], help="Select 'Yes' if you are on BP meds")
    prevalentStroke = st.selectbox("Prevalent Stroke", options=["Yes", "No"], help="Select 'Yes' if you've had a stroke")
    prevalentHyp = st.selectbox("Prevalent Hypertension", options=["Yes", "No"], help="Select 'Yes' if you have high BP")

with col2:
    diabetes = st.selectbox("Diabetes", options=["Yes", "No"], help="Select 'Yes' if you have diabetes")
    totChol = st.number_input("Total Cholesterol (mg/dL)", min_value=100, max_value=500, value=195)
    sysBP = st.number_input("Systolic Blood Pressure", min_value=80, max_value=200, value=106)
    diaBP = st.number_input("Diastolic Blood Pressure", min_value=50, max_value=130, value=70)
    BMI = st.number_input("Body Mass Index (BMI)", min_value=10.0, max_value=50.0, value=26.97)
    heartRate = st.number_input("Heart Rate (bpm)", min_value=40, max_value=200, value=80)
    glucose = st.number_input("Glucose Level (mg/dL)", min_value=50, max_value=300, value=77)

# Convert categorical inputs to binary values
male = 1 if sex == "Male" else 0
currentSmoker = 1 if currentSmoker == "Yes" else 0
BPMeds = 1 if BPMeds == "Yes" else 0
prevalentStroke = 1 if prevalentStroke == "Yes" else 0
prevalentHyp = 1 if prevalentHyp == "Yes" else 0
diabetes = 1 if diabetes == "Yes" else 0

# Add a dropdown to select the model
model_choice = st.selectbox("Choose a Model", options=["Random Forest", "Logistic Regression", "XGBoost"])

# Add a button to submit and calculate the prediction
if st.button("Predict Heart Disease Risk"):
    try:
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
        elif model_choice == "XGBoost":
            prediction = xgboost_model.predict(input_data)

        # Display the prediction result
        if prediction[0] == 1:
            st.write("**Prediction Result:** You are at high risk of heart disease.")
        else:
            st.write("**Prediction Result:** You are at low risk of heart disease.")
    
    except Exception as e:
        st.error(f"An error occurred: {e}")
