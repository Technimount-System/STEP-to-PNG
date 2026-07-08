from flask import Flask
from api import register_blueprints
from pyngrok import ngrok
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
register_blueprints(app)

if __name__ == "__main__":
    port = 5000
    public_url = ngrok.connect(port).public_url
    print(f" * ngrok tunnel: {public_url} -> http://127.0.0.1:{port}")
    app.run(port=port)