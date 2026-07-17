import streamlit as st
import os
import json

from config import UPLOAD_FOLDER, METADATA_FOLDER
from backend.editor import edit_image


st.set_page_config(
    page_title="Image Detail",
    layout="wide"
)


st.title("🖼 Image Detail")


# ==========================
# Check Selected Image
# ==========================

if "selected_image" not in st.session_state:
    st.warning("No image selected.")
    st.stop()


filename = st.session_state["selected_image"]

image_path = os.path.join(
    UPLOAD_FOLDER,
    filename
)


# ==========================
# Original Image
# ==========================

st.image(
    image_path,
    use_container_width=True
)

st.subheader(filename)

st.write("---")


# ==========================
# Quick AI Edit Buttons
# ==========================

st.subheader("✨ Quick AI Edits")


col1, col2, col3 = st.columns(3)


with col1:

    if st.button("🧹 Remove Background"):

        edited = edit_image(
            image_path,
            "Remove Background"
        )

        st.success(
            "Background removed successfully!"
        )

        st.image(
            edited,
            caption="Edited Version",
            use_container_width=True
        )



with col2:

    if st.button("❌ Remove Objects"):

        edited = edit_image(
            image_path,
            "Remove unwanted objects"
        )

        st.success(
            "Objects removed successfully!"
        )

        st.image(
            edited,
            caption="Edited Version",
            use_container_width=True
        )



with col3:

    if st.button("✨ Enhance Image"):

        edited = edit_image(
            image_path,
            "Enhance image quality"
        )

        st.success(
            "Image enhanced successfully!"
        )

        st.image(
            edited,
            caption="Edited Version",
            use_container_width=True
        )



col4, col5, col6 = st.columns(3)


with col4:

    if st.button("🎨 Change Colors"):

        edited = edit_image(
            image_path,
            "Change image colors professionally"
        )

        st.success(
            "Colors changed!"
        )

        st.image(
            edited,
            caption="Edited Version",
            use_container_width=True
        )



with col5:

    if st.button("🌄 Change Background"):

        edited = edit_image(
            image_path,
            "Change background"
        )

        st.success(
            "Background changed!"
        )

        st.image(
            edited,
            caption="Edited Version",
            use_container_width=True
        )



with col6:

    if st.button("🌈 Cartoon Style"):

        edited = edit_image(
            image_path,
            "Convert image into cartoon style"
        )

        st.success(
            "Cartoon style applied!"
        )

        st.image(
            edited,
            caption="Edited Version",
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
    placeholder=
    "Example: Remove the person on left and add a sunset background."
)



if st.button("🚀 Generate AI Edit"):

    if prompt.strip() == "":

        st.warning(
            "Please enter an editing instruction."
        )

    else:

        with st.spinner(
            "AI is processing your request..."
        ):

            edited = edit_image(
                image_path,
                prompt
            )


        st.success(
            "AI edit completed successfully!"
        )


        st.image(
            edited,
            caption="Generated Version",
            use_container_width=True
        )



st.write("---")


# ==========================
# Version History
# ==========================

st.subheader("🕒 Edit Version History")


HISTORY_FILE = os.path.join(
    METADATA_FOLDER,
    "history.json"
)



def load_history():

    if not os.path.exists(HISTORY_FILE):

        return []

    with open(
        HISTORY_FILE,
        "r"
    ) as f:

        return json.load(f)



history = load_history()



image_history = []


for item in history:

    if item["original"] == filename:

        image_history.append(item)



if len(image_history) == 0:

    st.info(
        "No edited versions available yet."
    )


else:

    st.write(
        f"Total Versions: {len(image_history)}"
    )


    cols = st.columns(3)


    for i, item in enumerate(
        reversed(image_history)
    ):


        version_path = os.path.join(
            "edited",
            item["edited_file"]
        )


        with cols[i % 3]:


            if os.path.exists(version_path):

                st.image(
                    version_path,
                    use_container_width=True
                )


            st.caption(
                item["edited_file"]
            )


            st.write(
                "📝 Prompt:"
            )

            st.write(
                item["prompt"]
            )


            st.write(
                "🕒 Time:"
            )

            st.write(
                item["timestamp"]
            )