from flask import Flask, request
import requests


app = Flask(__name__)


@app.route("/")
def index():
    url = request.args.get("url")
    response = requests.get(url)
    return response.text


if __name__ == "__main__":
    app.run(host='192.168.1.116', port=8000)
