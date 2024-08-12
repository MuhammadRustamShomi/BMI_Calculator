

import streamlit as st

# Title of the web application
st.title("BMI Calculator")

# Getting user input for weight and height
weight = st.number_input("Enter your weight in kg:", min_value=0.0, format="%.2f")
height = st.number_input("Enter your height in metres:", min_value=0.0, format="%.2f")

# BMI calculation button
if st.button("Calculate BMI"):
    if height > 0:  # To ensure height is not zero
        bmi = weight / (height ** 2)
        st.write(f"Your body mass index (BMI) = {round(bmi, 2)}")

        # Providing feedback based on the BMI
        if bmi < 18.5:
            st.error("You are in the Underweight category, check your diet and gain some weight!")
        elif 18.5 <= bmi < 25:
            st.success("You are in the Normal Weight category, keep it up!")
        else:
            st.warning("You are in the Overweight category, you should try hitting the gym and check your diet as well!")
    else:
        st.error("Height cannot be zero!")