
import os
from dotenv import load_dotenv

load_dotenv()

class Settings:

    API_KEY = os.getenv("GROQ_API_KEY")

    LLM_API_URL = "https://api.groq.com/openai/v1"

    MODEL = "openai/gpt-oss-120b"
