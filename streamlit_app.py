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
        background-color: #f9f9f9;
    }
    .main-title {
        font-size: 50px;
        color: #FF4B4B;
        text-align: center;
        font-weight: bold;
        margin-top: 30px;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.1);
    }
    .sub-title {
        font-size: 24px;
        color: #4B4B4B;
        text-align: center;
        margin-bottom: 10px;
    }
    .description {
        font-size: 18px;
        color: #333333;
        text-align: center;
        margin: 20px auto;
        max-width: 700px;
        line-height: 1.6;
    }
    .footer {
        text-align: center;
        color: gray;
        font-size: 14px;
        margin-top: 40px;
        margin-bottom: 20px;
    }
    .image-container {
        display: flex;
        justify-content: center;
        margin: 30px 0;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        border-radius: 10px;
        overflow: hidden;
    }
    img {
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# Title and description
st.markdown("<h1 class='main-title'>Heart Disease Prediction</h1>", unsafe_allow_html=True)
st.markdown("<h3 class='sub-title'>Using Data to Predict and Prevent Heart Disease</h3>", unsafe_allow_html=True)
st.markdown("<p class='description'>Explore risk factors, visualize trends, and predict heart disease risk using advanced machine learning and interactive tools.</p>", unsafe_allow_html=True)

# Display image on the home screen
st.markdown("<div class='image-container'>", unsafe_allow_html=True)
st.image(image, use_column_width='auto')
st.markdown("</div>", unsafe_allow_html=True)

# Additional content section
st.markdown("<div class='stats'>", unsafe_allow_html=True)
st.markdown("<h4>Did You Know?</h4>", unsafe_allow_html=True)
st.markdown("<p>Heart disease is the leading cause of death worldwide, claiming around 17.9 million lives each year.</p>", unsafe_allow_html=True)
st.markdown("<p>Key risk factors include high blood pressure, high cholesterol, smoking, diabetes, and obesity.</p>", unsafe_allow_html=True)
st.markdown("<p>Early detection and lifestyle changes can significantly reduce the risk of heart disease.</p>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p class='footer'>Created by Prasad Upasani | Michigan State University | Data Science Project</p>", unsafe_allow_html=True)
