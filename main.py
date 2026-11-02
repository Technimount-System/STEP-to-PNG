import os
import sys
import subprocess
from pathlib import Path

# Install requirements if requirements.txt exists
requirements = Path(__file__).parent / "requirements.txt"
if requirements.exists():
    subprocess.check_call([
        sys.executable,
        "-m",
        "pip",
        "install",
        "-r",
        str(requirements)
    ])

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
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)