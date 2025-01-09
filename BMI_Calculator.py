import streamlit as st

# Set page configuration
st.set_page_config(page_title="BMI Calculator", page_icon="🏋️", layout="centered")

# Custom CSS to improve the app's appearance
st.markdown("""
<style>
    .main {
        background-color: #001f3f;
        color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .stButton > button {
        width: 100%;
        background-color: #0074D9;
        color: white;
        font-weight: bold;
    }
    .result {
        font-size: 24px;
        font-weight: bold;
        margin-top: 20px;
    }
    .stTextInput > div > div > input {
        color: black;
    }
    .stNumberInput > div > div > input {
        color: black;
    }
</style>
""", unsafe_allow_html=True)

# Title of the web application
st.title("🏋️ BMI Calculator")

# Create two columns for input fields
col1, col2 = st.columns(2)

with col1:
    weight = st.number_input("Enter your weight (kg)", min_value=0.0, max_value=500.0, value=70.0, step=0.1, format="%.1f")

with col2:
    height = st.number_input("Enter your height (m)", min_value=0.0, max_value=3.0, value=1.70, step=0.01, format="%.2f")

# BMI calculation button
if st.button("Calculate BMI"):
    if height > 0:
        bmi = weight / (height ** 2)
        st.markdown(f"<div class='result'>Your BMI: {bmi:.2f}</div>", unsafe_allow_html=True)

        # Providing feedback based on the BMI
        if bmi < 18.5:
            st.error("You are in the Underweight category. Consider consulting a nutritionist to gain healthy weight.")
        elif 18.5 <= bmi < 25:
            st.success("You are in the Normal Weight category. Keep up the good work!")
        elif 25 <= bmi < 30:
            st.warning("You are in the Overweight category. Consider adopting a healthier lifestyle.")
        else:
            st.error("You are in the Obese category. It's recommended to consult a healthcare professional.")

        # Display a BMI chart
        st.image("https://www.cdc.gov/healthyweight/images/assessing/bmi-adult-fb-600x315.jpg", caption="BMI Categories")
    else:
        st.error("Height cannot be zero!")

# Add some health tips
st.markdown("---")
st.subheader("💡 Health Tips")
st.markdown("""
- Maintain a balanced diet rich in fruits, vegetables, and whole grains.
- Stay hydrated by drinking plenty of water throughout the day.
- Engage in regular physical activity for at least 30 minutes a day.
- Get adequate sleep, aiming for 7-9 hours per night.
- Manage stress through relaxation techniques or mindfulness practices.
""")
