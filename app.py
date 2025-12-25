import streamlit as st
from PIL import Image
import numpy as np
import cv2

st.set_page_config(page_title="Halki Streamlit Web App", layout="centered")
st.title("Halki Image Processing App")
st.write("Upload karo apni image aur grayscale dekho!")

# Image uploader
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Original Image", use_column_width=True)
    
    # Convert to grayscale
    img_cv = np.array(image)
    img_gray = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)
    st.image(img_gray, caption="Grayscale Image", use_column_width=True, channels="GRAY")
