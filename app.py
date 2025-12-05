# app.py
from flask import Flask, jsonify, make_response
from prometheus_flask_exporter import PrometheusMetrics
import time

app = Flask(__name__)
metrics = PrometheusMetrics(app)  # Initialize


@app.route("/api/users")
def get_users():
    time.sleep(0.1)  # Simulate some work
    return jsonify({"users": ["User 1", "User 2"]})


@app.route("/api/products")
def get_products():
    time.sleep(0.3)
    return make_response("Internal Server Error", 500)


@app.route("/")
def home():
    return "Hello! Go to /metrics to see the stats."


# This is needed to run with Docker
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
