import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
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

import streamlit as st
import pandas as pd

# Set the title of the Streamlit app
st.title('Data Analysis')

# Load the datasets
# Replace the paths with your actual dataset paths or upload functionality
df_fram = pd.read_csv('dataset1/framingham.csv')  # Update with your first dataset path
df_diabetes = pd.read_csv('dataset1/diabetes1.csv')  # Update with your second dataset path

# Display the first dataset
st.subheader('Dataset 1: Heart Disease Prediction Data')
st.write(df_fram.head())  # Display first 5 rows of the first dataset

# Explanation for Dataset 1 variables
st.markdown("""
**Variables in Dataset 1:**
- **male**: Gender of the individual (binary: 1 for male, 0 for female).
- **age**: Age of the individual in years.
- **education**: Education level of the individual (categorical: e.g., high school, college, etc.).
- **currentSmoker**: Whether the individual currently smokes (binary: 1 for yes, 0 for no).
- **cigsPerDay**: Average number of cigarettes smoked per day by the individual.
- **BPMeds**: Whether the individual is on blood pressure medication (binary: 1 for yes, 0 for no).
- **prevalentStroke**: Whether the individual has had a stroke in the past (binary: 1 for yes, 0 for no).
- **prevalentHyp**: Whether the individual has hypertension (binary: 1 for yes, 0 for no).
- **diabetes**: Whether the individual has diabetes (binary: 1 for yes, 0 for no).
- **totChol**: Total cholesterol level of the individual (in mg/dL).
- **sysBP**: Systolic blood pressure of the individual (in mmHg).
- **diaBP**: Diastolic blood pressure of the individual (in mmHg).
- **BMI**: Body Mass Index of the individual (calculated from height and weight).
- **heartRate**: Heart rate of the individual (in beats per minute).
- **glucose**: Glucose level of the individual (in mg/dL).
- **TenYearCHD**: Whether the individual has a 10-year risk of coronary heart disease (binary: 1 for yes, 0 for no).
""")

# Display the second dataset
st.subheader('Dataset 2: Diabetes Prediction Data')
st.write(df_diabetes.head())  # Display first 5 rows of the second dataset

# Explanation for Dataset 2 variables
st.markdown("""
**Variables in Dataset 2:**
- **gender**: Gender of the individual (binary: 1 for male, 0 for female).
- **age**: Age of the individual in years.
- **hypertension**: Whether the individual has hypertension (binary: 1 for yes, 0 for no).
- **heart_disease**: Whether the individual has heart disease (binary: 1 for yes, 0 for no).
- **smoking_history**: History of smoking (categorical: e.g., 'never smoked', 'smokes currently', etc.).
- **bmi**: Body Mass Index of the individual (calculated from height and weight).
- **HbA1c_level**: Hemoglobin A1c level of the individual (percentage).
- **blood_glucose_level**: Blood glucose level of the individual (in mg/dL).
- **diabetes**: Whether the individual has diabetes (binary: 1 for yes, 0 for no).
""")

# Data Sources
st.markdown("""
**Data Sources:**
1. Heart Disease Dataset (Framingham): [Link to Dataset](https://www.kaggle.com/datasets/aasheesh200/framingham-heart-study-dataset)
2. Diabetes Prediction Dataset: [Link to Dataset](https://www.kaggle.com/datasets/iammustafatz/diabetes-prediction-dataset)
""")


st.subheader('Categorical to Numerical')
st.markdown("### Dataset 2: Diabetes Prediction Data")
df_diabetes['gender'] = df_diabetes['gender'].map({'Male': 1, 'Female': 0})
df_diabetes['smoking_history'] = df_diabetes['smoking_history'].map({'never': 0, 'current': 1, 'former': 1})
st.write(df_diabetes.head())

st.subheader('Merging the datasets')
st.markdown("The common columns in both datasets are matched, and the data is merged accordingly, ensuring that the corresponding rows are aligned. After the combination, we have a single dataset that integrates all relevant features.")
# DataFrame for the table with common columns
data = {
    'Framingham Heart Study': ['male', 'age', 'prevalentHyp', 'currentSmoker', 'BMI', 'glucose', 'totChol', 'TenYearCHD'],
    'Diabetes Prediction Dataset': ['gender', 'age', 'hypertension', 'smoking_history', 'bmi', 'HbA1c_level', 'blood_glucose_level', 'diabetes']
}

# Create a DataFrame
df = pd.DataFrame(data)

# Display the table in Streamlit
st.markdown("### Common Columns in Both Datasets")
st.write("The following table shows the common columns present in both datasets with their original names:")

st.dataframe(df)
