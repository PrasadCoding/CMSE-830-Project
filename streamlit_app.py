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

# Add buttons for navigation
st.markdown("<div class='button-container'>", unsafe_allow_html=True)
col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    if st.button('Explore Data'):
        st.session_state.page = "Explore Data"  # Set the page state
        st.experimental_rerun()  # Refresh to navigate

with col2:
    if st.button('Risk Prediction'):
        st.session_state.page = "Risk Prediction"  # Set the page state
        st.experimental_rerun()  # Refresh to navigate

with col3:
    if st.button('Simulate Risks'):
        st.session_state.page = "Simulate Risks"  # Set the page state
        st.experimental_rerun()  # Refresh to navigate

st.markdown("</div>", unsafe_allow_html=True)

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Explore Data", "Risk Prediction", "Simulate Risks"])

# Manage page content based on selected state
if 'page' not in st.session_state:
    st.session_state.page = "Home"

if st.session_state.page == "Home":
    # Home page content is already rendered above
    ...

elif st.session_state.page == "Explore Data":
    # Render the EDA Overview page
    exec(open("pages/EDA Overview.py").read())

elif st.session_state.page == "Risk Prediction":
    # Logic for the Risk Prediction page
    st.write("Risk Prediction Page")
    # Include your prediction model code here

elif st.session_state.page == "Simulate Risks":
    # Logic for the Simulate Risks page
    st.write("Simulate Risks Page")
    # Include your simulation code here

# Footer (optional)
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>Created by Prasad Upasani | Michigan State University | Data Science Project</p>", unsafe_allow_html=True)
