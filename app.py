import streamlit as st
from PIL import Image, ImageOps
import numpy as np

st.title("Live Mobile Camera Input App")
st.write("Camera se photo capture karo aur grayscale dekho!")

# Camera input widget
camera_image = st.camera_input("Take a picture")

if camera_image:
    # PIL image me convert
    img = Image.open(camera_image)
    
    # Show original image
    st.image(img, caption="Original Image", use_column_width=True)
    
    # Convert to grayscale
    img_gray = ImageOps.grayscale(img)
    st.image(img_gray, caption="Grayscale Image", use_column_width=True)
