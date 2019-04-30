from datetime import datetime
from flask import render_template, request, session, abort
from junkerPoS import app
import config_cosmos
import azure.cosmos.documents as documents
import azure.cosmos.cosmos_client as cosmos_client
import azure.cosmos.errors as errors


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
        'home.html',
        year=datetime.now().year,
        result = "valid",
    )