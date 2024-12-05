import streamlit as st
from PIL import Image
import os

# Set the page layout to wide
st.set_page_config(page_title="Heart Disease Prediction", page_icon="❤️", layout="wide")

# Set background image using a relative path
def set_bg_image(image_path):
    """
    Set background image for the Streamlit app
    """
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("{image_path}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            height: 100vh;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )

# Path to the image in the 'images' folder
image_path = 'images/your-image-name.png'  # Replace with your actual image name
set_bg_image(image_path)

# Add title to the app
st.title("Heart Disease Prediction App")
st.markdown(
    """
    ### Predict Heart Disease Risk with Machine Learning

    This app uses a machine learning model to predict the risk of heart disease based on various health parameters. It provides valuable insights to help individuals understand their heart health status and take preventive measures.

    #### Key Features:
    - User-friendly interface
    - Accurate predictions based on real-time data
    - Quick results to help assess heart disease risk

    [Get Started Now →](#)
    """,
    unsafe_allow_html=True,
)

# Display an attractive, interactive button
st.markdown(
    """
    <style>
    .stButton > button {
        background-color: #ff4b4b;
        color: white;
        font-size: 18px;
        font-weight: bold;
        border-radius: 12px;
        height: 50px;
        width: 300px;
        border: none;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        transition: background-color 0.3s ease;
    }
    .stButton > button:hover {
        background-color: #ff1a1a;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

if st.button("Start Prediction"):
    st.markdown("#### Let's Predict Your Heart Disease Risk!")
    # Add your prediction form or further logic here
    # You can link this to other parts of your app
