import os
import uuid
from PIL import Image
from config import UPLOAD_FOLDER

def save_uploaded_image(uploaded_file):

    extension = uploaded_file.name.split(".")[-1]

    filename = f"{uuid.uuid4()}.{extension}"

    filepath = os.path.join(UPLOAD_FOLDER, filename)

    image = Image.open(uploaded_file)

    image.save(filepath)

    return filename, filepath