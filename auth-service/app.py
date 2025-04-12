from flask import Flask, jsonify

app = Flask(__name__)
CORS(app)

@app.route("/health")
def health():
    return jsonify({"service": "auth", "status": "ok"})

@app.route("/login")
def login():
    return jsonify({"message": "Login success"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)