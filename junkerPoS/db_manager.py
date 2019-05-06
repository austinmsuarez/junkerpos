import logging
import config_cosmos
import azure.cosmos.documents as documents
import azure.cosmos.cosmos_client as cosmos_client
import azure.cosmos.errors as errors
import pydocumentdb.document_client as document_client
from werkzeug.security import generate_password_hash, check_password_hash



def refresh():
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
        {  "id": "1234",
           "employeeName": "John Snow",
           "username": "kingofthenorth",
           "password": "pbkdf2:sha256:50000$MeT7QKTp$6f5827542861370090c30f40a461ed9a9ec9da6b8ec6facf205875ec003c5204"
        })

def validate_user(username, password):
    client = document_client.DocumentClient(config_cosmos.COSMOSDB_HOST, {'masterKey': config_cosmos.COSMOSDB_KEY})
    # gets user database
    try:       
        db_query = "select * from r where r.id = '{0}'".format(config_cosmos.COSMOSDB_DATABASE)
        db = list(client.QueryDatabases(db_query))[0]
        db_link = db['_self']

        coll_query = "select * from r where r.id = '{0}'".format(config_cosmos.COSMOSDB_COLLECTION)
        coll = list(client.QueryCollections(db_link, coll_query))[0]
        coll_link = coll['_self']

        query = "select * from r where r.username = '{0}'".format(username)
        docs = list(client.QueryDocuments(coll_link ,query))[0]
        docs_link = docs['_self']

        d = client.ReadDocument(docs_link)
        if check_password_hash(d['password'], password):
            print("valid")
        print(d)
        print("hello")
    except:
        pass

def addUser():
    pass

