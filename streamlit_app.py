import streamlit as st

# Set the page layout to wide
st.set_page_config(page_title="Heart Disease Prediction", page_icon="❤️", layout="centered")

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

# Path to your background image file on GitHub (use the raw URL)
image_url = 'https://raw.githubusercontent.com/PrasadCoding/CMSE-830-Project/refs/heads/master/images/bg43.png'  # Replace with your raw URL
set_bg_image(image_url)

title_color = "#ef233c"  # Set your desired title color here
text_color = "#2b2d42"


# Add title with the chosen color
st.markdown(f"<h1 style='color:{title_color}; text-align: center;'>Heart Disease Prediction App</h1>", unsafe_allow_html=True)

# Display the GIF animation with size customization
gif_url = 'https://raw.githubusercontent.com/PrasadCoding/CMSE-830-Project/refs/heads/master/animation/Animation%20-%201743363269713.gif'  # Replace with your GIF URL

# Customize the width and height of the GIF
gif_width = 300  # Width of the GIF (in pixels)
gif_height = 300  # Height of the GIF (in pixels)

# Center the content in a container and add the GIF animation
st.markdown("""<div style="width: 80%; max-width: 1000px; margin: 0 auto;">""", unsafe_allow_html=True)
st.write("")
# Display the GIF image
st.markdown(
    f"""
    <div style="text-align: center;">
        <img src="{gif_url}" width="{gif_width}px" height="{gif_height}px" />
    </div>
    """,
    unsafe_allow_html=True,
)
st.write("")
st.markdown(
    f"""
    <h3 style='text-align: center; color:{text_color};'>App Features</h3>
    <p style='text-align: justify; color:{text_color};'>Uses machine learning to assess heart disease risk based on health parameters.</p>
    <p style='text-align: center; color:{text_color};'>Provides accurate, real-time predictions to understand heart health.</p>
    <p style='text-align: center; color:{text_color};'>Offers a user-friendly interface and quick results for evaluating risk.</p>
    """, unsafe_allow_html=True
)


