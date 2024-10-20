import streamlit as st
import pandas as pd
import numpy as np


df = pd.read_csv("dataset/heart_disease.csv")
# Dataset description section
st.title("My Analysis")

st.header("Dataset Description")
st.markdown("""
The dataset used in this analysis is focused on heart disease prediction. It contains health and demographic information about individuals, including features such as Sex_male, age, currentSmoker, cigsPerDay, BPMeds, prevalentStroke, prevalentHyp, diabetes, totChol, sysBP, diaBP, BMI, heartRate, glucose, TenYearCHD.
""")

# Add dataset overview
st.subheader("Dataset Overview")
st.markdown("""
- **Number of rows**: 4240 
- **Number of features**: 15
- **Target variable**: `TenYearCHD` – whether an individual will develop coronary heart disease within 10 years.
""")

# Display a table of key features
st.subheader("Features")
st.table({
    'Feature Name': [
        'Sex_male', 'age', 'currentSmoker', 'cigsPerDay', 'BPMeds', 'prevalentStroke', 
        'prevalentHyp', 'diabetes', 'totChol', 'sysBP', 'diaBP', 'BMI', 
        'heartRate', 'glucose', 'TenYearCHD'
    ],
    'Description': [
        'Gender (1: Male, 0: Female)',
        'Age of the individual',
        'Whether the individual is a current smoker (1 or 0)',
        'Cigarettes smoked per day by the individual',
        'Whether the individual is on blood pressure medication (1 or 0)',
        'Whether the individual has had a stroke (1 or 0)',
        'Whether the individual has hypertension (1 or 0)',
        'Whether the individual has diabetes (1 or 0)',
        'Total cholesterol level (mg/dL)',
        'Systolic blood pressure (mmHg)',
        'Diastolic blood pressure (mmHg)',
        'Body Mass Index (BMI)',
        'Heart rate (beats per minute)',
        'Glucose level (mg/dL)',
        'Whether the person develops heart disease in 10 years (1 or 0)'
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

st.header("Missing Values Analysis")

# Brief introduction
st.write("""
Understanding missing values is crucial in data analysis as they can affect the performance of models and the overall insights we derive from the data. 
Here, we check the number of missing values in each feature of the dataset to determine if any imputation or data cleaning is necessary.
""")

# Display the missing values count
missing_values = df.isnull().sum()
st.write(missing_values)

st.subheader("Handling Missing Data")

st.write("""
After analyzing the missing values in the dataset, I have decided to drop rows with missing data. Since this is medical data, many of the features are categorical, 
and filling missing values with averages (mean or median) would not provide meaningful or accurate results. 
For example, filling in someone's medical measurements, like cholesterol or glucose levels, based on average values could lead to inaccurate insights or predictions. 
Therefore, removing the missing data will maintain the integrity and reliability of the analysis.
""")

st.subheader("Descriptive Statistics")

st.write("""
The table below provides an overview of the key statistical metrics for each feature in the dataset, including the count, mean, standard deviation, 
minimum, maximum, and the 25th, 50th, and 75th percentiles. This helps us understand the central tendencies and spread of the data, 
which will inform our decision-making process during the analysis.
""")

st.dataframe(df.describe())

# Data Type Conversion Section
st.subheader("Data Type Conversion")

st.write("""
In this section, we analyze the dataset and ensure that the variable types are appropriate for the predictive modeling process.

We have identified several variables in our dataset that should be treated as categorical. These include:

- **Sex_male**: Indicates whether the individual is male (1) or not (0).
- **currentSmoker**: Indicates whether the individual is a current smoker (1) or not (0).
- **BPMeds**: Indicates whether the individual is on blood pressure medication (1) or not (0).
- **prevalentStroke**: Indicates whether the individual has a history of stroke (1) or not (0).
- **prevalentHyp**: Indicates whether the individual has hypertension (1) or not (0).
- **diabetes**: Indicates whether the individual has diabetes (1) or not (0).
- **TenYearCHD**: Indicates whether the individual is predicted to have coronary heart disease in the next 10 years (1) or not (0).

To optimize our analysis, these variables have been converted to categorical data types. This allows us to effectively utilize them in our machine learning models, as categorical variables can be better handled during model training and evaluation.
""")

# Display Data Types Before Conversion
st.subheader("Data Types Before Conversion")
st.code("df.dtypes")
st.dataframe(df.dtypes)

# Convert categorical variables
category_list = ['Sex_male', 'currentSmoker', 'BPMeds', 'prevalentStroke', 'prevalentHyp', 'diabetes', 'TenYearCHD']
for i in category_list:
    df[i] = df[i].astype('category')

# Display Data Types After Conversion
st.subheader("Data Types After Conversion")
st.code("df.dtypes")
st.dataframe(df.dtypes)
