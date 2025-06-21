from google import genai
from google.genai import types

import requests
import os


class ImageAnalysis:
    def __init__(self, image_path, api_key):
        self.image_path = image_path
        self.image_bytes = requests.get(image_path).content
        self.image = types.Part.from_bytes(
            data=self.image_bytes, mime_type="image/jpeg"
        )
        self.client = genai.Client(api_key=api_key)

    def analyze(self):
        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=["What is this image?", self.image],
        )
        return response.text


if __name__ == "__main__":
    image_analysis = ImageAnalysis(
        "https://goo.gle/instrument-img",
        api_key=os.getenv("GOOGLE_API_KEY"),
    )
    print(image_analysis.analyze())
