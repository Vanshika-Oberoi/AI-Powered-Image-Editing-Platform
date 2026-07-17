import streamlit as st
import os

from backend.embeddings import search_images
from config import UPLOAD_FOLDER


st.title(
    "🔍 AI Image Search"
)


query = st.text_input(
    "Search images",
    placeholder="Example: beach sunset mountain"
)



if st.button("Search"):


    results = search_images(
        query
    )


    if len(results)==0:

        st.info(
            "No matching images found"
        )


    else:


        cols = st.columns(3)


        for i,img in enumerate(results):


            path=os.path.join(
                UPLOAD_FOLDER,
                img["filename"]
            )


            with cols[i%3]:

                st.image(
                    path,
                    use_container_width=True
                )


                st.write(
                    img["caption"]
                )