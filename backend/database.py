import json
import os
from config import METADATA_FILE

def load_database():
    if not os.path.exists(METADATA_FILE):
        return []

    with open(METADATA_FILE, "r") as f:
        try:
            return json.load(f)
        except:
            return []


def save_database(data):
    with open(METADATA_FILE, "w") as f:
        json.dump(data, f, indent=4)


def add_image(image_data):
    data = load_database()
    data.append(image_data)
    save_database(data)

def get_all_images():
    return load_database()    