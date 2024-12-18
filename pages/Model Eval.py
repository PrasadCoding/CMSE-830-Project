import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay

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

# Center layout
st.set_page_config(layout="centered")

# Path to your background image file on GitHub (use the raw URL)
image_url = 'https://raw.githubusercontent.com/PrasadCoding/CMSE-830-Project/refs/heads/master/images/bg43.png'  # Replace with your raw URL
set_bg_image(image_url)

# Load the dataset (replace this with your actual dataset)
df = pd.read_csv("dataset/heart_disease.csv")  # Your DataFrame
df = df.drop('education', axis=1)
df.dropna(inplace=True)

# Assuming 'TenYearCHD' is the target variable and all other columns are features
X = df.drop(columns=['TenYearCHD'])
y = df['TenYearCHD']

# Load pre-trained models
rf_model = joblib.load("https://github.com/PrasadCoding/CMSE-830-Project/raw/refs/heads/master/models_midterm/Random%20Forest_model.pkl")  # Replace with the path to your Random Forest model
lr_model = joblib.load("https://github.com/PrasadCoding/CMSE-830-Project/raw/refs/heads/master/models_midterm/Logistic%20Regression_model.pkl")  # Replace with the path to your Logistic Regression model
xgboost_model = joblib.load("https://github.com/PrasadCoding/CMSE-830-Project/raw/refs/heads/master/models_midterm/XGBoost_model.pkl")  # Replace with the path to your XGBoost model

# Making predictions with Random Forest, Logistic Regression, and XGBoost
rf_y_pred = rf_model.predict(X)
lr_y_pred = lr_model.predict(X)
xgboost_y_pred = xgboost_model.predict(X)

# Calculating accuracy
rf_accuracy = accuracy_score(y, rf_y_pred)
lr_accuracy = accuracy_score(y, lr_y_pred)
xgboost_accuracy = accuracy_score(y, xgboost_y_pred)

# Feature importance (for Random Forest and XGBoost)
rf_feature_importances = rf_model.feature_importances_
xgboost_feature_importances = xgboost_model.feature_importances_

# Create feature importance DataFrame for Random Forest
rf_feature_importance_df = pd.DataFrame({
    'Feature': X.columns,
    'Importance': rf_feature_importances
}).sort_values(by='Importance', ascending=False)

# Create feature importance DataFrame for XGBoost
xgboost_feature_importance_df = pd.DataFrame({
    'Feature': X.columns,
    'Importance': xgboost_feature_importances
}).sort_values(by='Importance', ascending=False)

# Set up the page title and description
st.markdown("<h1 style='color: #FF4B4B;'>Heart Disease Model Evaluation</h1>", unsafe_allow_html=True)
st.write("Choose a model to see its evaluation metrics and confusion matrix:")

# Add a dropdown to select the model for evaluation
model_choice = st.selectbox("Choose a Model", options=["Random Forest", "Logistic Regression", "XGBoost"])

# Display evaluation and confusion matrix for the selected model
if model_choice == "Random Forest":
    # Display the Random Forest model evaluation
    st.write("**Random Forest Model Evaluation**")
    st.write(f"Accuracy: {rf_accuracy * 100:.2f}%")

    # Display the confusion matrix
    cm_rf = confusion_matrix(y, rf_y_pred)
    cm_display_rf = ConfusionMatrixDisplay(confusion_matrix=cm_rf, display_labels=["No Disease", "Heart Disease"])
    cm_display_rf.plot(cmap='Blues')
    st.pyplot(cm_display_rf.figure_)

    # Display feature importance
    st.write("**Feature Importance (Random Forest)**")
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.barplot(x='Importance', y='Feature', data=rf_feature_importance_df, palette="coolwarm", ax=ax)
    ax.set_title("Feature Importance (Random Forest)", fontsize=16)
    ax.set_xlabel("Importance", fontsize=14)
    ax.set_ylabel("Feature", fontsize=14)
    st.pyplot(fig)

elif model_choice == "Logistic Regression":
    # Display the Logistic Regression model evaluation
    st.write("**Logistic Regression Model Evaluation**")
    st.write(f"Accuracy: {lr_accuracy * 100:.2f}%")

    # Display the confusion matrix
    cm_lr = confusion_matrix(y, lr_y_pred)
    cm_display_lr = ConfusionMatrixDisplay(confusion_matrix=cm_lr, display_labels=["No Disease", "Heart Disease"])
    cm_display_lr.plot(cmap='Blues')
    st.pyplot(cm_display_lr.figure_)

elif model_choice == "XGBoost":
    # Display the XGBoost model evaluation
    st.write("**XGBoost Model Evaluation**")
    st.write(f"Accuracy: {xgboost_accuracy * 100:.2f}%")

    # Display the confusion matrix
    cm_xgboost = confusion_matrix(y, xgboost_y_pred)
    cm_display_xgboost = ConfusionMatrixDisplay(confusion_matrix=cm_xgboost, display_labels=["No Disease", "Heart Disease"])
    cm_display_xgboost.plot(cmap='Blues')
    st.pyplot(cm_display_xgboost.figure_)

    # Display feature importance
    st.write("**Feature Importance (XGBoost)**")
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.barplot(x='Importance', y='Feature', data=xgboost_feature_importance_df, palette="coolwarm", ax=ax)
    ax.set_title("Feature Importance (XGBoost)", fontsize=16)
    ax.set_xlabel("Importance", fontsize=14)
    ax.set_ylabel("Feature", fontsize=14)
    st.pyplot(fig)

# Add footer to display additional knowledge
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown(
    """<div style='text-align: center;'>
    <h4>Insights:</h4>
    <p>The Random Forest model provides feature importance, enabling interpretability and highlighting key risk factors for heart disease.</p>
    <p>Logistic Regression offers simplicity and is well-suited for binary classification tasks.</p>
    <p>XGBoost is a powerful gradient boosting model that often outperforms other models in classification tasks.</p>
    </div>""",
    unsafe_allow_html=True
)
