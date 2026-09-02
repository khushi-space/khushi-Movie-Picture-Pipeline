import os
import sys
from flask import Flask
from flask_cors import CORS
from movies.movies_api import movies_api

# Add current directory to sys.path for resolution during direct execution
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

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
