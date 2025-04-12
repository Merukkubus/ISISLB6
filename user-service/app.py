from flask import Flask, jsonify

app = Flask(__name__)
CORS(app)

@app.route("/health")
def health():
    return jsonify({"service": "user", "status": "ok"})

@app.route("/profile")
def profile():
    return jsonify({
        "username": "john_doe",
        "email": "john@example.com"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)