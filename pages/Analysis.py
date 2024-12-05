import streamlit as st

# Set the page layout to wide
st.set_page_config(page_title="Heart Disease Prediction - Analysis", page_icon="❤️", layout="wide")

# Set the background image for the page
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

# Add title and subtitle with improved styling
st.markdown(
    """
    <style>
    .title {
        color: #000000;
        font-size: 70px;
        font-weight: bold;
        text-align: center;
        margin-top: 50px;
    }
    .subtitle {
        color: #000000;
        font-size: 40px;
        text-align: center;
        margin-top: 10px;
        text-shadow: none;
    }
    .content {
        color: #000000;
        font-size: 24px;
        text-align: justify;
        margin: 50px auto;
        padding: 20px;
        max-width: 800px;
        border-radius: 10px;
        text-shadow: none;
    }
    .key-features {
        text-align: left;
        font-size: 28px;
        font-weight: bold;
        margin-top: 40px;
        color: #000000;
        max-width: 800px;
        margin-left: auto;
        margin-right: auto;
    }
    ul {
        text-align: left;
        max-width: 800px;
        margin: 0 auto;
        font-size: 20px;
        color: #000000;
    }

    </style>
    """,
    unsafe_allow_html=True,
)

# Add title and subtitle with shadowing for readability
st.markdown('<p class="title">Data Overview</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Understanding the Datasets Used for Heart Disease Prediction</p>', unsafe_allow_html=True)

# Content section with a left-aligned, well-spaced layout
st.markdown(
    """
    <div class="content">
    In this analysis, two datasets have been used to predict heart disease risk. These datasets provide information on patient demographics, health parameters, and their heart disease status. The two datasets have been merged on the **'id'** column, which serves as the primary key.

    The first dataset contains the following columns:
    - id
    - full_name
    - country
    - state
    - first_name
    - last_name
    - hospital
    - treatment
    - treatment_date

    The second dataset includes the following columns:
    - id
    - full_name
    - male
    - age
    - education
    - currentSmoker
    - cigsPerDay
    - BPMeds
    - prevalentStroke
    - prevalentHyp
    - diabetes
    - totChol
    - sysBP
    - diaBP
    - BMI
    - heartRate
    - glucose
    - TenYearCHD

    These datasets were joined based on the 'id' column, and the resulting dataframe was used for further analysis and machine learning model training.
    </div>
    """,
    unsafe_allow_html=True,
)
