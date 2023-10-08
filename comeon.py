import streamlit as st
import tensorflow as tf
from tensorflow.keras.models import load_model
from PIL import Image
import os

MODELSPATH = 'waste_model.h5'
DATAPATH = 'waste1.jpg'
IMAGE_DIR = 'images'  # Directory containing recycling images

# Function to load data
@st.cache
def load_data():
    img = Image.open(DATAPATH)
    return img

# Function to load models
def load_models():
    model = load_model(MODELSPATH, compile=False)
    return model

# Set page title and background
st.set_page_config(
    page_title="Recycling Importance & Waste Prediction",
    page_icon="🔄",
    layout="wide",
)

# Add a title with a background image
st.markdown(
    """
    <style>
        .title-text {
            font-size: 36px;
            font-weight: bold;
            color: #ffffff;
        }
        .title-container {
            display: flex;
            align-items: center;
            justify-content: center;
            background-image: url('https://img.freepik.com/free-vector/green-set-recycled-signs_78370-662.jpg?w=2000');
            background-size: cover;
            background-position: center;
            height: 300px;
        }
    </style>
    <div class="title-container">
        <div class="title-text">The Importance of Recycling</div>
    </div>
    """,
    unsafe_allow_html=True
)

# Add some information about recycling
st.markdown(
    """
    Recycling is crucial for preserving our environment and conserving natural resources. It helps reduce pollution, 
    saves energy, and reduces the need for raw materials. By recycling, we can contribute to a more sustainable and 
    eco-friendly future.
    """
)

# Add images related to recycling
recycling_images = ['https://img.freepik.com/free-vector/green-set-recycled-signs_78370-662.jpg?w=2000']  
st.image(recycling_images, caption=["Recycling Image 1"], width=300)

# Sidebar for page selection
st.sidebar.title('Select options:')
page = st.sidebar.selectbox("Choose a page:", ["Sample Data", "Upload an Image"])

if page == "Sample Data":
    st.header("Sample prediction for waste")
    if st.checkbox('Show Sample Data'):
        st.info("Sample image:")
        image = load_data()
        st.image(image, caption='Sample Data', use_column_width=True)
        image = image.resize((64, 64))
        image = tf.keras.preprocessing.image.img_to_array(image)
        image = image.reshape((1, 64, 64, 3))
        st.subheader("Check waste prediction")
        if st.checkbox('Show Prediction of simple image'):
            model = load_models()
            result = model.predict(image)
            st.write(result)
            if result[0][0] == 1:
                prediction = 'Recyclable Waste'
            else:
                prediction = 'Organic Waste'
            st.write(prediction)
            st.success("It is prediction for sample image!")

if page == "Upload an Image":
    st.header("Your prediction of waste")
    uploaded_file = st.file_uploader("Choose your image", type=["jpg", "png"])
    if uploaded_file is not None:
        img = Image.open(uploaded_file)
        st.info("Show your image:")
        st.image(img, caption="Upload image", use_column_width=True)
        img = img.resize((64, 64))
        img = tf.keras.preprocessing.image.img_to_array(img)
        img = img.reshape((1, 64, 64, 3))
        st.subheader("Check waste prediction")
        if st.checkbox('Show Prediction of your image'):
            model = load_models()
            result = model.predict(img)
            st.write(result)
            if result[0][0] == 1:
                prediction = 'Recyclable Waste'
            else:
                prediction = 'Organic Waste'
            st.write(prediction)
            st.success("That is your prediction!")
