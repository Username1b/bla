from flask import Flask, jsonify, request
import requests
import os
import threading
import time

app = Flask(__name__)

TARGET_URL = "https://luphtlgbcckhyhwuebpyvajszh0zdcv14.oast.fun"
SEARCH_TEXT = "bla"   
INTERVAL = 1

def auto_fetch():
    while True:
        try:
            r = requests.get(TARGET_URL)
            text = r.text
            found = SEARCH_TEXT in text
            print(f"Запрос к {TARGET_URL} | Найдено: {found} | Длина ответа: {len(text)}")
        except Exception as e:
            print(f"Ошибка запроса: {e}")
        time.sleep(INTERVAL)

threading.Thread(target=auto_fetch, daemon=True).start()

@app.route("/")
def home():
    return "Server is running!"

@app.route("/proxy")
def proxy():
    url = request.args.get("url")
    if not url:
        return {"error": "No URL provided"}, 400
    try:
        r = requests.get(url)
        text = r.text
        found = SEARCH_TEXT in text
        return {"url": url, "found": found, "length": len(text), "preview": text[:200]}
    except Exception as e:
        return {"error": str(e)}, 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 3000))
    app.run(host="0.0.0.0", port=port)
    port = int(os.environ.get("PORT", 3000))
    app.run(host="0.0.0.0", port=port)
