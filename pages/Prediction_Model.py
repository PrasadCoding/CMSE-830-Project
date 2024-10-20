import streamlit as st
import pandas as pd

# Load the pre-trained Random Forest model
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Sample DataFrame (replace this with your actual DataFrame)
df = pd.read_csv("dataset/heart_disease.csv")  # Your DataFrame
df.dropna(inplace = True)
# Assuming 'TenYearCHD' is the target variable and all other columns are features
X = df.drop(columns=['TenYearCHD'])
y = df['TenYearCHD']

# Splitting the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Creating the Random Forest Classifier
rf_model = RandomForestClassifier(random_state=42)

# Fitting the model
rf_model.fit(X_train, y_train)

# Making predictions
y_pred = rf_model.predict(X_test)

# Calculating accuracy
accuracy = accuracy_score(y_test, y_pred)


# Set up the page title and description
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

        # Make a prediction using the loaded model
        prediction = rf_model.predict(input_data)

        # Display the prediction result
        if prediction[0] == 1:
            st.write("**Prediction Result:** You are at high risk of heart disease.")
        else:
            st.write("**Prediction Result:** You are at low risk of heart disease.")
    
    except Exception as e:
        st.error(f"An error occurred: {e}")
