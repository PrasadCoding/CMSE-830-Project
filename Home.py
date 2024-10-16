import streamlit as st
from PIL import Image

# Set page config
st.set_page_config(page_title="Heart Disease Prediction App")

# Load image for the home screen (replace with your own image)
image = Image.open('images/heart_disease_image.jpg')

# Custom CSS for styling (optional)
st.markdown("""
    <style>
    .main-title {
        font-size: 50px;
        color: #FF4B4B;
        text-align: center;
        font-weight: bold;
    }
    .sub-title {
        font-size: 20px;
        color: #4B4B4B;
        text-align: center;
    }
    .description {
        font-size: 18px;
        color: #333333;
        text-align: center;
        margin-bottom: 30px;
    }
    .button-container {
        display: flex;
        justify-content: center;
        gap: 20px;
    }
    .stButton button {
        width: 200px;
        height: 50px;
        font-size: 18px;
        color: white;
        background-color: #FF4B4B;
        border: none;
    }
    </style>
    """, unsafe_allow_html=True)

# Title and description
st.markdown("<h1 class='main-title'>Heart Disease Prediction</h1>", unsafe_allow_html=True)
st.markdown("<h3 class='sub-title'>Using Data to Predict and Prevent Heart Disease</h3>", unsafe_allow_html=True)
st.markdown("<p class='description'>Explore risk factors, visualize trends, and predict heart disease risk using advanced machine learning and interactive tools.</p>", unsafe_allow_html=True)

# Display image on the home screen
st.image(image, use_column_width=True)

# Add buttons for navigation (optional)
st.markdown("<div class='button-container'>", unsafe_allow_html=True)
col1, col2, col3 = st.columns([1,1,1])

with col1:
    if st.button('Explore Data'):
        pass  # Place your logic for navigating to EDA page here
with col2:
    if st.button('Risk Prediction'):
        pass  # Place your logic for navigating to prediction model page here
with col3:
    if st.button('Simulate Risks'):
        pass  # Place your logic for navigating to simulation page here
st.markdown("</div>", unsafe_allow_html=True)

# Footer (optional)
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>Created by Prasad Upasani | Michigan State University | Data Science Project</p>", unsafe_allow_html=True)
