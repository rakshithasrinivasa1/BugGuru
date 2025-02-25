import os
from dotenv import load_dotenv
import openai

# Load API key from .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
