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
image_url = 'https://raw.githubusercontent.com/PrasadCoding/CMSE-830-Project/refs/heads/master/images/bg4_o.png'  # Replace with your raw URL
set_bg_image(image_url)

# Add title and subtitle with improved styling using the exact color palette
st.markdown(
    """
    <style>
    .title {
        color: #C9CED1;  /* Silver color for the title text */
        font-size: 50px;
        font-weight: bold;
        text-align: center;
        text-shadow: 3px 3px 5px rgba(0, 0, 0, 0.7);  /* Strong shadow for readability */
        margin-top: 50px;
    }
    .subtitle {
        color: #E3CBC3;  /* Pale Dogwood for the subtitle */
        font-size: 24px;
        text-align: center;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);  /* Light shadow for contrast */
        margin-top: 10px;
    }
    .content {
        color: #E3CBC3;  /* Pale Dogwood for content text */
        font-size: 18px;
        text-align: center;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);  /* Slight shadow for readability */
        max-width: 800px;
        margin: 50px auto;
        padding: 20px;
        background-color: rgba(0, 0, 0, 0.5);  /* Semi-transparent dark background for text readability */
        border-radius: 10px;
    }
    .button-container {
        display: flex;
        justify-content: center;
        margin-top: 30px;
    }
    .stButton > button {
        background-color: #E3CBC3;  /* Pale Dogwood for button background */
        color: #ffffff;
        font-size: 18px;
        font-weight: bold;
        border-radius: 12px;
        height: 50px;
        width: 300px;
        border: none;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        transition: background-color 0.3s ease;
    }
    .stButton > button:hover {
        background-color: #DBB5AA;  /* Pale Dogwood 2 for button hover */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Add title and subtitle with shadowing for readability
st.markdown('<p class="title">Heart Disease Prediction App</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Predict Heart Disease Risk with Machine Learning</p>', unsafe_allow_html=True)

# Content section with a centered, well-spaced layout
st.markdown(
    """
    <div class="content">
    This app uses a machine learning model to predict the risk of heart disease based on various health parameters. 
    It provides valuable insights to help individuals understand their heart health status and take preventive measures.

    #### Key Features:
    - User-friendly interface
    - Accurate predictions based on real-time data
    - Quick results to help assess heart disease risk
    </div>
    """,
    unsafe_allow_html=True,
)

# Button to start prediction with hover effects
st.markdown('<div class="button-container">', unsafe_allow_html=True)
if st.button("Start Prediction"):
    st.markdown("#### Let's Predict Your Heart Disease Risk!")
    # Add your prediction form or further logic here
    # You can link this to other parts of your app
st.markdown('</div>', unsafe_allow_html=True)
