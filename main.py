from flask import Flask
from api import register_blueprints


app = Flask(__name__)

register_blueprints(app)

if __name__ == "__main__":
    port = 5000


    app.run(debug=True, port=port)