import streamlit as st
import joblib  # or import pickle if you used pickle to save your model

# Load the pre-trained Random Forest model
# model = joblib.load('random_forest_model.pkl')  # Adjust the path as needed

# Set up the page title and description
st.title("Heart Disease Prediction Model")
st.write("Provide the following information to predict the likelihood of heart disease:")

# Collect user input for the prediction model
col1, col2 = st.columns(2)

with col1:
    male = st.selectbox("Sex (Male)", options=["Yes", "No"], help="Select 'Yes' for Male, 'No' for Female")
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

# Convert "Yes" and "No" options to 1 and 0 for the machine learning model
male = 1 if male == "Yes" else 0
currentSmoker = 1 if currentSmoker == "Yes" else 0
BPMeds = 1 if BPMeds == "Yes" else 0
prevalentStroke = 1 if prevalentStroke == "Yes" else 0
prevalentHyp = 1 if prevalentHyp == "Yes" else 0
diabetes = 1 if diabetes == "Yes" else 0

# Add a button to submit and calculate the prediction
if st.button("Predict Heart Disease Risk"):
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
    
    # import pandas as pd
    # input_data = pd.DataFrame(user_data)
    
    # # Make a prediction using the loaded model
    # prediction = model.predict(input_data)

    # # Display the prediction result
    # if prediction[0] == 1:
    #     st.write("**Prediction Result:** You are at high risk of heart disease.")
    # else:
    #     st.write("**Prediction Result:** You are at low risk of heart disease.")
