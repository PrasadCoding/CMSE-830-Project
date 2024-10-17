import streamlit as st
import matplotlib.pyplot as plt

# Set page title and description
st.title("BMI Calculator")
st.write("Calculate your Body Mass Index (BMI) and visualize your BMI category.")

# Input form for height and weight
st.subheader("Enter your details:")

height = st.number_input("Height (in cm):", min_value=50, max_value=250, step=1)
weight = st.number_input("Weight (in kg):", min_value=20, max_value=200, step=1)

# BMI Calculation
if height > 0 and weight > 0:
    height_m = height / 100  # Convert height to meters
    bmi = weight / (height_m ** 2)
    st.write(f"Your BMI is: **{bmi:.2f}**")

    # Determine BMI category
    if bmi < 18.5:
        category = "Underweight"
        color = "blue"
    elif 18.5 <= bmi < 24.9:
        category = "Normal weight"
        color = "green"
    elif 25 <= bmi < 29.9:
        category = "Overweight"
        color = "orange"
    else:
        category = "Obese"
        color = "red"

    st.write(f"Based on your BMI, you are in the **{category}** category.")

    # Visualization of BMI category
    fig, ax = plt.subplots(figsize=(5, 3))
    ax.barh([category], [bmi], color=color)
    ax.set_xlim(0, 40)
    ax.set_xlabel("BMI Value")
    st.pyplot(fig)

else:
    st.write("Please enter valid height and weight values.")
