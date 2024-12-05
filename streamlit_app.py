import streamlit as st
from PIL import Image
import base64

# Set page config
st.set_page_config(page_title="Heart Disease Prediction App", page_icon="❤️")

# Raw URL of the background image hosted on GitHub
bg_image_url = "https://raw.githubusercontent.com/PrasadCoding/CMSE-830-Project/master/images/bg3.png"

# Custom CSS for styling (full-screen background and text overlay)
st.markdown(f"""
    <style>
    .stApp {{
        background-image: url('{bg_image_url}');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        min-height: 100vh;
        position: relative;
    }}
    
    .overlay {{
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        color: white;
        text-align: center;
        font-family: 'Arial', sans-serif;
    }}
    
    .main-title {{
        font-size: 50px;
        font-weight: bold;
        text-shadow: 3px 3px 6px rgba(0, 0, 0, 0.5);
    }}
    
    .sub-title {{
        font-size: 24px;
        margin-top: 10px;
        font-weight: normal;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
    }}
    
    .description {{
        font-size: 18px;
        margin-top: 15px;
        font-weight: normal;
        max-width: 600px;
        line-height: 1.6;
        margin-left: auto;
        margin-right: auto;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
    }}
    
    </style>
""", unsafe_allow_html=True)

# Overlay text on the background image
st.markdown(f"""
    <div class="overlay">
        <h1 class="main-title">Heart Disease Prediction</h1>
        <h3 class="sub-title">Using Data to Predict and Prevent Heart Disease</h3>
        <p class="description">Explore risk factors, visualize trends, and predict heart disease risk using advanced machine learning and interactive tools.</p>
    </div>
""", unsafe_allow_html=True)

# Footer
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p class='footer' style='text-align:center; color: gray;'>Created by Prasad Upasani | Michigan State University | Data Science Project</p>", unsafe_allow_html=True)
