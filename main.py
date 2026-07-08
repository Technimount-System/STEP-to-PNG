import os
from flask import Flask
from dotenv import load_dotenv
from api import register_blueprints

load_dotenv()

app = Flask(__name__)
register_blueprints(app)

@app.route("/")
def home():
    return {"status": "API is running"}


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)