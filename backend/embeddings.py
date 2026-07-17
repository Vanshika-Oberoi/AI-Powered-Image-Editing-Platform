import os
import json
import pickle

import numpy as np
import faiss

from sentence_transformers import SentenceTransformer


MODEL = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


INDEX_FILE = "metadata/image_index.faiss"
DATA_FILE = "metadata/image_data.pkl"



def create_embeddings(images):

    texts = []

    for img in images:

        caption = img.get(
            "caption",
            ""
        )

        texts.append(caption)


    vectors = MODEL.encode(
        texts
    )


    vectors = np.array(
        vectors
    ).astype("float32")


    index = faiss.IndexFlatL2(
        vectors.shape[1]
    )


    index.add(
        vectors
    )


    os.makedirs(
        "metadata",
        exist_ok=True
    )


    faiss.write_index(
        index,
        INDEX_FILE
    )


    with open(
        DATA_FILE,
        "wb"
    ) as f:

        pickle.dump(
            images,
            f
        )



def search_images(query, top_k=3):

    index = faiss.read_index(
        INDEX_FILE
    )


    query_vector = MODEL.encode(
        [query]
    )


    query_vector = np.array(
        query_vector
    ).astype("float32")


    distances, ids = index.search(
        query_vector,
        top_k
    )


    with open(
        DATA_FILE,
        "rb"
    ) as f:

        images = pickle.load(f)


    results=[]


    for i in ids[0]:

        if i < len(images):

            results.append(
                images[i]
            )


    return results