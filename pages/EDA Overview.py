# EDA Overview Page: Interactive Correlation Heatmap

import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt
import plotly.graph_objects as go

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


# Customizable Box Plots

# Customizable Interactive Box Plots

st.subheader("Customizable Interactive Box Plots")

# Select a numeric variable for the box plot
box_variable = st.selectbox("Choose a numeric variable for the box plot:", options=numeric_features.columns)

# If there are categorical variables, select one for grouping (adjust based on your DataFrame)
categorical_features = df.select_dtypes(include=['object', 'category']).columns.tolist()
if categorical_features:
    box_group_variable = st.selectbox("Choose a categorical variable for grouping:", options=categorical_features)
else:
    box_group_variable = None

# Function to plot the interactive box plot
def plot_interactive_box_plot(numeric_var, group_var=None):
    if group_var:
        fig = px.box(df, x=numeric_var, y=group_var, points="all", title=f'Interactive Box Plot of {numeric_var} by {group_var}')
    else:
        fig = px.box(df, x=numeric_var, points="all", title=f'Interactive Box Plot of {numeric_var}')

    fig.update_layout(
        xaxis_title=numeric_var,
        yaxis_title=group_var if group_var else 'Distribution',
        width=800, height=600
    )
    
    st.plotly_chart(fig)

# Render the interactive box plot
plot_interactive_box_plot(box_variable, box_group_variable)

# Interactive Scatter Plot
st.subheader("Interactive Scatter Plot")

# Create two columns for X and Y variable select boxes
col1, col2 = st.columns(2)

# Select X and Y variables
with col1:
    x_variable = st.selectbox("Choose a variable for the X-axis:", options=numeric_features.columns)

with col2:
    y_variable = st.selectbox("Choose a variable for the Y-axis:", options=numeric_features.columns)

# Allow the user to input a hex color code or leave it blank
color_input = st.text_input("Enter a hex color code (e.g., #FF5733) or leave blank for default color:")

# Define a default color
default_color = 'blue'

# Function to plot the interactive scatter plot
def plot_interactive_scatter_plot(x_var, y_var, point_color):
    fig = px.scatter(df, x=x_var, y=y_var,
                     title=f'Interactive Scatter Plot of {y_var} vs {x_var}',
                     color_discrete_sequence=[point_color])

    fig.update_layout(
        xaxis_title=x_var,
        yaxis_title=y_var,
        width=800, height=600
    )

    st.plotly_chart(fig)

# Determine the color to use: user input or default
color_to_use = color_input if color_input else default_color

# Render the interactive scatter plot
plot_interactive_scatter_plot(x_variable, y_variable, color_to_use)







