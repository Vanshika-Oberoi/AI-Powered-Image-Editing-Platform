import streamlit as st
import os

from backend.database import get_all_images
from config import UPLOAD_FOLDER

st.set_page_config(page_title="Image Library", layout="wide")

st.title("🖼 AI Image Library")

images = get_all_images()

search = st.text_input(
    "🔍 Search images",
    placeholder="Example: dog, beach, mountain, person..."
)

if search:

    search = search.lower()

    filtered = []

    for img in images:

        if search in img["caption"].lower():

            filtered.append(img)

    images = filtered

st.write(f"### {len(images)} Image(s) Found")

if len(images) == 0:

    st.info("No matching images found.")

    st.stop()

cols = st.columns(3)

for i, image in enumerate(images):

    with cols[i % 3]:

        path = os.path.join(
            UPLOAD_FOLDER,
            image["filename"]
        )

        st.image(
            path,
            use_container_width=True
        )

        st.write(f"**{image['filename']}**")

        st.caption(image["caption"])

        if st.button(
            "👁 View Details",
            key=i
        ):

            st.session_state.selected_image = image["filename"]

            st.switch_page(
                "pages/2_Image_Detail.py"
            )