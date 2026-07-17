import streamlit as st
import os

from config import UPLOAD_FOLDER
from backend.editor import edit_image

st.set_page_config(
    page_title="Image Detail",
    layout="wide"
)

st.title("🖼 Image Detail")

if "selected_image" not in st.session_state:
    st.warning("No image selected.")
    st.stop()

filename = st.session_state["selected_image"]

path = os.path.join(UPLOAD_FOLDER, filename)

st.image(path, use_container_width=True)

st.subheader(filename)

st.write("---")

# ==========================
# Quick AI Edit Buttons
# ==========================

st.subheader("✨ Quick AI Edits")

col1, col2 = st.columns(2)

with col1:

    if st.button("🧹 Remove Background"):

        edited = edit_image(path, "Remove Background")

        st.success("Background removed successfully!")

        st.image(
            edited,
            caption="Edited Image",
            use_container_width=True
        )

    if st.button("🎨 Change Colors"):

        edited = edit_image(path, "Change Colors")

        st.success("Colors changed successfully!")

        st.image(
            edited,
            caption="Edited Image",
            use_container_width=True
        )

    if st.button("✨ Enhance Image"):

        edited = edit_image(path, "Enhance Image Quality")

        st.success("Image enhanced successfully!")

        st.image(
            edited,
            caption="Edited Image",
            use_container_width=True
        )

with col2:

    if st.button("❌ Remove Objects"):

        edited = edit_image(path, "Remove Objects")

        st.success("Objects removed successfully!")

        st.image(
            edited,
            caption="Edited Image",
            use_container_width=True
        )

    if st.button("🌄 Change Background"):

        edited = edit_image(path, "Change Background")

        st.success("Background changed successfully!")

        st.image(
            edited,
            caption="Edited Image",
            use_container_width=True
        )

    if st.button("🌈 Cartoon Style"):

        edited = edit_image(path, "Convert to Cartoon Style")

        st.success("Cartoon style applied!")

        st.image(
            edited,
            caption="Edited Image",
            use_container_width=True
        )

st.write("---")

# ==========================
# Custom AI Prompt
# ==========================

st.subheader("📝 Custom AI Edit")

prompt = st.text_area(
    "Describe your edit",
    height=150,
    placeholder="Example:\nRemove the person on the left, replace the background with snowy mountains and make the sky sunset."
)

if st.button("🚀 Generate AI Edit"):

    if prompt.strip() == "":
        st.warning("Please enter an editing instruction.")

    else:

        edited = edit_image(path, prompt)

        st.success("AI edit completed successfully!")

        st.image(
            edited,
            caption="Edited Image",
            use_container_width=True
        )

st.write("---")

# ==========================
# Version History (Placeholder)
# ==========================

st.subheader("🕒 Version History")

edited_folder = "edited"

if os.path.exists(edited_folder):

    versions = sorted(os.listdir(edited_folder), reverse=True)

    if len(versions) == 0:
        st.info("No edited versions available yet.")

    else:

        for version in versions:

            if version.startswith(os.path.splitext(filename)[0]):

                st.write(version)

else:

    st.info("No edited versions available.")