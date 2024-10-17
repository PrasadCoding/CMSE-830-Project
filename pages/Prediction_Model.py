import streamlit as st

# Page title and description
st.title("Heart Disease Prediction Model")
st.write("""
    Please provide the following information for prediction of heart disease risk. This tool helps assess risk based on various health indicators and personal habits.
""")

# Create input fields for user data
col1, col2 = st.columns(2)

# Column 1 inputs
with col1:
    male = st.selectbox("Sex", ["Male", "Female"])
    age = st.slider("Age", 18, 100, 30)
    education = st.selectbox("Education Level", ["Less than high school", "High school", "College", "Post-graduate"])
    current_smoker = st.selectbox("Current Smoker", ["Yes", "No"])
    cigs_per_day = st.number_input("Cigarettes Per Day", min_value=0, max_value=100, value=0, step=1)
    prevalent_stroke = st.selectbox("History of Stroke", ["Yes", "No"])

# Column 2 inputs
with col2:
    prevalent_hyp = st.selectbox("Prevalent Hypertension", ["Yes", "No"])
    bpm_meds = st.selectbox("On Blood Pressure Medication", ["Yes", "No"])
    diabetes = st.selectbox("Diabetes", ["Yes", "No"])
    tot_chol = st.number_input("Total Cholesterol (mg/dL)", min_value=100, max_value=500, value=200, step=1)
    sys_bp = st.number_input("Systolic Blood Pressure (mm Hg)", min_value=80, max_value=200, value=120, step=1)
    dia_bp = st.number_input("Diastolic Blood Pressure (mm Hg)", min_value=40, max_value=120, value=80, step=1)
    heart_rate = st.number_input("Heart Rate (bpm)", min_value=40, max_value=200, value=70, step=1)
    glucose = st.number_input("Glucose Level (mg/dL)", min_value=50, max_value=300, value=100, step=1)

# Calculate BMI from user-provided weight and height
bmi = st.number_input("Body Mass Index (BMI)", min_value=10.0, max_value=50.0, value=24.0, step=0.1)

# Submit button for prediction
if st.button("Predict Risk"):
    st.success("Prediction logic will be applied here.")

# Add optional visualizations related to user inputs
st.subheader("Your Health Indicators Overview")
st.write("Here you can include visualizations or summaries of the user's inputs to provide immediate feedback on health indicators.")
