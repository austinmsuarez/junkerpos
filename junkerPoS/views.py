from datetime import datetime
from flask import render_template, request, session, abort
import db_manager
from junkerPoS import app


@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        year=datetime.now().year,
    )

@app.route('/login', methods=["post"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    if db_manager.validate_user(username,password):
        return render_template(
            'home.html',
            year=datetime.now().year,
            result = "valid",
        )
    else:
        return render_template(
            'index.html',
            year=datetime.now().year,
            result = "Invalid username or password",
        )

@app.route('/get_product', methods=["GET"])
def get_product():
    product_info = request.form[""]