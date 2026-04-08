from flask import Flask, jsonify, request
import requests
import os

app = Flask(__name__)

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
        text = r.text  # <- берём HTML как текст

        # ищем нужный текст
        if "нужная_информация" in text:
            found = True
        else:
            found = False

        return {"found": found, "length": len(text)}
    except Exception as e:
        return {"error": str(e)}, 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 3000))
    app.run(host="0.0.0.0", port=port)
