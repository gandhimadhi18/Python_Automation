# import os
# class Settings:
#     LLM_API_URL = ("https://api.groq.com/openai/v1/chat/completions")
#
#
#     # RAG_API_URL =os.getenv("RAG_API_URL", "")
#     API_KEY = os.getenv("GROQ_API_KEY")
#     MODEL_NAME = "openai/gpt-oss-20b"
#     TIMEOUT = 30
# import os
#
# class Settings:
#     API_KEY = os.getenv("GROQ_API_KEY")
#     LLM_API_URL = "https://api.groq.com/openai/v1/chat/completions"
#     MODEL = "llama-3.3-70b-versatile"

import os
from dotenv import load_dotenv
load_dotenv()
class Settings:

    API_KEY = os.getenv("GROQ_API_KEY")

    # LLM_API_URL = "https://api.groq.com/openai/v1/chat/completions"
    #
    # MODEL = "openai/gpt-oss-120b"
    LLM_API_URL = "https://api.groq.com/openai/v1"
    MODEL = "llama-3.3-70b-versatile"