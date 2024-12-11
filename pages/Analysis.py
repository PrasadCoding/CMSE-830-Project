import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import plotly.express as px


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
df_combined = pd.read_csv('dataset1/merged_data.csv', index_col = 0)

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
st.markdown("### Merged Data")
st.dataframe(df_combined)

st.subheader("Handling Missing Values")
st.write("The following shows the number of missing values in each column of the combined dataset:")

# Display the count of missing values in each column
missing_values = df_combined.isnull().sum()
st.write(missing_values)

# Creating the heatmap of missing data
missing_data = df_combined.isnull()

# Plot using seaborn and convert to plotly for interactivity
plt.figure(figsize=(12, 8))
sns.heatmap(missing_data, cmap='magma', cbar=False, yticklabels=False)
plt.title("Heatmap of Missing Values", fontsize=16, pad=20)


# Alternatively, to use Plotly for an interactive heatmap
# Reshaping the missing data into a long format for Plotly
missing_data_long = missing_data.reset_index().melt(id_vars=["index"]).rename(columns={"index": "Row", "variable": "Column", "value": "Missing"})
missing_data_long["Missing"] = missing_data_long["Missing"].apply(lambda x: 1 if x else 0)

# Plotly heatmap
fig = px.density_heatmap(missing_data_long, x="Column", y="Row", z="Missing", 
                         color_continuous_scale='magma', title="Interactive Heatmap of Missing Values")
st.plotly_chart(fig)


from sklearn.experimental import enable_iterative_imputer 
from sklearn.impute import IterativeImputer

# Imputing missing values using Iterative Imputer
iterative_imputer = IterativeImputer(max_iter=10, random_state=0)
df_combined_imputed = pd.DataFrame(iterative_imputer.fit_transform(df_combined), columns=df_combined.columns)

# Displaying the number of missing values after imputation
st.title("Handling Missing Values - Iterative Imputer")
st.write("The Iterative Imputer is a machine learning-based imputation technique that models each feature with missing values as a function of the other features and iteratively predicts the missing values. This method is more sophisticated than simple imputation strategies (such as mean or median imputation) because it takes into account the relationships between the features.")

# Display null values count after imputation
missing_values_after_imputation = df_combined_imputed.isnull().sum()
st.write(missing_values_after_imputation)

from sklearn.preprocessing import StandardScaler, MinMaxScaler

# Data Transformation: Standard Scaling and Min-Max Scaling
numeric_columns = ['age', 'bmi', 'blood_glucose_level']

# Standard Scaling
standard_scaler = StandardScaler()
df_combined[numeric_columns] = standard_scaler.fit_transform(df_combined[numeric_columns])

# Displaying the data after Standard Scaling
st.title("Data Transformation")

st.markdown("Standard Scaling: The StandardScaler standardizes the numeric columns by removing the mean and scaling to unit variance. This is useful when the features have different scales, and you want to ensure that they contribute equally to machine learning models.")
st.markdown("Min-Max Scaling: The MinMaxScaler scales the numeric columns to a specific range (usually 0 to 1). This is particularly useful when features have varying scales and you need a consistent range for certain algorithms that are sensitive to the range of input features, such as neural networks.")
st.write("The following table shows the data after applying Standard Scaling:")

# Displaying the transformed data
st.write(df_combined[numeric_columns].head())


# Function to handle outliers using IQR method
def handle_outliers_iqr(df, columns):
    for col in columns:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR

        # Replace outliers with the median value of the column
        outliers = (df[col] < lower_bound) | (df[col] > upper_bound)
        if outliers.any():
            df.loc[outliers, col] = df[col].median()
    return df

# Function to plot boxplots
def plot_boxplots(df, columns, title):
    plt.figure(figsize=(12, 6))
    for i, col in enumerate(columns, 1):
        plt.subplot(1, len(columns), i)
        sns.boxplot(y=df[col], color='lightblue')
        plt.title(f'{col}')
    plt.suptitle(title, fontsize=16)
    plt.tight_layout()
    st.pyplot(plt)

# Columns to analyze
numeric_columns = ['age', 'bmi', 'blood_glucose_level']

# Streamlit UI: Display explanation and boxplots before and after handling outliers
st.title("Outlier Handling")
st.write("""
    In this section, we use the **IQR (Interquartile Range)** method to identify and handle outliers. The IQR method calculates the 
    range between the first (Q1) and third (Q3) quartiles, and any values outside the range of `Q1 - 1.5 * IQR` to `Q3 + 1.5 * IQR` 
    are considered outliers. These outliers are then replaced with the median value of the respective column.
""")

# Plot before handling outliers
st.write("Boxplots Before Handling Outliers:")
plot_boxplots(df_combined, numeric_columns, "Boxplots Before Handling Outliers")

# Apply IQR method to handle outliers
df_combined = handle_outliers_iqr(df_combined, numeric_columns)

# Plot after handling outliers
st.write("Boxplots After Handling Outliers:")
plot_boxplots(df_combined, numeric_columns, "Boxplots After Handling Outliers")



st.subheader("EDA")

st.write("""
    EDA on the dataset. 
    We will create **histograms** to understand the distribution and spread of the data. 
    The histograms show the frequency distribution of the variables.
""")
st.subheader("Histogram")
# Select numeric columns
# Select numeric columns
numeric_cols = df_combined.select_dtypes(include=['float64', 'int64']).columns

# Dropdown to select feature
selected_col = st.selectbox("Select a numeric feature to plot the histogram:", numeric_cols)

# Plot selected feature's histogram with Plotly
st.subheader(f'Histogram of {selected_col}')

# Plot histogram using Plotly for interactivity
fig = px.histogram(df_combined, x=selected_col, nbins=30, title=f'Histogram of {selected_col}', marginal="box")
st.plotly_chart(fig)


# Streamlit UI: Title and explanation
st.subheader("Scatterplot")
st.write("""
    Now, we perform bivariate analysis on the numeric variables by plotting **scatter plots**.
    The scatter plot helps us examine the relationship between two numeric variables.
""")

# Select numeric columns
numeric_cols = df_combined.select_dtypes(include=['float64', 'int64']).columns

# Dropdowns to select features for scatter plot
x_col = st.selectbox("Select the feature for the x-axis:", numeric_cols)
y_col = st.selectbox("Select the feature for the y-axis:", numeric_cols)

# Plot selected features' scatter plot with Plotly
st.subheader(f'Scatter Plot between {x_col} and {y_col}')

# Create scatter plot using Plotly
fig = px.scatter(df_combined, x=x_col, y=y_col, title=f'Scatter Plot between {x_col} and {y_col}')
st.plotly_chart(fig)


st.subheader("Pairplot")
st.write("""
    This is an interactive pairplot visualizing relationships between numeric features with hue by 'heart_disease'.
    You can interact with the plot to zoom, hover over data points, and more.
""")

sns.pairplot(df_combined, hue='heart_disease', diag_kind='kde')

# Display the plot in Streamlit
st.pyplot(plt)

