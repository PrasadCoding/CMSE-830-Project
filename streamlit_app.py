import streamlit as st
from PIL import Image

# Set page config
st.set_page_config(page_title="Heart Disease Prediction App")

# Check session state for page navigation
if 'page' not in st.session_state:
    st.session_state.page = 'home'  # Default to home page

# Navigation logic using session state
def go_to_visualization():
    st.session_state.page = 'visualization'

# Home Screen layout
if st.session_state.page == 'home':
    # Load image for the home screen (replace with your own image)
    image = Image.open('heart_disease_image.jpg')
    
    # Title and description
    st.markdown("<h1 style='text-align: center; color: #FF4B4B;'>Heart Disease Prediction</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: #4B4B4B;'>Using Data to Predict and Prevent Heart Disease</h3>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #333333;'>Explore risk factors, visualize trends, and predict heart disease risk using advanced machine learning and interactive tools.</p>", unsafe_allow_html=True)
    
    # Display image on the home screen
    st.image(image, use_column_width=True)
    
    # Button to navigate to visualization page
    st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
    if st.button("Go to Visualizations"):
        go_to_visualization()
    st.markdown("</div>", unsafe_allow_html=True)

# Visualization Page
if st.session_state.page == 'visualization':
    st.markdown("<h1 style='text-align: center;'>Data Visualization</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Here you can explore the data through various visualizations.</p>", unsafe_allow_html=True)
    
    # Example plot (replace with your actual visualizations)
    import matplotlib.pyplot as plt
    import numpy as np

    fig, ax = plt.subplots()
    ax.plot(np.random.randn(100), color='blue')
    st.pyplot(fig)

    # Button to return to Home
    if st.button("Back to Home"):
        st.session_state.page = 'home'
