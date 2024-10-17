# EDA Overview Page: Interactive Correlation Heatmap

import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.figure_factory as ff
# Assuming you already have your dataset
df = pd.read_csv('dataset/heart_disease.csv')

# Select numeric features for correlation heatmap
numeric_features = df.select_dtypes(include=['float64', 'int64'])

# Calculate the correlation matrix
correlation_matrix = numeric_features.corr()

# Title and description
st.markdown("<h1 style='color: #FF4B4B;'>EDA Overview</h1>", unsafe_allow_html=True)
st.write(
    "Welcome to the Exploratory Data Analysis (EDA) Overview! "
    "In this section, we will visualize the relationships between variables using an interactive correlation heatmap."
)

# Detect missing values in the dataset
missing_values = df.isnull()

# Select color palette for the heatmap
st.write("### Interactive Missing Values Heatmap")

# Create an input box to choose a color palette
palette_choice = st.selectbox(
    "Choose a color palette",
    ["RdBu", "viridis", "plasma", "cividis", "inferno", "magma", "Plasma", "YlGnBu"]
)

# Option to use seaborn heatmap or interactive plotly heatmap
heatmap_type = st.selectbox("Choose Heatmap Type", ["Seaborn", "Plotly"])

# Function to plot seaborn heatmap
def plot_seaborn_missing_values_heatmap():
    fig, ax = plt.subplots(figsize=(12, 8))
    sns.heatmap(missing_values, cmap=palette_choice, cbar=False, ax=ax)
    ax.set_title("Missing Values Heatmap")
    st.pyplot(fig)

# Function to plot interactive heatmap using plotly
def plot_interactive_missing_values_heatmap():
    z = missing_values.astype(int).values
    fig = ff.create_annotated_heatmap(z, colorscale=palette_choice)
    fig.update_layout(title="Interactive Missing Values Heatmap", width=900, height=600)
    st.plotly_chart(fig)

# Render the selected heatmap
if heatmap_type == "Seaborn":
    plot_seaborn_missing_values_heatmap()
else:
    plot_interactive_missing_values_heatmap()


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
    fig, ax = plt.subplots(figsize=(10, 8))
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









