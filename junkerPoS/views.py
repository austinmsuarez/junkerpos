from datetime import datetime
from flask import render_template, request, session, abort
from junkerPoS import app

import pydocumentdb.document_client as document_client

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
    print("hello")

    username = request.form["username"]
    password = request.form["password"]
    print("username " + username)
    print("password " + password)


    return render_template(
        'index.html',
        year=datetime.now().year,
        result = "valid",
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )
