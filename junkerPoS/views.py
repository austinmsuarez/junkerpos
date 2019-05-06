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

@app.route('/login', methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    db_manager.validate_user(username,password)

    return render_template(
        'home.html',
        year=datetime.now().year,
        result = "valid",
    )