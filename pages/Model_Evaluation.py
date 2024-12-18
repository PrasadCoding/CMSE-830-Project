import streamlit as st
import pandas as pd
import xgboost as xgb
import joblib
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score, roc_curve, ConfusionMatrixDisplay
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import cross_val_score
import requests
from io import BytesIO

# Set background image
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

# Load the dataset (assuming it's final_df in your case)
final_df = pd.read_csv("dataset1/final_df.csv", index_col=0)

# Separate features and target
X = final_df.drop('heart_disease', axis=1)
y = final_df['heart_disease']

def load_model_from_github(url):
    response = requests.get(url)
    model = joblib.load(BytesIO(response.content))  # Use joblib for loading models
    return model

# URLs to your models on GitHub (use raw URLs for the pickle files)
xgb_model_url = "https://github.com/PrasadCoding/CMSE-830-Project/raw/refs/heads/master/models/xgb_model.pkl"
gb_model_url = "https://github.com/PrasadCoding/CMSE-830-Project/raw/refs/heads/master/models/gb_model.pkl"
rf_model_url = "https://github.com/PrasadCoding/CMSE-830-Project/raw/refs/heads/master/models/rf_model1.pkl"  # Add the Random Forest model URL

# Load the models from GitHub
xgb_model = load_model_from_github(xgb_model_url)
gb_model = load_model_from_github(gb_model_url)
rf_model = load_model_from_github(rf_model_url)  # Load the Random Forest model

# Function to display the classification report as a nicely formatted table
def display_classification_report(y_true, y_pred, model_name):
    """
    Display classification report as a table.
    """
    st.markdown(f"### **{model_name} Classification Report**")
    report_dict = classification_report(y_true, y_pred, target_names=["No Disease", "Heart Disease"], output_dict=True)
    report_df = pd.DataFrame(report_dict).transpose()
    report_df.index.name = "Metrics"
    report_df.reset_index(inplace=True)
    st.table(report_df)

# Function to plot the ROC curve
def plot_roc_curve(fpr, tpr, auc, model_name):
    fig, ax = plt.subplots()
    ax.plot(fpr, tpr, label=f"{model_name} (AUC = {auc:.2f})")
    ax.set_xlabel("False Positive Rate")
    ax.set_ylabel("True Positive Rate")
    ax.set_title(f"ROC Curve - {model_name}")
    ax.legend()
    st.pyplot(fig)

# Function to plot feature importances
def plot_feature_importance(importance, features, model_name):
    importance_df = pd.DataFrame({"Feature": features, "Importance": importance})
    importance_df = importance_df.sort_values(by="Importance", ascending=False)
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(x='Importance', y='Feature', data=importance_df.head(10), color='blue', ax=ax)
    ax.set_title(f'Top 10 Feature Importance - {model_name}')
    ax.set_xlabel('Importance')
    ax.set_ylabel('Feature')
    plt.tight_layout()
    st.pyplot(fig)

# Function for Cross-validation AUC scores
def plot_cv_scores(cv_scores, model_name):
    st.write(f"{model_name} Cross-Validation AUC Scores: {cv_scores}")
    st.write(f"Mean AUC Score: {cv_scores.mean()}")

# Evaluation for XGBoost, Gradient Boosting, and Random Forest models
def evaluate_model(model, model_name):
    y_pred = model.predict(X)
    y_prob = model.predict_proba(X)[:, 1]

    # Display Classification Report
    display_classification_report(y, y_pred, model_name)

    # Confusion Matrix
    cm = confusion_matrix(y, y_pred)
    cm_display = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=["No Disease", "Heart Disease"])
    cm_display.plot(cmap='Blues')
    st.pyplot(cm_display.figure_)

    # ROC AUC Score
    auc_score = roc_auc_score(y, y_prob)
    st.write(f"**{model_name} ROC AUC Score:** {auc_score:.2f}")

    # ROC Curve
    fpr, tpr, _ = roc_curve(y, y_prob)
    plot_roc_curve(fpr, tpr, auc_score, model_name)

    # Feature Importance
    importance = model.feature_importances_
    plot_feature_importance(importance, X.columns, model_name)

    # Cross-Validation AUC Scores
    cv_scores = cross_val_score(model, X, y, cv=5, scoring='roc_auc')
    plot_cv_scores(cv_scores, model_name)

# Set up the page title and description
st.markdown("<h1 style='color: #FF4B4B;'>Heart Disease Model Evaluation</h1>", unsafe_allow_html=True)
st.write("Choose a model to see its evaluation metrics and confusion matrix:")

# Dropdown to select the model
model_choice = st.selectbox("Choose a Model", options=["XGBoost", "Gradient Boosting", "Random Forest"])

# Display evaluation and confusion matrix for the selected model
if model_choice == "XGBoost":
    st.write("**Evaluating XGBoost Model**")
    evaluate_model(xgb_model, "XGBoost")

elif model_choice == "Gradient Boosting":
    st.write("**Evaluating Gradient Boosting Model**")
    evaluate_model(gb_model, "Gradient Boosting")

elif model_choice == "Random Forest":
    st.write("**Evaluating Random Forest Model**")
    evaluate_model(rf_model, "Random Forest")
