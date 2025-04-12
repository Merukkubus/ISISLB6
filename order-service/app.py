from flask import Flask, jsonify

app = Flask(__name__)
CORS(app)

@app.route("/health")
def health():
    return jsonify({"service": "order", "status": "ok"})

@app.route("/orders")
def orders():
    return jsonify([
        {"id": 1, "product": "Laptop", "user": "john_doe"},
        {"id": 2, "product": "Phone", "user": "jane_smith"}
    ])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5004)