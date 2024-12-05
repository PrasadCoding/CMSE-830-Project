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

# Add title and subtitle with improved styling using a black color
st.markdown(
    """
    <style>
    .title {
        color: #000000;  /* Black color for the title text */
        font-size: 70px;  /* Increased font size */
        font-weight: bold;
        text-align: center;  /* Center text */
        text-shadow: 3px 3px 5px rgba(0, 0, 0, 0.7);  /* Shadow for readability */
        margin-top: 50px;
    }
    .subtitle {
        color: #000000;  /* Black for the subtitle */
        font-size: 40px;  /* Increased font size */
        text-align: center;  /* Center text */
        margin-top: 10px;
        text-shadow: none;  /* No shadow for subtitle */
    }
    .content {
        color: #000000;  /* Black for content text */
        font-size: 24px;  /* Increased font size */
        text-align: center;  /* Center text */
        margin: 50px auto;
        padding: 20px;
        max-width: 800px;
        border-radius: 10px;
        text-shadow: none;  /* No shadow for content */
    }
    .key-features {
        text-align: left;  /* Align "Key Features" to left */
        font-size: 28px;  /* Increased font size */
        font-weight: bold;
        margin-top: 40px;
        color: #000000;
        max-width: 800px;
        margin-left: auto;
        margin-right: auto;
    }
    ul {
        text-align: left;  /* Align the bullet points to the left */
        max-width: 800px;
        margin: 0 auto;
        font-size: 28px;  /* Increased font size */
        color: #000000;  /* Bullet points in black */
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

    <p class="key-features">Key Features:</p>
    <ul>
        <li>User-friendly interface</li>
        <li>Accurate predictions based on real-time data</li>
        <li>Quick results to help assess heart disease risk</li>
    </ul>
    </div>
    """,
    unsafe_allow_html=True,
)
