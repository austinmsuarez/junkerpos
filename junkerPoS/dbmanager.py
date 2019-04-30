import azure.cosmos.documents as documents
import azure.cosmos.cosmos_client as cosmos_client
import azure.cosmos.errors as errors



HOST = cfg.settings['host']
MASTER_KEY = cfg.settings['master_key']
DATABASE_ID = cfg.settings['database_id']
class dbmanager(object):
    """description of class"""
    table_service = TableService(connection_string='DefaultEndpointsProtocol=https;AccountName=myaccount;AccountKey=mykey;TableEndpoint=myendpoint;')
    table_service.create_table('employees')
    employee = {'PartitionKey': 'California', 'RowKey': 123, 'EmployeeName': 'bob', 'EmployeePassword': '1234','Role': 'Sales Associate'}  
    table_service.insert_entity('employees',employee)