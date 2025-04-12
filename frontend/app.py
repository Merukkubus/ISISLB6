from flask import Flask, jsonify, send_file
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

BACKENDS = {
    "auth": "http://auth-service:5001/health",
    "user": "http://user-service:5002/health",
    "product": "http://product-service:5003/health",
    "order": "http://order-service:5004/health"
}

@app.route("/api/<service>")
def proxy(service):
    try:
        r = requests.get(BACKENDS[service])
        return jsonify(r.json())
    except:
        return jsonify({"error": "unavailable"}), 503

@app.route("/")
def index():
    return send_file("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)