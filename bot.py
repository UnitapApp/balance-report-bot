import requests
from config import API_TOKEN

CHANNEL_ID = -1001609474777
BASE_URL = f"https://api.telegram.org/bot{API_TOKEN}"


def send_message(text):
    url = f"{BASE_URL}/sendMessage"
    payload = {"chat_id": CHANNEL_ID, "text": text}
    response = requests.post(url, data=payload)
    return response.json()
