import streamlit as st

# Set the page layout to wide
st.set_page_config(page_title="Heart Disease Prediction", page_icon="❤️", layout="centered")

# Manually set the background color and title color
bg_color = "#f4442e"  # Set your desired background color here
title_color = "#d90429"  # Set your desired title color here

# Apply the background color to the app
st.markdown(f"<style>.stApp {{ background-color: {bg_color}; }}</style>", unsafe_allow_html=True)

# Add title and subtitle with the chosen color
st.markdown(f"<h1 style='color:{title_color}; text-align: center;'>Heart Disease Prediction App</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Predict Heart Disease Risk with Machine Learning</h3>", unsafe_allow_html=True)

# Add an image (optional)
image_url_between = 'https://raw.githubusercontent.com/PrasadCoding/CMSE-830-Project/refs/heads/master/images/heart_disease_image.jpg'  # Replace with your image URL
st.image(image_url_between, use_container_width=True)

# Content section
st.markdown(
    """
    This app uses a machine learning model to predict the risk of heart disease based on various health parameters. 
    It provides valuable insights to help individuals understand their heart health status and take preventive measures.

    **Key Features:**
    - User-friendly interface
    - Accurate predictions based on real-time data
    - Quick results to help assess heart disease risk
    """
)
