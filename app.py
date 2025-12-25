import streamlit as st
from PIL import Image, ImageOps

st.set_page_config(page_title="Mobile Image App", layout="centered")
st.title("Mobile Image Processing App")
st.write("Do options: Upload image ya Live camera capture!")

# --- Feature 1: Upload existing image ---
st.subheader("1️⃣ Upload image from mobile/gallery")
uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    img = Image.open(uploaded_file)
    st.image(img, caption="Original Image", use_column_width=True)
    
    # Grayscale conversion
    img_gray = ImageOps.grayscale(img)
    st.image(img_gray, caption="Grayscale Image", use_column_width=True)

# --- Feature 2: Live camera input ---
st.subheader("2️⃣ Capture live photo from camera")
camera_image = st.camera_input("Take a picture")

if camera_image:
    cam_img = Image.open(camera_image)
    st.image(cam_img, caption="Live Camera Image", use_column_width=True)
    
    # Grayscale conversion
    cam_gray = ImageOps.grayscale(cam_img)
    st.image(cam_gray, caption="Grayscale Live Image", use_column_width=True)
