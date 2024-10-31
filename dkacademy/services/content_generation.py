import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


class GeminiService:

    def __init__(self, system_instruction: str):
        self.model = genai.GenerativeModel(
            os.getenv("GEMINI_MODEL_NAME"),
            system_instruction=system_instruction)

    def generate_content(self, prompt: str):
        response = self.model.generate_content(prompt)
        return response.text
