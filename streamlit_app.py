import streamlit as st
from PIL import Image

# Set page config
st.set_page_config(page_title="Heart Disease Prediction App", layout="wide")

# Set up session state to handle page navigation
if 'page' not in st.session_state:
    st.session_state.page = 'home'  # default page

# Function to change pages
def navigate_to(page):
    st.session_state.page = page
    st.experimental_rerun()

# Home page layout
if st.session_state.page == 'home':
    # Load image for the home screen (replace with your own image)
    image = Image.open('heart_disease_image.jpg')  # Replace with your image path

    # Custom CSS for styling
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
            navigate_to('explore_data')  # Navigate to 'Explore Data' page
    with col2:
        if st.button('Risk Prediction'):
            navigate_to('risk_prediction')  # Navigate to 'Risk Prediction' page
    with col3:
        if st.button('Dummy Section'):
            navigate_to('dummy_section')  # Navigate to 'Dummy Section'
    st.markdown("</div>", unsafe_allow_html=True)

# Explore Data page layout
elif st.session_state.page == 'explore_data':
    st.title("Explore Data")
    st.write("This is where you'll show the EDA for the heart disease dataset.")
    # Add your EDA code here

    # Navigation back to home
    if st.button("Go back to Home"):
        navigate_to('home')

# Risk Prediction page layout
elif st.session_state.page == 'risk_prediction':
    st.title("Risk Prediction")
    st.write("This is where you'll show the risk prediction model.")
    # Add your prediction model code here

    # Navigation back to home
    if st.button("Go back to Home"):
        navigate_to('home')

# Dummy Section layout
elif st.session_state.page == 'dummy_section':
    st.title("Dummy Section")
    st.write("This is a dummy section that was navigated to from the home screen.")

    # You can add more widgets, information, or functionality here for this dummy section.

    # Navigation back to home
    if st.button("Go back to Home"):
        navigate_to('home')
