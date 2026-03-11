from flask import Flask, render_template
import requests

app = Flask(__name__)

urls = "https://iot-madv-2026-default-rtdb.firebaseio.com/.json"
@app.route("/")
def index():
    response = requests.get(urls)
    data = response.json()
    return render_template("index.html", datos = data)

if __name__ == "__main__":
    app.run(debug=True)