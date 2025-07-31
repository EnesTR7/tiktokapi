from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "TikTok API çalışıyor! 🚀"

@app.route("/gettiktok", methods=["POST"])
def get_tiktok():
    data = request.get_json()
    if not data or "url" not in data:
        return jsonify({"error": "TikTok URL'si eksik"}), 400

    tiktok_url = data["url"]

    api_url = "https://tiktok-video-no-watermark2.p.rapidapi.com/no-watermark"

    payload = {
        "url": tiktok_url,
        "hd": "0"
    }

    headers = {
        "User-Agent": "okhttp/3.12.0",
        "Accept-Encoding": "gzip",
        "x-rapidapi-host": "tiktok-video-no-watermark2.p.rapidapi.com",
        "x-rapidapi-key": "b7a226349dmshe6962f8400d6eedp1d6c1ejsne5229da5f4cc"  # Kendi anahtarını kullan
    }

    try:
        response = requests.post(api_url, json=payload, headers=headers)
        response.raise_for_status()  # HTTP hata kodlarını tetikle
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        print(f"RapidAPI isteğinde hata: {e}")
        return jsonify({"error": f"RapidAPI isteği başarısız: {str(e)}"}), 500
    except Exception as e:
        print(f"Beklenmeyen hata: {e}")
        return jsonify({"error": f"Beklenmeyen hata: {str(e)}"}), 500

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
