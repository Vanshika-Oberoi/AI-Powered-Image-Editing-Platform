from google import genai
from PIL import Image
from config import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)

def generate_caption(image_path):
    image = Image.open(image_path)

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=[
            "Describe this image in one detailed sentence.",
            image
        ]
    )

    return response.text