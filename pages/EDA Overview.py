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


# Risk Heatmap

st.header("Risk Heatmap")

# Create bins for age and BMI
age_bins = [20, 30, 40, 50, 60, 70, 80, 90]
bmi_bins = [15, 20, 25, 30, 35, 40]

# Categorize the data
df['age_group'] = pd.cut(df['age'], bins=age_bins)
df['bmi_group'] = pd.cut(df['BMI'], bins=bmi_bins)
# Use the currentSmoker column directly
df['smoking_group'] = df['currentSmoker'].replace({0: "Non-Smoker", 1: "Smoker"})

# Create a pivot table to calculate the average risk for each group
risk_heatmap_data = df.groupby(['age_group', 'bmi_group', 'smoking_group']).agg(
    average_risk=('TenYearCHD', 'mean')).reset_index()

# Pivot the data for heatmap
risk_matrix = risk_heatmap_data.pivot_table(
    index=['age_group', 'bmi_group'], 
    columns='smoking_group', 
    values='average_risk', 
    fill_value=0)

# Create the heatmap
fig = go.Figure(data=go.Heatmap(
    z=risk_matrix.values,
    x=risk_matrix.columns,
    y=risk_matrix.index,
    colorscale='Viridis',  # Change color scale as needed
    colorbar=dict(title='Average Risk'),
))

fig.update_layout(
    title='Risk Heatmap of Heart Disease',
    xaxis_title='Smoking Status',
    yaxis_title='Age and BMI Groups',
    height=600,
    width=800
)

# Render the heatmap
st.plotly_chart(fig)






