"""
The flask application package.
"""
import logging
#import config_cosmos
import azure.cosmos.documents as documents
import azure.cosmos.cosmos_client as cosmos_client
import azure.cosmos.errors as errors
import pydocumentdb.document_client as document_client
import db_manager
from flask import Flask

app = Flask(__name__)
db_manager.refresh()
import junkerPoS.views

