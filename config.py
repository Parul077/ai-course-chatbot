import os
from dotenv import load_dotenv

load_dotenv()

OPENRouter_API_KEY = os.getenv("OPENRouter_API_KEY")

# Using the model that we confirmed works with your free tier settings
MODEL_NAME = "meta-llama/llama-3.3-70b-instruct:free"
BASE_URL = "https://openrouter.ai/api/v1"