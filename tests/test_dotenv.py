import os

API_KEY = os.getenv("GEMINI_API_KEY")
assert isinstance(API_KEY, str), "GEMINI_API_KEY not found in environment variables. Please ensure it is set in the .env file."