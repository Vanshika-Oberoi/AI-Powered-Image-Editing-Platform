import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

UPLOAD_FOLDER = "uploads"
EDITED_FOLDER = "edited"
VERSION_FOLDER = "versions"
METADATA_FILE = "metadata/images.json"