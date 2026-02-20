from flask import Flask, render_template,jsonify
import requests

app = Flask(__name__)

URLS = "https://iot-madv-2026-default-rtdb.firebaseio.com/sensores.json"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/sensores")
def api_sensor():
    response = requests.get(URLS)
    data = response.json()
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug = True)