
import requests
from config.settings import Settings

class LLMClient:
    def __init__(self):
        if not Settings.API_KEY:
            raise ValueError(
                "GROQ_API_KEY environment variable is missing"
            )

        self.url = Settings.LLM_API_URL

        self.headers ={
            "Authorization" : f"Bearer {Settings.API_KEY}",
            "Content_Type" : "Application/json"
        }
    def generate_response(self, prompt):

        payload ={
            "model": Settings.MODEL,
            "messages": [
                      {
                          "role": "user",
                          "content" : prompt

                      }
                  ],
                  "temperature" : 0.3
                  }
        response = requests.post(
            self.url,
            headers=self.headers,
            json=payload,
            timeout=30
         )
        print("Status code:", response.status_code)
        print("Response body:", response.text)
        response.raise_for_status()
        return response.json()