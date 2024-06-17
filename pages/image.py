import pickle
import streamlit as st
import pandas as pd
import pickle
from nltk.corpus import names
from PIL import Image
from io import BytesIO
from img2vec_pytorch import Img2Vec
import streamlit as st
from sklearn.exceptions import NotFittedError
from sklearn.utils.validation import check_is_fitted

# Set Streamlit page configuration
st.set_page_config(layout="wide", page_title="Image Classification for Big Cats")

# Function to load the model
def load_model():
    try:
        with open('pages/cat.p', 'rb') as f:
            model = pickle.load(f)
        return model
    except FileNotFoundError:
        st.error("Model file not found. Please upload the model file.")
        return None
    except Exception as e:
        st.error(f"Error loading the model: {e}")
        return None

# Function to check if the model is fitted
def is_model_fitted(model):
    try:
        check_is_fitted(model)
        return True
    except NotFittedError:
        return False

# Load the model
model = load_model()

# Initialize Img2Vec
img2vec = Img2Vec()

# Streamlit Web App Interface
st.write("## This image classification identifies big cats in the animal kingdom")
st.write(":grin: We'll try to identify any big cats you upload :grin:")
st.sidebar.write("## Upload and download :gear:")

MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB

# Function to convert image to bytes
@st.cache_data
def convert_image(img):
    buf = BytesIO()
    img.save(buf, format="JPEG")
    byte_im = buf.getvalue()
    return byte_im

# Function to fix and predict the image category
def fix_image(upload):
    image = Image.open(upload)
    col1.write("Image to be predicted :camera:")
    col1.image(image)

    col2.write("Category :wrench:")
    img = Image.open(upload)
    features = img2vec.get_vec(img)
    pred = model.predict([features])

    col2.header(pred[0])

col1, col2 = st.columns(2)
my_upload = st.sidebar.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if my_upload is not None:
    if my_upload.size > MAX_FILE_SIZE:
        st.error("The uploaded file is too large. Please upload an image smaller than 5MB.")
    else:
        fix_image(upload=my_upload)
else:
    st.write("by PEDILO...")