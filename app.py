import streamlit as st

# Title
st.title("BMI Calculator")

# Inputs
weight = st.number_input("Enter your weight (kg):", min_value=0.0, format="%.2f")
height = st.number_input("Enter your height (meters):", min_value=0.0, format="%.2f")

# Calculate BMI
if st.button("Calculate BMI"):
    if height > 0:
        bmi = weight / (height ** 2)
        st.success(f"Your BMI is: {bmi:.2f}")
        
        # BMI Categories
        if bmi < 18.5:
            st.info("Category: Underweight")
        elif 18.5 <= bmi < 25:
            st.info("Category: Normal weight")
        elif 25 <= bmi < 30:
            st.warning("Category: Overweight")
        else:
            st.error("Category: Obese")
    else:
        st.error("Height must be greater than 0")
