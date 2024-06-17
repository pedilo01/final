import streamlit as st

st.title("Description of Different Streamlit Application")


st.header('Simple Sentiment Analyzer App')
st.image("./pic/feeling.png")

with st.expander("🔮Sentiment Analyzer"):
    st.markdown("""
    
    #
                A Sentiment Analyzer 
A sentiment analyzer is a powerful tool in natural language processing that evaluates text to determine its underlying sentiment or emotional tone.
                 Using algorithms and machine learning models, it classifies sentences or larger bodies of text as positive, negative, or neutral. 
                The analyzer examines various linguistic features, such as word choice, context, and syntax, to identify the feelings and attitudes conveyed by the text. 
                For example, if you input a sentence like "I love this new smartphone!", the sentiment analyzer would detect a positive sentiment due to the use of the word "love" and the overall enthusiastic tone.
                 Conversely, a sentence like "I am really disappointed with this service" would be classified as negative, reflecting dissatisfaction. 
                This tool is widely used in customer feedback analysis, social media monitoring, and other applications where understanding emotional responses is crucial.

                
    """, unsafe_allow_html=True)

st.header('𓍢ִ໋ Big Cats Image Classification')
st.image("./pic/cats.png")

with st.expander("Big Cats Image Classification Project"):
    st.markdown("""
    
    #
                Image Classificationse
Welcome to the Big Cat Image Classifier! This application allows you to upload an image of a big cat, and our model will identify the species for you. 
                Simply upload your image using the sidebar, and the classifier will display the predicted category.
                 This tool is perfect for anyone interested in the animal kingdom and big cats in particular.
                
    """, unsafe_allow_html=True)

st.header('🔍Prediction')
st.image("./pic/heart.png")

with st.expander("Heart Disease Predictor"):
    st.markdown("""
    
    #
                A Sentiment Analyzer 
This app uses a machine learning model to predict whether a patient is likely to have heart disease based on various medical parameters.
Simply enter the details in the form below, and click 'Predict' to see the prediction.
The parameters used for prediction include:
- Age
- Gender
- Chest Pain Type
- Resting Blood Pressure
- Cholesterol Level
- Fasting Blood Sugar
- Resting Electrocardiographic Results
- Maximum Heart Rate Achieved
- Exercise Induced Angina
- ST Depression Induced by Exercise
- Slope of the Peak Exercise ST Segment

                
    """, unsafe_allow_html=True)