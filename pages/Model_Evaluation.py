import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
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

# Splitting the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Creating the Random Forest Classifier and Logistic Regression models
rf_model = RandomForestClassifier(random_state=42)
lr_model = LogisticRegression(max_iter=1000, random_state=42)

# Fitting the models
rf_model.fit(X_train, y_train)
lr_model.fit(X_train, y_train)

# Making predictions with Random Forest and Logistic Regression
rf_y_pred = rf_model.predict(X_test)
lr_y_pred = lr_model.predict(X_test)

# Calculating accuracy
rf_accuracy = accuracy_score(y_test, rf_y_pred)
lr_accuracy = accuracy_score(y_test, lr_y_pred)

# Set up the page title and description
st.markdown("<h1 style='color: #FF4B4B;'>Heart Disease Model Evaluation</h1>", unsafe_allow_html=True)
st.write("Choose a model to see its evaluation metrics and confusion matrix:")

# Add a dropdown to select the model for evaluation
model_choice = st.selectbox("Choose a Model", options=["Random Forest", "Logistic Regression"])

# Display evaluation and confusion matrix for the selected model
if model_choice == "Random Forest":
    # Display the Random Forest model evaluation
    st.write("**Random Forest Model Evaluation**")
    st.write(f"Accuracy: {rf_accuracy * 100:.2f}%")

    # Display the confusion matrix
    cm_rf = confusion_matrix(y_test, rf_y_pred)
    cm_display_rf = ConfusionMatrixDisplay(confusion_matrix=cm_rf, display_labels=["No Disease", "Heart Disease"])
    cm_display_rf.plot(cmap='Blues')
    st.pyplot(cm_display_rf.figure_)

elif model_choice == "Logistic Regression":
    # Display the Logistic Regression model evaluation
    st.write("**Logistic Regression Model Evaluation**")
    st.write(f"Accuracy: {lr_accuracy * 100:.2f}%")

    # Display the confusion matrix
    cm_lr = confusion_matrix(y_test, lr_y_pred)
    cm_display_lr = ConfusionMatrixDisplay(confusion_matrix=cm_lr, display_labels=["No Disease", "Heart Disease"])
    cm_display_lr.plot(cmap='Blues')
    st.pyplot(cm_display_lr.figure_)
