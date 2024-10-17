import streamlit as st
from PIL import Image

# Set page config
st.set_page_config(page_title="Heart Disease Prediction App")

# Load image for the home screen (replace with your own image)
image = Image.open('images/heart_disease_image.jpg')

# Custom CSS for styling (optional)
st.markdown("""
    <style>
    body {
        background-color: #f0f4f8; /* Light blue background */
        margin: 0; /* Remove default margin */
    }
    .main-title {
        font-size: 40px; /* Smaller title */
        color: #FF4B4B;
        text-align: center;
        font-weight: bold;
        margin: 5px 0; /* Reduced margin */
    }
    .sub-title {
        font-size: 20px; /* Smaller subtitle */
        color: #333333;
        text-align: center;
        margin: 5px 0; /* Reduced margin */
    }
    .description {
        font-size: 16px; /* Smaller description */
        color: #555555;
        text-align: center;
        margin: 5px auto; /* Reduced margin */
        max-width: 600px; /* Smaller max width */
        line-height: 1.4; /* Adjusted line height */
    }
    .footer {
        text-align: center;
        color: gray;
        font-size: 12px; /* Smaller footer */
        margin: 5px 0; /* Reduced margin */
    }
    .image-container {
        display: flex;
        justify-content: center;
        margin: 10px 0; /* Reduced margin */
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        border-radius: 10px;
        overflow: hidden;
    }
    img {
        border-radius: 10px;
    }
    .stats {
        background-color: #ffffff;
        padding: 15px; /* Smaller padding */
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        margin: 15px auto; /* Smaller margin */
        max-width: 600px; /* Smaller max width */
    }
    .stats h4 {
        color: #FF4B4B;
        margin-bottom: 5px; /* Reduced margin */
    }
    </style>
    """, unsafe_allow_html=True)

# Title and description
st.markdown("<h1 class='main-title'>Heart Disease Prediction</h1>", unsafe_allow_html=True)
st.markdown("<h3 class='sub-title'>Using Data to Predict and Prevent Heart Disease</h3>", unsafe_allow_html=True)
st.markdown("<p class='description'>Explore risk factors and visualize trends using advanced machine learning tools.</p>", unsafe_allow_html=True)

# Display image on the home screen
st.markdown("<div class='image-container'>", unsafe_allow_html=True)
st.image(image, use_column_width='auto')
st.markdown("</div>", unsafe_allow_html=True)

# Additional content section
st.markdown("<div class='stats'>", unsafe_allow_html=True)
st.markdown("<h4>Did You Know?</h4>", unsafe_allow_html=True)
st.markdown("<p>Heart disease is a leading cause of death, claiming millions of lives each year.</p>", unsafe_allow_html=True)
st.markdown("<p>Key risk factors include high blood pressure, smoking, and obesity.</p>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p class='footer'>Created by Prasad Upasani | Michigan State University | Data Science Project</p>", unsafe_allow_html=True)
