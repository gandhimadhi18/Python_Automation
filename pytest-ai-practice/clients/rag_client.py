import requests
from config.settings import Settings

class RAGClient:
    def __init__(self):

      self.url = Settings.RAG_API_URL
      self.headers ={
        "Authorization": f"Bearer{Settings.API_KEY}",
        "Content-Type": "application/json"
        }
    def ask_question(self, question):
        payload = {"question" : question}
        response = requests.post(
            self.url,
            headers = self.headers,
            json=payload,
            timeout=Settings.TIMEOUT
        )
        response.raise_for_status()
        return response.json()