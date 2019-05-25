import logging
#import config_cosmos
import azure.cosmos.documents as documents
import azure.cosmos.cosmos_client as cosmos_client
import azure.cosmos.errors as errors
import pydocumentdb.document_client as document_client
from werkzeug.security import generate_password_hash, check_password_hash 

def refresh():
    pass

def validate_user(username, password):
    client = document_client.DocumentClient(config_cosmos.COSMOSDB_HOST, {'masterKey': config_cosmos.COSMOSDB_KEY})
    # gets user database
    try:       
        db_link = get_db(client)
        col_link = get_collection(db_link,client)
        query = "select * from r where r.username = '{0}'".format(username)
        docs = list(client.QueryDocuments(col_link ,query))[0]
        docs_link = docs['_self']
        d = client.ReadDocument(docs_link)
        if check_password_hash(d['password'], password):
            return True
        else:
            return False
    except:
        return False
        print("error in validation")

def get_db(client):
    try:       
        db_query = "select * from r where r.id = '{0}'".format(config_cosmos.COSMOSDB_DATABASE)
        db = list(client.QueryDatabases(db_query))[0]
        db_link = db['_self']
        return db_link
    except:
        print("error in database reach")

def get_collection(db_link,client):
    try:       
        col_query = "select * from r where r.id = '{0}'".format(config_cosmos.COSMOSDB_COLLECTION)
        col = list(client.QueryCollections(db_link, col_query))[0]
        col_link = col['_self']
        return col_link
    except:
        print("error in collection reach")

def get_product():

    pass