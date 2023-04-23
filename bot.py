import requests
from config import API_TOKEN

CHANNEL_ID = -1001609474777
BASE_URL = f"https://api.telegram.org/bot{API_TOKEN}"


def send_message(text):
    url = f"{BASE_URL}/sendMessage"
    payload = {"chat_id": CHANNEL_ID, "text": text,
               "parse_mode": "MarkdownV2", "disable_web_page_preview": True}
    response = requests.post(url, data=payload)
    return response.json()


def pin_message(message_id):
    url = f"{BASE_URL}/pinChatMessage"
    payload = {"chat_id": CHANNEL_ID, "message_id": message_id}
    response = requests.post(url, data=payload)
    return response.json()
