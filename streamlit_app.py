import streamlit as st
import numpy as np
import pickle

# Load model
model = pickle.load(open("model.pkl", "rb"))

st.title("Medical Insurance Cost Prediction")

# Inputs
age = st.number_input("Age", 1, 100, 25)
sex = st.selectbox("Sex", ["male", "female"])
bmi = st.number_input("BMI", 10.0, 60.0, 25.0)
children = st.number_input("Children", 0, 10, 1)
smoker = st.selectbox("Smoker", ["yes", "no"])
region = st.selectbox("Region", ["southeast", "southwest", "northwest", "northeast"])

# Encoding
sex = 1 if sex == "male" else 0
smoker = 1 if smoker == "yes" else 0

region_map = {'southeast':0, 'southwest':1, 'northwest':2, 'northeast':3}
region = region_map[region]

# Predict
if st.button("Predict Insurance Cost"):
    input_data = np.array([[age, sex, bmi, children, smoker, region]])
    prediction = model.predict(input_data)
    st.success(f"Estimated Insurance Cost: ${prediction[0]:.2f}")

