# EDA Overview Page: Interactive Correlation Heatmap

import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.figure_factory as ff
import hiplot as hip
import streamlit.components.v1 as components
# Assuming you already have your dataset
df = pd.read_csv('dataset/heart_disease.csv')

# Select numeric features for correlation heatmap
numeric_features = df.select_dtypes(include=['float64', 'int64'])

# Calculate the correlation matrix
correlation_matrix = numeric_features.corr()

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

# Title and description
st.markdown("<h1 style='color: #FF4B4B;'>EDA Overview</h1>", unsafe_allow_html=True)
st.write(
    "Welcome to the Exploratory Data Analysis (EDA) Overview! "
    "In this section, we will visualize the relationships between variables using an interactive correlation heatmap."
)
# Subtitle for heatmap
st.subheader("Interactive Correlation Heatmap")

# Selectbox for color scheme
col1, col2 = st.columns(2)

with col1:
    heatmap_type = st.selectbox("Choose Heatmap Type", ["Seaborn", "Plotly"])

with col2:
    color_palette = st.selectbox("Choose Color Palette", ["RdBu", "viridis", "plasma", "cividis", "inferno", "magma", "Plasma", "YlGnBu"])

# Option 1: Using Seaborn for Static Heatmap
def plot_seaborn_heatmap():
    fig, ax = plt.subplots(figsize=(15, 8))
    try:
        sns.heatmap(correlation_matrix, annot=True, cmap=color_palette, center=0, ax=ax)
        st.pyplot(fig)
    except KeyError:
        st.write(f"The selected color palette '{color_palette}' is **not supported** by Seaborn. Please choose a different palette.")

# Option 2: Using Plotly for Interactive Heatmap
def plot_plotly_heatmap():
    fig = go.Figure(data=go.Heatmap(
        z=correlation_matrix.values,
        x=correlation_matrix.columns,
        y=correlation_matrix.columns,
        colorscale=color_palette,  # Use selected color palette
        zmin=-1, zmax=1))

    fig.update_layout(title="Interactive Correlation Heatmap", 
                      xaxis_nticks=36, 
                      width=800, height=600)
    st.plotly_chart(fig)

# Render the selected heatmap
if heatmap_type == "Seaborn":
    plot_seaborn_heatmap()
else:
    plot_plotly_heatmap()


# Customizable Histogram

st.header("Customizable Histograms")

# Create columns for feature selection, color input, and bins slider
hist_col1, hist_col2 = st.columns(2)

with hist_col1:
    selected_feature = st.selectbox("Select Feature for Histogram", numeric_features.columns)

with hist_col2:
    color_input = st.text_input("Enter Color (Hex Code or Name)", placeholder="#1f77b4")  # Default color as a placeholder

# Slider for number of bins
num_bins = st.slider("Select Number of Bins", min_value=5, max_value=50, value=20)

# Plot histogram
def plot_histogram():
    default_color = "#1f77b4"  # Default color
    color = color_input if color_input else default_color  # Use input color or default
    fig = go.Figure(data=go.Histogram(x=df[selected_feature], marker_color=color, nbinsx=num_bins))
    fig.update_layout(title=f"Histogram of {selected_feature}", xaxis_title=selected_feature, yaxis_title="Count")
    st.plotly_chart(fig)

# Render the histogram
plot_histogram()


# Customizable Box Plot

st.header("Customizable Box Plots")

# Create columns for feature selection and color input
box_col1, box_col2 = st.columns(2)

with box_col1:
    selected_box_feature = st.selectbox("Select Feature for Box Plot", numeric_features.columns)

with box_col2:
    color_input_box = st.text_input("Enter Box Color (Hex Code or Name)", placeholder="#1f77b4")  # Default color as a placeholder

# Plot box plot
def plot_box_plot():
    default_color = "#1f77b4"  # Default color
    color = color_input_box if color_input_box else default_color  # Use input color or default
    
    # Create the horizontal box plot using Plotly
    fig = go.Figure(data=go.Box(x=df[selected_box_feature], boxmean=True, marker_color=color))
    fig.update_layout(title=f"Horizontal Box Plot of {selected_box_feature}", xaxis_title=selected_box_feature)
    
    st.plotly_chart(fig)

# Render the box plot
plot_box_plot()


# Interactive Scatter Plot

st.header("Interactive Scatter Plot")

# Create columns for select boxes and color input
col1, col2 = st.columns(2)

# Select X and Y variables
x_variable = col1.selectbox("Choose X Variable", numeric_features.columns)
y_variable = col2.selectbox("Choose Y Variable", numeric_features.columns)

# Create another row of columns for custom color and categorical variable
col3, col4 = st.columns(2)

# Options for the selectbox
color_options = ["None", "male", "currentSmoker", "BPMeds", "prevalentStroke", "prevalentHyp", "diabetes", "TenYearCHD"]
# In the first column, create the selectbox for choosing the categorical variable
with col3:
    categorical_variable = st.selectbox('Choose a categorical variable for color', color_options)

# In the second column, create the input box for a custom color
with col4:
    custom_color = st.text_input('Enter color (hex code)', value='#1f77b4')

if custom_color == '':
    custom_color = '#1f77b4'  # Default color

# If the user chooses "None", use the custom color for the scatter plot
if categorical_variable == "None":
    fig = px.scatter(df, x=x_variable, y=y_variable, color_discrete_sequence=[custom_color])  # Use custom color
else:
    # Convert the selected column to categorical if it's not already
    if df[categorical_variable].dtype != 'object' and df[categorical_variable].dtype.name != 'category':
        df[categorical_variable] = df[categorical_variable].astype('category')
    
    # Plot the scatter plot with color based on the selected categorical variable
    fig = px.scatter(df, x=x_variable, y=y_variable, color=categorical_variable,
                     color_discrete_sequence=px.colors.qualitative.Set1)

# Display the scatter plot
st.plotly_chart(fig)

st.header("Interactive Parallel Plot")

selected_columns = st.multiselect(
    "Select features for Parallel Plot", 
    df.columns.tolist(), 
    default=["age", "BMI", "sysBP", "diaBP", "heartRate", "glucose", "TenYearCHD"]
)

# Check if the user has selected at least two columns
if len(selected_columns) > 1:
    # Create the parallel plot using hiplot
    exp = hip.Experiment.from_dataframe(df[selected_columns])

    # Render the parallel plot using streamlit's component function
    with st.spinner("Loading Parallel Plot..."):
        # Convert the hiplot experiment to HTML
        hiplot_html = exp.to_html()

        # Use Streamlit to embed the HTML
        components.html(hiplot_html, height=800)
else:
    st.warning("Please select at least two columns for the parallel plot.")






