"""
The flask application package.
"""
import logging
import config_cosmos
import azure.cosmos.documents as documents
import azure.cosmos.cosmos_client as cosmos_client
import azure.cosmos.errors as errors
import pydocumentdb.document_client as document_client

from flask import Flask

app = Flask(__name__)
import junkerPoS.views

app.config.from_pyfile('config_cosmos.py')
logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

client = document_client.DocumentClient(config_cosmos.COSMOSDB_HOST, {'masterKey': config_cosmos.COSMOSDB_KEY})

# Attempt to delete the database.  This allows this to be used to recreate as well as create
try:
    db = next((data for data in client.ReadDatabases() if data['id'] == config_cosmos.COSMOSDB_DATABASE))
    client.DeleteDatabase(db['_self'])
except:
    pass

# Create database
db = client.CreateDatabase({ 'id': config_cosmos.COSMOSDB_DATABASE })

# Create collection
collection = client.CreateCollection(db['_self'],{ 'id': config_cosmos.COSMOSDB_COLLECTION })

# Create document
document = client.CreateDocument(collection['_self'],
    { 'id': config_cosmos.COSMOSDB_DOCUMENT,
        'Web Site': 0,
        'Cloud Service': 0,
        'Virtual Machine': 0,
        'name': config_cosmos.COSMOSDB_DOCUMENT 
    })
