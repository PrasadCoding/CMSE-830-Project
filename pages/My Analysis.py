import streamlit as st

# Dataset description section
st.title("My Analysis")

st.header("Dataset Description")
st.markdown("""
The dataset used in this analysis is focused on heart disease prediction. It contains health and demographic information about individuals, including features such as age, gender, blood pressure, cholesterol levels, smoking status, and others.
""")

# Add dataset overview
st.subheader("Dataset Overview")
st.markdown("""
- **Number of rows**: X (replace with actual number)
- **Number of features**: Y (replace with actual number)
- **Target variable**: `TenYearCHD` – whether an individual will develop coronary heart disease within 10 years.
""")

# Display a table of key features
st.subheader("Key Features")
st.table({
    'Feature Name': ['age', 'sex', 'currentSmoker', 'totChol', 'sysBP', 'BMI', 'TenYearCHD'],
    'Description': [
        'Age of the individual',
        'Gender (1: Male, 0: Female)',
        'Whether the individual is a current smoker (1 or 0)',
        'Total cholesterol level',
        'Systolic blood pressure',
        'Body Mass Index',
        'Whether the person develops heart disease in 10 years'
    ]
})

# Goal of the analysis section
st.header("Goal of the Analysis")
st.markdown("""
The primary goal of this project is to develop a predictive model that can assess the risk of an individual developing coronary heart disease (CHD) within the next 10 years. To achieve this, we will:

1. Perform **Exploratory Data Analysis (EDA)** to uncover patterns and relationships in the data.
2. Address **missing data** using appropriate techniques.
3. Develop a **machine learning model** for heart disease prediction.
4. Assess and visualize the performance of the model.
""")

