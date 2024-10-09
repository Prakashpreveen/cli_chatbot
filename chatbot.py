import requests
from dotenv import load_dotenv
import os
from yaspin import yaspin

load_dotenv(override=True)

BASE_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-pro:generateContent?key="
API_KEY = os.getenv("API_KEY")
url = BASE_URL + API_KEY

def chat_with_gemini(prompt):
    json = {
        "contents": [
            {
            "role": "user",
            "parts": [
                {
                "text": prompt
                }
            ]
            }
        ],
        "generationConfig": {
            "temperature": 1,
            "topK": 64,
            "topP": 0.95,
            "maxOutputTokens": 8192,
            "responseMimeType": "text/plain"
        }
    }
    response = requests.post(url,json=json)
    res_json = response.json()
    return res_json["candidates"][0]["content"]["parts"][0]["text"]

if __name__ == "__main__":
    while True:
        user_prompt = input("You: ")
        if user_prompt.lower() in ["end","quit","bye"]:
            break
        with yaspin() as spinner:
            response = chat_with_gemini(user_prompt)
            spinner.hide()
            print("Chatbot: ",response)
