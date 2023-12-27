"""
This module defines a Flask Blueprint for handling routes related to the index and CV pages.

Author: Your Name
"""

from flask import Blueprint, render_template
from database import insert_data_and_get_variables

# Create a Blueprint named 'index'
index_bp = Blueprint('index', __name__)

@index_bp.route("/")
def index():
    """
    Render the index page with CV data.

    Returns:
    flask.Response: The rendered HTML template.
    """
    cv_data = insert_data_and_get_variables()
    return render_template("index2.html", cv_data=cv_data)

@index_bp.route("/cv")
def cv():
    """
    Render the CV page with CV data.

    Returns:
    flask.Response: The rendered HTML template.
    """
    cv_data = insert_data_and_get_variables()
    return render_template("cv.html", cv_data=cv_data)
