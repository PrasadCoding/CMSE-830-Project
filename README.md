
# Heart Disease Prediction with Machine Learning

## Streamlit App

**[Open in Streamlit]([https://your-app-url](https://cmse-heart-disease-pred.streamlit.app/))**

## Table of Contents
- [Introduction](#introduction)
- [Project Structure](#project-structure)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
- [Modeling](#modeling)
- [Results](#results)
- [Conclusion](#conclusion)
- [Future Work](#future-work)

---

## Introduction
This project aims to predict the likelihood of individuals developing heart disease within ten years based on various clinical and lifestyle factors. Using machine learning techniques, we built a model that helps in risk stratification for heart disease, which is crucial in healthcare to prioritize preventive care.

## Project Structure
```
├── dataset/                   # Folder for dataset
├── Heart_Disease_Prediction.ipynb/              # Jupyter notebooks for analysis and model building
├── pages/                  # Streamlit pages for the app
├── streamlit_app.py                  # Main Streamlit app script
└── README.md               # Project README file
```

## Features
The dataset consists of multiple medical and demographic features, which are key in predicting heart disease.

| **Feature Name**     | **Description**                                                      |
|----------------------|----------------------------------------------------------------------|
| `age`                | Age of the individual                                                |
| `Sex_male`           | Gender (1: Male, 0: Female)                                          |
| `currentSmoker`      | Whether the individual is a current smoker (1: Yes, 0: No)           |
| `cigsPerDay`         | Number of cigarettes smoked per day                                  |
| `BPMeds`             | Whether the individual is on blood pressure medication (1 or 0)      |
| `prevalentStroke`    | Whether the individual has had a stroke (1 or 0)                     |
| `prevalentHyp`       | Whether the individual has hypertension (1 or 0)                     |
| `diabetes`           | Whether the individual has diabetes (1 or 0)                         |
| `totChol`            | Total cholesterol level                                              |
| `sysBP`              | Systolic blood pressure                                              |
| `diaBP`              | Diastolic blood pressure                                             |
| `BMI`                | Body Mass Index                                                      |
| `heartRate`          | Heart rate                                                           |
| `glucose`            | Glucose level                                                       |
| `TenYearCHD`         | Whether the individual develops heart disease in 10 years (1 or 0)   |

## Installation
To run this project locally, follow these steps:

1. Clone this repository:
   ```
   git clone https://github.com/your-username/heart-disease-prediction.git
   ```

2. Navigate to the project directory:
   ```
   cd heart-disease-prediction
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Launch the Streamlit app:
   ```
   streamlit run app.py
   ```

## Usage
1. Explore the dataset using the EDA tools provided.
2. Use the prediction page to input medical data and predict the likelihood of heart disease.
3. Customize the visualizations by selecting different parameters.

## Exploratory Data Analysis (EDA)
The EDA section provides insights into the dataset through various visualizations like histograms, box plots, scatter plots, and more. It also handles missing data, outliers, and distribution of features.

## Modeling
The project uses machine learning models such as Random Forest, Logistic Regression, and Support Vector Machines to predict heart disease risk. Each model was evaluated on key metrics such as accuracy, precision, and recall.

## Results
The Random Forest model was the best-performing model, achieving an accuracy of 85%. The results from this model are further explored using confusion matrices and ROC curves to analyze the trade-offs between precision and recall.

## Conclusion
By using the available clinical and demographic data, the project successfully built a model to predict heart disease risk. The interactive Streamlit app allows users to explore the dataset and make predictions.

## Future Work
Future improvements could include:
- Adding more features related to diet and exercise.
- Testing additional machine learning models.
- Improving the user interface and experience of the app.
