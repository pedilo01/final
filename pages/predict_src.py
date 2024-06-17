import streamlit as st


st.header('Prediction Source Code')
st.subheader('This python code is implemented for Streamlit')
st.code(''' 
 # Notes
# do a "pip install streamlit" first 
# to run on terminal issue this command
# python -m streamlit run streamlit_test.py

import streamlit as st
import pickle

# Load the trained Naive Bayes classifier from the saved file
filename = 'pages/heart.csv'
with open(filename, 'rb') as file:
    loaded_model = pickle.load(file)

st.title("Heart Disease Predictor 🩺")
st.subheader("Enter patient details to predict heart disease status:")

# User inputs for patient details
age_input = st.number_input("Age:", min_value=1, max_value=120, step=1, value=50)
gender_input = st.selectbox("Gender:", ["Male", "Female"])
chest_pain_type_input = st.selectbox("Chest Pain Type:", ["ATA", "NAP", "ASY", "TA"])
resting_bp_input = st.number_input("Resting Blood Pressure:", min_value=50, max_value=200, step=1, value=120)
cholesterol_input = st.number_input("Cholesterol (mg/dl):", min_value=100, max_value=600, step=1, value=200)
fasting_bs_input = st.selectbox("Fasting Blood Sugar > 120 mg/dl", [0, 1])
resting_ecg_input = st.selectbox("Resting Electrocardiographic Results", ["Normal", "ST", "LVH"])
max_hr_input = st.number_input("Maximum Heart Rate Achieved:", min_value=50, max_value=220, step=1, value=150)
exercise_angina_input = st.selectbox("Exercise Induced Angina", ["Yes", "No"])
oldpeak_input = st.number_input("ST Depression Induced by Exercise:", min_value=0.0, max_value=10.0, step=0.1, value=1.0)
st_slope_input = st.selectbox("Slope of the Peak Exercise ST Segment", ["Up", "Flat", "Down"])

# Function to make a prediction
def predict_heart_disease(age, gender, chest_pain_type, resting_bp, cholesterol, fasting_bs, resting_ecg, max_hr, exercise_angina, oldpeak, st_slope):
    # Encode the categorical variables as required by the model
    gender = 1 if gender == "Male" else 0
    chest_pain_type = {"ATA": 1, "NAP": 2, "ASY": 3, "TA": 4}[chest_pain_type]
    resting_ecg = {"Normal": 0, "ST": 1, "LVH": 2}[resting_ecg]
    exercise_angina = 1 if exercise_angina == "Yes" else 0
    st_slope = {"Up": 1, "Flat": 2, "Down": 3}[st_slope]

    # Prepare the features for prediction
    features = [age, gender, chest_pain_type, resting_bp, cholesterol, fasting_bs, resting_ecg, max_hr, exercise_angina, oldpeak, st_slope]

    # Use the model to get the prediction
    prediction = loaded_model.predict([features])
    return prediction[0]

# Display button and result
if st.button('Predict'):
    predicted_status = predict_heart_disease(age_input, gender_input, chest_pain_type_input, resting_bp_input, cholesterol_input, fasting_bs_input, resting_ecg_input, max_hr_input, exercise_angina_input, oldpeak_input, st_slope_input)
    st.text("The predicted heart disease status based on the given patient details is:")
    st.text_area(label="", value=str(predicted_status), height=100)

''')