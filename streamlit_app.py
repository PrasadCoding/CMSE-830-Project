import streamlit as st
import base64
from pathlib import Path

# Set the page layout to wide
st.set_page_config(page_title="Heart Disease Prediction", page_icon="❤️", layout="wide")

# Function to load an image for background
def set_bg_image(image_path):
    """
    Set background image for the Streamlit app
    """
    # Load the image as binary
    try:
        with open(image_path, "rb") as image_file:
            img_bytes = image_file.read()
        # Encode the image to base64
        encoded_image = base64.b64encode(img_bytes).decode()

        # Use the base64 encoded image for the background
        st.markdown(
            f"""
            <style>
            .stApp {{
                background-image: url('data:image/png;base64,{encoded_image}');
                background-size: cover;
                background-position: center;
                background-repeat: no-repeat;
                height: 100vh;
            }}
            </style>
            """,
            unsafe_allow_html=True,
        )
    except FileNotFoundError:
        st.error("The image file was not found. Please check the path.")

# Path to your image file
image_path = Path('images/bg_4.png')  # Make sure the file is in the correct folder
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

