import streamlit as st
import pandas as pd
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, roc_auc_score, roc_curve, ConfusionMatrixDisplay
import xgboost as xgb
import joblib
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import cross_val_score

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

# Load the dataset (replace this with your actual dataset)
df = pd.read_csv("dataset1/final_df.csv")  # Your DataFrame
df = df.drop('education', axis=1)
df.dropna(inplace=True)

# Assuming 'heart_disease' is the target variable and all other columns are features
X = df.drop(columns=['heart_disease'])
y = df['heart_disease']

# Splitting the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

def load_model_from_github(url):
    response = requests.get(url)
    model = joblib.load(BytesIO(response.content))  # Use joblib for loading models
    return model

# URLs to your models on GitHub (use raw URLs for the pickle files)
xgb_model_url = "https://github.com/PrasadCoding/CMSE-830-Project/raw/refs/heads/master/models/xgb_model.pkl"
gb_model_url = "https://github.com/PrasadCoding/CMSE-830-Project/raw/refs/heads/master/models/gb_model.pkl"

# Load the models from GitHub
xgb_model = load_model_from_github(xgb_model_url)
gb_model = load_model_from_github(gb_model_url)

# Making predictions with XGBoost and Gradient Boosting
xgb_y_pred = xgb_model.predict(X_test)
gb_y_pred = gb_model.predict(X_test)

# Getting prediction probabilities for ROC AUC
xgb_y_prob = xgb_model.predict_proba(X_test)[:, 1]
gb_y_prob = gb_model.predict_proba(X_test)[:, 1]

# Calculating accuracy for both models
xgb_accuracy = accuracy_score(y_test, xgb_y_pred)
gb_accuracy = accuracy_score(y_test, gb_y_pred)

# Set up the page title and description
st.markdown("<h1 style='color: #FF4B4B;'>Heart Disease Model Evaluation</h1>", unsafe_allow_html=True)
st.write("Choose a model to see its evaluation metrics and confusion matrix:")

# Add a dropdown to select the model for evaluation
model_choice = st.selectbox("Choose a Model", options=["XGBoost", "Gradient Boosting"])

# Display evaluation and confusion matrix for the selected model
if model_choice == "XGBoost":
    # Display the XGBoost model evaluation
    st.write("**XGBoost Model Evaluation**")
    st.write(f"Accuracy: {xgb_accuracy * 100:.2f}%")

    # Classification report
    st.write("**Classification Report**")
    st.text(classification_report(y_test, xgb_y_pred))

    # Confusion matrix
    st.write("**Confusion Matrix**")
    cm_xgb = confusion_matrix(y_test, xgb_y_pred)
    cm_display_xgb = ConfusionMatrixDisplay(confusion_matrix=cm_xgb, display_labels=["No Disease", "Heart Disease"])
    cm_display_xgb.plot(cmap='Blues')
    st.pyplot(cm_display_xgb.figure_)

    # ROC AUC Score
    xgb_roc_auc = roc_auc_score(y_test, xgb_y_prob)
    st.write(f"**ROC AUC Score**: {xgb_roc_auc:.2f}")

    # Plot ROC curve
    fpr, tpr, _ = roc_curve(y_test, xgb_y_prob)
    plt.plot(fpr, tpr, label="XGBoost (AUC = {:.2f})".format(xgb_roc_auc))
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.title("ROC Curve - XGBoost")
    plt.legend()
    st.pyplot()

    # Feature importance plot
    xgb_importance = xgb_model.feature_importances_
    xgb_features = pd.DataFrame({"Feature": X.columns, "Importance": xgb_importance})
    xgb_features = xgb_features.sort_values(by="Importance", ascending=False)
    st.write("**Top 10 Feature Importance**")
    plt.figure(figsize=(12, 6))
    sns.barplot(x='Importance', y='Feature', data=xgb_features.head(10), color='blue')
    plt.title('Top 10 Feature Importance - XGBoost')
    plt.xlabel('Importance')
    plt.ylabel('Feature')
    plt.tight_layout()
    st.pyplot()

    # Cross-validation AUC scores
    xgb_cv_scores = cross_val_score(xgb_model, X, y, cv=5, scoring='roc_auc')
    st.write(f"**XGBoost Cross-Validation AUC Scores**: {xgb_cv_scores}")
    st.write(f"**Mean AUC Score**: {xgb_cv_scores.mean():.2f}")

elif model_choice == "Gradient Boosting":
    # Display the Gradient Boosting model evaluation
    st.write("**Gradient Boosting Model Evaluation**")
    st.write(f"Accuracy: {gb_accuracy * 100:.2f}%")

    # Classification report
    st.write("**Classification Report**")
    st.text(classification_report(y_test, gb_y_pred))

    # Confusion matrix
    st.write("**Confusion Matrix**")
    cm_gb = confusion_matrix(y_test, gb_y_pred)
    cm_display_gb = ConfusionMatrixDisplay(confusion_matrix=cm_gb, display_labels=["No Disease", "Heart Disease"])
    cm_display_gb.plot(cmap='Blues')
    st.pyplot(cm_display_gb.figure_)

    # ROC AUC Score
    gb_roc_auc = roc_auc_score(y_test, gb_y_prob)
    st.write(f"**ROC AUC Score**: {gb_roc_auc:.2f}")

    # Plot ROC curve
    fpr, tpr, _ = roc_curve(y_test, gb_y_prob)
    plt.plot(fpr, tpr, label="Gradient Boosting (AUC = {:.2f})".format(gb_roc_auc))
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.title("ROC Curve - Gradient Boosting")
    plt.legend()
    st.pyplot()

    # Feature importance plot
    gb_importance = gb_model.feature_importances_
    gb_features = pd.DataFrame({"Feature": X.columns, "Importance": gb_importance})
    gb_features = gb_features.sort_values(by="Importance", ascending=False)
    st.write("**Top 10 Feature Importance**")
    plt.figure(figsize=(12, 6))
    sns.barplot(x='Importance', y='Feature', data=gb_features.head(10), color='blue')
    plt.title('Top 10 Feature Importance - Gradient Boosting')
    plt.xlabel('Importance')
    plt.ylabel('Feature')
    plt.tight_layout()
    st.pyplot()

    # Cross-validation AUC scores
    gb_cv_scores = cross_val_score(gb_model, X, y, cv=5, scoring='roc_auc')
    st.write(f"**Gradient Boosting Cross-Validation AUC Scores**: {gb_cv_scores}")
    st.write(f"**Mean AUC Score**: {gb_cv_scores.mean():.2f}")
