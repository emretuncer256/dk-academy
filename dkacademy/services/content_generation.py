import google.generativeai as genai
import os
import json
from models import Content

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


class GeminiService:

    def __init__(self, system_instruction: str):
        self.model = genai.GenerativeModel(
            os.getenv("GEMINI_MODEL_NAME"),
            system_instruction=system_instruction)

    def generate_content(self, prompt: str):
        response = self.model.generate_content(prompt)
        return self._response_to_content(response)

    def _response_to_content(self, response: str):
        content = response.text
        content = content.replace("```json", "").replace("```", "")
        content = json.loads(content)
        return Content.from_json(content)
