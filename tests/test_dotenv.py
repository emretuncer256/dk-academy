import os
import pytest


def test_dotenv_file_exists():
    dotenv_path = os.path.join(os.getcwd(), '.env')
    assert os.path.isfile(
        dotenv_path
    ), ".env file not found. Please ensure it exists in the project root directory."


def test_api_key_exists():
    API_KEY = os.getenv("GEMINI_API_KEY")
    assert isinstance(
        API_KEY, str
    ), "GEMINI_API_KEY not found in environment variables. Please ensure it is set in the .env file."
