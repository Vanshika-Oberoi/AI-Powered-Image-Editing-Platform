import streamlit as st
import os
from PIL import Image
from datetime import datetime

from backend.caption import generate_caption
from backend.database import add_image
from config import UPLOAD_FOLDER

# ----------------------------
# Create upload folder if needed
# ----------------------------
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

st.set_page_config(
    page_title="AI Image Editing Platform",
    layout="wide"
)

st.title("🎨 AI-Powered Image Editing Platform")
st.write("Upload an image and let AI generate a caption.")

uploaded_file = st.file_uploader(
    "Choose an image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    # Save image
    image_path = os.path.join(UPLOAD_FOLDER, uploaded_file.name)

    with open(image_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Display image
    image = Image.open(image_path)

    st.image(
        image,
        caption="Uploaded Image",
        use_container_width=True
    )

    # Generate AI caption
    try:
        with st.spinner("Generating AI caption..."):
            caption = generate_caption(image_path)

    except Exception as e:
        st.warning("⚠️ AI Caption unavailable. Image has still been saved.")
        print(e)
        caption = "AI caption unavailable"

    # Save metadata
    image_data = {
        "filename": uploaded_file.name,
        "caption": caption,
        "upload_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    add_image(image_data)

    st.success("✅ Image uploaded successfully!")

    st.subheader("AI Caption")

    st.write(caption)