import streamlit as st

# Set the page layout to wide
st.set_page_config(page_title="Heart Disease Prediction", page_icon="❤️", layout="centered")

# Manually set the background color and title color
bg_color = "#edf2f4"  # Set your desired background color here
title_color = "#ef233c"  # Set your desired title color here

# Apply the background color to the app
st.markdown(f"<style>.stApp {{ background-color: {bg_color}; display: flex; justify-content: center; align-items: center; height: 100vh; text-align: center; }}</style>", unsafe_allow_html=True)

# Add title with the chosen color
st.markdown(f"<h1 style='color:{title_color}; text-align: center;'>Heart Disease Prediction App</h1>", unsafe_allow_html=True)

# Display the GIF animation with size customization
gif_url = 'https://raw.githubusercontent.com/PrasadCoding/CMSE-830-Project/refs/heads/master/animation/Animation%20-%201743363269713.gif'  # Replace with your GIF URL

# Customize the width and height of the GIF
gif_width = 300  # Width of the GIF (in pixels)
gif_height = 300  # Height of the GIF (in pixels)

# Center the content in a container and add the GIF animation
st.markdown("""<div style="width: 80%; max-width: 1000px; margin: 0 auto;">""", unsafe_allow_html=True)

# Display the GIF image
st.markdown(
    f"""
    <div style="text-align: center;">
        <img src="{gif_url}" width="{gif_width}px" height="{gif_height}px" />
    </div>
    """,
    unsafe_allow_html=True,
)

# Content section with center alignment
st.markdown(
    """
    <h3 style='text-align: center;'>App Features</h3>
    <p style='text-align: center;'>Uses machine learning to assess heart disease risk based on health parameters.</p>
    <p style='text-align: center;'>Provides accurate, real-time predictions to understand heart health.</p>
    <p style='text-align: center;'>Offers a user-friendly interface and quick results for evaluating risk.</p>
    """, unsafe_allow_html=True
)
