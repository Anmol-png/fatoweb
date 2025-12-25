import streamlit as st
from PIL import Image, ImageOps

st.title("Halki Image Processing App")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Original Image", use_column_width=True)
    
    # Grayscale conversion without cv2
    img_gray = ImageOps.grayscale(image)
    st.image(img_gray, caption="Grayscale Image", use_column_width=True)
