import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler

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
# Count of missing values
missing_values = df.isnull().sum()
st.dataframe(missing_values[missing_values > 0])  # Display only features with missing values

# Plotting heatmap of missing data
st.write("### Heatmap of Missing Data")
plt.figure(figsize=(10, 6))
sns.heatmap(df.isnull(), cbar=False, cmap='viridis')
plt.title('Heatmap of Missing Data in Heart Disease Dataset')

# Show the heatmap in Streamlit
st.pyplot(plt)
plt.close() 

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
category_list = ['male', 'currentSmoker', 'BPMeds', 'prevalentStroke', 'prevalentHyp', 'diabetes', 'TenYearCHD']
for i in category_list:
    df[i] = df[i].astype('category')

# Display Data Types After Conversion
st.subheader("Data Types After Conversion")
st.code("df.dtypes")
st.dataframe(df.dtypes)

# Scaling Numeric Features Section
st.subheader("Feature Scaling")
st.write("""
Feature scaling is an essential preprocessing step in machine learning. It helps to standardize the range of independent variables or features 
of data. In this analysis, we will standardize the numeric features using the StandardScaler, which will transform the features to have a mean of 0 and a standard deviation of 1.
""")

# Selecting numeric features
numeric_features = df.select_dtypes(include=['float64', 'int64'])

# Standardize the features
scaler = StandardScaler()
scaled_features = scaler.fit_transform(numeric_features)

# Create a DataFrame for the scaled features
scaled_features_df = pd.DataFrame(scaled_features, columns=numeric_features.columns)
scaled_features_df['TenYearCHD'] = df['TenYearCHD'].values

# Display the scaled features DataFrame
st.write("### Scaled Features")
st.dataframe(scaled_features_df)


# Encoding Section
st.subheader("Encoding of Categorical Variables")
st.write("""
In this analysis, we have determined that the categorical variables in our dataset have already been appropriately encoded. 
Therefore, no additional encoding steps are required at this stage. This is beneficial as it allows us to proceed directly to modeling 
without the need for further preprocessing of categorical features.
""")
