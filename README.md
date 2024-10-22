# CMSE 830 Project Heart Disease Prediction

Heart Disease Prediction with Machine Learning
Table of Contents
Introduction
Project Structure
Features
Installation
Usage
Exploratory Data Analysis (EDA)
Modeling
Results
Conclusion
Future Work
License
Introduction
This project aims to predict the likelihood of individuals developing heart disease within ten years based on various clinical and lifestyle factors. Using machine learning techniques, we built a model that helps in risk stratification for heart disease, which is crucial in healthcare to prioritize preventive care.

Project Structure
bash
├── dataset/                   # Folder for dataset
├── Heart_Disease_Prediction.ipynb/              # Jupyter notebooks for analysis and model building
├── pages/                  # Streamlit pages for the app
├── streamlit_app.py                  # Main Streamlit app script
└── README.md               # Project README file
Features
The dataset consists of multiple medical and demographic features, which are key in predicting heart disease.

Feature Name	Description
age	Age of the individual
Sex_male	Gender (1: Male, 0: Female)
currentSmoker	Whether the individual is a current smoker (1: Yes, 0: No)
cigsPerDay	Number of cigarettes smoked per day
BPMeds	Whether the individual is on blood pressure medication (1 or 0)
prevalentStroke	Whether the individual has had a stroke (1 or 0)
prevalentHyp	Whether the individual has hypertension (1 or 0)
diabetes	Whether the individual has diabetes (1 or 0)
totChol	Total cholesterol level
sysBP	Systolic blood pressure
diaBP	Diastolic blood pressure
BMI	Body Mass Index
heartRate	Heart rate
glucose	Glucose level
TenYearCHD	Whether the individual develops heart disease in 10 years (1 or 0)
Installation
To run this project locally, ensure you have Python 3.9 or higher installed and follow these steps:

Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/heart-disease-prediction.git
cd heart-disease-prediction
Install the required Python packages:

bash
Copy code
pip install -r requirements.txt
Launch the Streamlit app:

bash
Copy code
streamlit run app.py
Usage
EDA Overview: Explore the data through descriptive statistics, missing value heatmaps, and customizable visualizations such as histograms, box plots, and scatter plots.
BMI Calculator: A separate page to calculate and visualize BMI distribution for individuals.
Heart Disease Risk Prediction: Input user details such as age, blood pressure, and cholesterol levels to get a prediction of heart disease risk using a Random Forest model.
Exploratory Data Analysis (EDA)
In the EDA phase, we explored the distribution of key features, investigated correlations, and examined missing data. We used visualizations like:

Histograms
Box plots
Heatmaps for missing data
Parallel plots (via HiPlot) to explore multidimensional relationships.
Modeling
Used several machine learning models, with Random Forest performing the best for predicting heart disease risk. The features were pre-processed, and categorical variables were encoded. 

Results
The Random Forest model achieved an accuracy of 82%. The confusion matrix and classification report are included for detailed evaluation of the model's performance.

Conclusion
The model demonstrates that features like systolic blood pressure, cholesterol levels, and BMI play crucial roles in determining heart disease risk. The app provides users with an interactive interface to calculate their risk based on various input features.

Future Work
Some future improvements and extensions of this project include:

Integrating additional datasets to improve prediction accuracy.
Implementing more sophisticated models like XGBoost or Neural Networks.
