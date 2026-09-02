import os
from flask import Flask
from flask_cors import CORS

from .movies_api import movies_api

app = Flask(__name__)

# Apply CORS globally across all routes and origins
CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)

app.register_blueprint(movies_api)

# Start app
if __name__ == "__main__":
    app.run(
        debug=True,
        host="0.0.0.0",
        port=int(os.getenv("FLASK_RUN_PORT", 5000)),
    )
