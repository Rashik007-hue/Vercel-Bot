import os
import json
import requests

BOT_TOKEN = os.environ.get("BOT_TOKEN")
API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

def handler(request):
    body = request.get_json() if hasattr(request, "get_json") else json.loads(request.body)

    if "message" in body:
        chat_id = body["message"]["chat"]["id"]
        text = body["message"]["text"]

        reply = "আপনি লিখেছেন: " + text if text != "/start" else "👋 হ্যালো! আমি Vercel Python Telegram Bot ✅"

        requests.post(API_URL, json={"chat_id": chat_id, "text": reply})

    return {"statusCode": 200, "body": "ok"}
