import os
import shutil
from datetime import datetime
import json
from backend.prompts import custom_edit_prompt

from config import EDITED_FOLDER, METADATA_FOLDER


HISTORY_FILE = os.path.join(
    METADATA_FOLDER,
    "history.json"
)


def load_history():

    if not os.path.exists(HISTORY_FILE):
        return []

    with open(HISTORY_FILE, "r") as f:
        return json.load(f)



def save_history(data):

    with open(HISTORY_FILE, "w") as f:
        json.dump(
            data,
            f,
            indent=4
        )


def generate_version_name(filename):

    name, ext = os.path.splitext(filename)

    versions = load_history()

    count = 1

    for item in versions:

        if item.get("original") == filename:

            count += 1


    return f"{name}_v{count}{ext}"


def edit_image(image_path, prompt):

    """
    AI editing pipeline placeholder.

    Later Gemini/OpenAI image API will be connected here.
    """

    if not os.path.exists(EDITED_FOLDER):

        os.makedirs(
            EDITED_FOLDER
        )


    filename = os.path.basename(image_path)


    new_filename = generate_version_name(
        filename
    )


    new_path = os.path.join(
        EDITED_FOLDER,
        new_filename
    )


    # Temporary simulation
    # Replace this with AI API response later

    shutil.copy(
        image_path,
        new_path
    )


    history = load_history()


    history.append({

        "original": filename,

        "edited_file": new_filename,

        "prompt": custom_edit_prompt(prompt),

        "timestamp":
        datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

    })


    save_history(history)


    return new_path