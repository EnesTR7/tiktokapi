from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "TikTok API ayakta! 🚀"

# Örnek TikTok endpoint'i
@app.route("/gettiktok", methods=["POST"])
def get_tiktok():
    # burada senin TikTok işlemlerin olacak
    return jsonify({"status": "ok"})

    api_url = "https://tiktok-video-no-watermark2.p.rapidapi.com"
    payload = {
        'url': tiktok_url,
        'hd': "0"
    }

    headers = {
        'User-Agent': "okhttp/3.12.0",
        'Accept-Encoding': "gzip",
        'x-rapidapi-host': "tiktok-video-no-watermark2.p.rapidapi.com",
        'x-rapidapi-key': "b7a226349dmshe6962f8400d6eedp1d6c1ejsne5229da5f4cc"
    }

    response = requests.post(api_url, data=payload, headers=headers)
    return jsonify(response.json())

if __name__ == "__main__":
    app.run(debug=True)
