from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/proxy")
def proxy():
    try:
        r = requests.get("https://luphtlgbcckhyhwuebpyvajszh0zdcv14.oast.fun")
        return jsonify(r.json())
    except:
        return {"error": "request failed"}, 500

app.run(host="0.0.0.0", port=3000)
