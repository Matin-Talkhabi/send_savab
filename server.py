# server.py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running!"  # این همون چیزی هست که UptimeRobot می‌بینه

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
