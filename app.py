"""
This script initializes a Flask web application and registers a blueprint for routing.

The Flask app includes only the main route from the 'index_bp' blueprint.

"""

from flask import Flask
from routes import index_bp  # Only import the blueprint

app = Flask(__name__)

# Register the blueprint (includes both routes)
app.register_blueprint(index_bp)

if __name__ == '__main__':
    # Run the Flask app in debug mode
    app.run(debug=True)
