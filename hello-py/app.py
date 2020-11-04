import os
import json

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return {"status": "OK"}

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='80', debug=True)
