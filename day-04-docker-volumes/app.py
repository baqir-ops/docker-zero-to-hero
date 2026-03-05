from flask import Flask
import os

app = Flask(__name__)
DATA_FILE = "/app/data/visits.txt"

@app.route("/")
def home():
    if not os.path.exists(DATA_FILE):
        count = 0
    else:
        with open(DATA_FILE, "r") as f:
            count = int(f.read())
    count += 1
    with open(DATA_FILE, "w") as f:
        f.write(str(count))
    return f"This page has been visited {count} times!"

@app.route("/health")
def health():
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
