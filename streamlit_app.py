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

# Add title and subtitle with improved styling using the dark attractive color
st.markdown(
    """
    <style>
    .title {
        color: #8B0000;  /* Dark Red color for the title text */
        font-size: 50px;
        font-weight: bold;
        text-align: center;  /* Center text */
        text-shadow: 3px 3px 5px rgba(0, 0, 0, 0.7);  /* Strong shadow for readability */
        margin-top: 50px;
    }
    .subtitle {
        color: #8B0000;  /* Dark Red for the subtitle */
        font-size: 24px;
        text-align: center;  /* Center text */
        margin-top: 10px;
        text-shadow: none;  /* No shadow for subtitle */
    }
    .content {
        color: #8B0000;  /* Dark Red for content text */
        font-size: 18px;
        text-align: center;  /* Center text */
        margin: 50px auto;
        padding: 20px;
        max-width: 800px;
        border-radius: 10px;
        text-shadow: none;  /* No shadow for content */
    }
    .button-container {
        display: flex;
        justify-content: center;
        margin-top: 30px;
    }
    .stButton > button {
        background-color: #8B0000;  /* Dark Red color for button background */
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
        background-color: #660000;  /* Darker shade of Dark Red for button hover */
    }
    ul {
        text-align: left;  /* Keep bullet points left-aligned */
        max-width: 800px;
        margin: 0 auto;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Add title and subtitle with shadowing for readability
st.markdown('<p class="title">Heart Disease Prediction App</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Predict Heart Disease Risk with Machine Learning</p>', unsafe_allow_html=True)

# Content section with a left-aligned, well-spaced layout (without black transparent background)
st.markdown(
    """
    <div class="content">
    This app uses a machine learning model to predict the risk of heart disease based on various health parameters. 
    It provides valuable insights to help individuals understand their heart health status and take preventive measures.

    #### Key Features:
    <ul>
        <li>User-friendly interface</li>
        <li>Accurate predictions based on real-time data</li>
        <li>Quick results to help assess heart disease risk</li>
    </ul>
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
