import streamlit as st

# Set the page layout to wide
st.set_page_config(page_title="Heart Disease Prediction", page_icon="❤️", layout="wide")

# Function to set background image using raw URL
def set_bg_image(image_url):
    """
    Set background image for the Streamlit app using a raw GitHub URL
    """
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("{image_url}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            height: 100vh;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )

# Path to your image file on GitHub (use the raw URL)
image_url = 'https://raw.githubusercontent.com/PrasadCoding/CMSE-830-Project/refs/heads/master/images/bg43.png'  # Replace with your raw URL
set_bg_image(image_url)

# Add title and subtitle with controlled styling
st.markdown(
    """
    <style>
    .custom-title {
        font-size: 70px;  /* Explicit font size */
        font-weight: bold;
        color: #000000;  /* Black color for better visibility */
        text-align: center;  /* Center the title */
        margin-top: 50px;
        margin-bottom: 10px;
    }
    .custom-subtitle {
        font-size: 40px;
        color: #000000;
        text-align: center;
        margin-bottom: 30px;
    }
    /* Content styling */
    .custom-content {
        font-size: 20px;  /* Limit font size to avoid sidebar issues */
        color: #000000;
        text-align: justify;
        margin: 20px auto;
        max-width: 800px;
        padding: 20px;
    }
    /* Styling for key features section */
    .custom-key-features {
        font-size: 28px; 
        font-weight: bold;
        color: #000000;
        margin-top: 40px;
    }
    ul.custom-list {{
        text-align: left;
        font-size: 20px;
        color: #000000;
        margin: 10px auto;
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

# Add title and subtitle with the updated styling
st.markdown('<div class="custom-title">Heart Disease Prediction App</div>', unsafe_allow_html=True)
st.markdown('<div class="custom-subtitle">Predict Heart Disease Risk with Machine Learning</div>', unsafe_allow_html=True)

# Add an image between subtitle and content with centered alignment
image_url_between = 'https://raw.githubusercontent.com/PrasadCoding/CMSE-830-Project/refs/heads/master/images/heart_disease_image.jpg'  # Replace with your image URL

# Centering the image using HTML and CSS
st.markdown(
    f"""
    <div style="text-align: center;">
        <img src="{image_url_between}" width="600px" />
    </div>
    """,
    unsafe_allow_html=True,
)

# Content section with well-spaced layout
st.markdown(
    """
    <div class="custom-content">
    This app uses a machine learning model to predict the risk of heart disease based on various health parameters. 
    It provides valuable insights to help individuals understand their heart health status and take preventive measures.

    <p class="custom-key-features">Key Features:</p>
    <ul class="custom-list">
        <li>User-friendly interface</li>
        <li>Accurate predictions based on real-time data</li>
        <li>Quick results to help assess heart disease risk</li>
    </ul>
    </div>
    """,
    unsafe_allow_html=True,
)
