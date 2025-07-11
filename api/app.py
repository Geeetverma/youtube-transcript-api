from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/transcript')
def transcript():
    video_id = request.args.get('videoId')
    if not video_id:
        return jsonify({"error": "Missing videoId"}), 400

    url = f"https://www.youtube.com/watch?v={video_id}"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return jsonify({"error": "Failed to load YouTube page"}), 500

    return response.text
