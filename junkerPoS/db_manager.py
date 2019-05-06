import logging
import config_cosmos
import azure.cosmos.documents as documents
import azure.cosmos.cosmos_client as cosmos_client
import azure.cosmos.errors as errors
import pydocumentdb.document_client as document_client



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
           "productId": "33218897",
           "category": "Women's Outerwear",
           "manufacturer": "Contoso",
           "description": "Black wool pea-coat",
           "price": "49.99",
           "shipping": {  "weight": 2,"dimensions": {"width": 8,"height": 11,"depth": 3 }}
        })

def validate_user(username, password):
    client = document_client.DocumentClient(config_cosmos.COSMOSDB_HOST, {'masterKey': config_cosmos.COSMOSDB_KEY})
    # gets user database
    try:       
        db_id = 'employeeDB'
        db_query = "select * from r where r.id = '{0}'".format(db_id)
        db = list(client.QueryDatabases(db_query))[0]
        db_link = db['_self']

        coll_id = 'employeeCol'
        coll_query = "select * from r where r.id = '{0}'".format(coll_id)
        coll = list(client.QueryCollections(db_link, coll_query))[0]
        coll_link = coll['_self']

        docs = client.ReadDocuments(coll_link)
        print list(docs)
        print("hello")
    except:
        pass

def addUser():
    pass

