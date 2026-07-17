from backend.database import get_all_images
from backend.embeddings import create_embeddings


images = get_all_images()


create_embeddings(
    images
)


print(
    "Embedding index created!"
)