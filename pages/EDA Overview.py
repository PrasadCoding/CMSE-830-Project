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
color_palette = st.selectbox(
    "Choose a color scheme for the heatmap:",
    options=["RdBu", "Viridis", "Cividis", "Inferno", "Magma", "Plasma", "YlGnBu"]
)

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

# Create a selectbox to switch between heatmap types
heatmap_type = st.selectbox("Choose Heatmap Type", ["Seaborn", "Plotly"])

# Render the selected heatmap
if heatmap_type == "Seaborn":
    plot_seaborn_heatmap()
else:
    plot_plotly_heatmap()


# Customizable Histograms

st.subheader("Customizable Histograms")

# Select a numeric variable for histogram
hist_variable = st.selectbox("Choose a variable for the histogram:", options=numeric_features.columns)

# Select number of bins
num_bins = st.slider("Select the number of bins:", min_value=5, max_value=100, value=20)

# Function to plot the histogram
def plot_histogram(variable, bins):
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.hist(df[variable], bins=bins, color='skyblue', edgecolor='black')
    ax.set_title(f'Histogram of {variable}')
    ax.set_xlabel(variable)
    ax.set_ylabel('Frequency')
    st.pyplot(fig)

# Render the histogram
plot_histogram(hist_variable, num_bins)

# Customizable Box Plots

st.subheader("Customizable Box Plots")

# Select a numeric variable for box plot
box_variable = st.selectbox("Choose a numeric variable for the box plot:", options=numeric_features.columns)

# If there are categorical variables, select one for grouping (adjust based on your DataFrame)
categorical_features = df.select_dtypes(include=['object', 'category']).columns.tolist()
if categorical_features:
    box_group_variable = st.selectbox("Choose a categorical variable for grouping:", options=categorical_features)
else:
    box_group_variable = None

# Function to plot the box plot
def plot_box_plot(numeric_var, group_var=None):
    fig, ax = plt.subplots(figsize=(10, 6))
    
    if group_var:
        sns.boxplot(data=df, x=group_var, y=numeric_var, ax=ax)
        ax.set_title(f'Box Plot of {numeric_var} by {group_var}')
    else:
        sns.boxplot(data=df, y=numeric_var, ax=ax)
        ax.set_title(f'Box Plot of {numeric_var}')

    ax.set_ylabel(numeric_var)
    st.pyplot(fig)

# Render the box plot
if box_group_variable:
    plot_box_plot(box_variable, box_group_variable)
else:
    plot_box_plot(box_variable)

