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
st.title("EDA Overview")
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
    sns.heatmap(correlation_matrix, annot=True, cmap=color_palette, center=0, ax=ax)
    st.pyplot(fig)

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
