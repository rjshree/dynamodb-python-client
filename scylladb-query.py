import boto3
from boto3.dynamodb.conditions import Key
scylla_host = 'http://eai-lf-scylladb.local-learning:8000'
dynamodb_client = boto3.client('dynamodb', region_name='None',endpoint_url=scylla_host)
dynamodb = boto3.resource('dynamodb', endpoint_url=scylla_host, region_name='None', aws_access_key_id='None', aws_secret_access_key='None')
def records():
    table = dynamodb.Table("dev-eai-EAICatalogTable")
    response=table.query(KeyConditionExpression=Key('objectId').eq('4c8bd55135bc43f3995dedb8123fd410') & Key('annotationIdVersion').eq('v0_89c9d62b-a6b9-11ed-863d-abcb76349dca'))
    print(response)
    
    
records()
