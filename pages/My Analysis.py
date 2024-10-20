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

# Univariate Analysis for Numeric Variables
st.subheader("Univariate Analysis for Numeric Variables")
st.write("""
In this section, we perform univariate analysis to explore the distribution of numeric variables in the dataset. 
Histograms will provide insights into the frequency distribution of each feature, allowing us to identify patterns and potential outliers.
""")

# Generate histograms
numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns

# Create a figure for histograms
plt.figure(figsize=(20, 15))

for i, col in enumerate(numeric_cols):
    # Histogram
    plt.subplot(4, 4, i + 1)
    sns.histplot(df[col], kde=True)
    plt.title(f'Histogram of {col}')
    plt.xlabel(col)
    plt.ylabel('Frequency')

plt.tight_layout()

# Show the histograms in Streamlit
st.pyplot(plt)
plt.close()  # Close the plot to prevent duplicate display

st.subheader("Univariate Analysis Insights")
st.write("""
The histograms above provide valuable insights into the distribution of numeric variables in our heart disease dataset:

1. **Age**: The age distribution appears to be roughly normal, with a peak around 60 years, indicating that this is the age range where heart disease prevalence may be higher.

2. **Education**: The education variable shows a distinct bar distribution, suggesting that most individuals have achieved either low or moderate levels of education, which could impact health outcomes.

3. **Cigarettes Per Day**: The distribution of cigarettes smoked per day indicates a significant number of individuals who are non-smokers, with a few outliers who smoke heavily, highlighting the importance of smoking as a risk factor.

4. **Total Cholesterol**: The total cholesterol levels show a right-skewed distribution, with most individuals having levels below 300, but with a few cases exceeding this threshold, indicating potential health risks.

5. **Systolic and Diastolic Blood Pressure**: Both blood pressure measures exhibit a normal distribution, but with noticeable peaks at lower values, suggesting a trend towards healthier blood pressure levels among the majority.

6. **Body Mass Index (BMI)**: The BMI distribution is left-skewed, with a concentration of individuals falling below the average range of 25, which may indicate a healthier population in terms of weight.

7. **Heart Rate**: The histogram of heart rate displays a more uniform distribution, suggesting a diverse range of heart rates among individuals, which may correlate with varying fitness levels.

8. **Glucose Levels**: Glucose levels are highly right-skewed, with most individuals showing low levels and a few outliers with elevated glucose levels, indicating potential health concerns such as prediabetes or diabetes.

Overall, these distributions provide important context for understanding the demographic and health-related characteristics of the individuals in this dataset. They can inform our modeling decisions and highlight potential areas for further investigation in relation to heart disease risk factors.
""")

st.subheader("Class Distribution of Ten-Year Coronary Heart Disease Risk")
st.write("""
The bar chart displays the distribution of the **Ten-Year Coronary Heart Disease Risk** variable, illustrating the number of individuals classified as either at risk or not at risk for coronary heart disease over the next decade.

1. **Not at Risk**: The majority of individuals fall into the 'not at risk' category, indicating a healthier population overall. This suggests that a significant portion of the dataset may have favorable health indicators and lifestyle choices.

2. **At Risk**: A smaller proportion of individuals are classified as 'at risk,' highlighting the importance of targeted interventions for this group. Understanding the characteristics of these individuals can help identify risk factors and develop strategies to mitigate heart disease risk.

Overall, this class distribution provides essential context for modeling and analysis, emphasizing the need to address the risk factors associated with coronary heart disease in the at-risk population.
""")

# Generate the count plot for Ten-Year Coronary Heart Disease Risk
plt.figure(figsize=(8, 5))
sns.countplot(x='TenYearCHD', data=df)
plt.title('Class Distribution of Ten-Year Coronary Heart Disease Risk')
plt.xlabel('Ten-Year Coronary Heart Disease Risk (0 = Not at Risk, 1 = At Risk)')
plt.ylabel('Count')

# Show the count plot in Streamlit
st.pyplot(plt)
plt.close()  # Close the plot to prevent duplicate display


# Display class distribution before applying SMOTE
st.subheader("Class Distribution Before Applying SMOTE")
st.write(df['TenYearCHD'].value_counts())

# Plotting class distribution before SMOTE
plt.figure(figsize=(8, 5))
sns.countplot(x='TenYearCHD', data=df)
plt.title('Class Distribution of Ten-Year Coronary Heart Disease Risk (Before SMOTE)')
plt.xlabel('Ten-Year Coronary Heart Disease Risk (0 = Not at Risk, 1 = At Risk)')
plt.ylabel('Count')
st.pyplot(plt)
plt.close()

# Applying SMOTE
from imblearn.over_sampling import SMOTE

X = df.drop('TenYearCHD', axis=1)  # Features
y = df['TenYearCHD']                # Target variable

smote = SMOTE(random_state=42)
X_resampled, y_resampled = smote.fit_resample(X, y)

# Display class distribution after applying SMOTE
st.subheader("Class Distribution After Applying SMOTE")
st.write(pd.Series(y_resampled).value_counts())

# Plotting class distribution after SMOTE
plt.figure(figsize=(8, 5))
sns.countplot(x=y_resampled)
plt.title('Class Distribution of Ten-Year Coronary Heart Disease Risk (After SMOTE)')
plt.xlabel('Ten-Year Coronary Heart Disease Risk (0 = Not at Risk, 1 = At Risk)')
plt.ylabel('Count')
st.pyplot(plt)
plt.close()

