import boto3

scylla_host = 'http://scylladb.test:8000'
dynamodb_client = boto3.client('dynamodb', region_name='None',endpoint_url=scylla_host)
dynamodb = boto3.resource('dynamodb', endpoint_url=scylla_host,
                          region_name='None', aws_access_key_id='None', aws_secret_access_key='None')

def records():
    table = dynamodb.Table('dev-table')
    response = table.scan()
    data = response['Items']
    for temp in data:
        if temp['recordType'] == 'image' and temp['batchId'] == 'a32e6ab4-ac39-47a5-baec-049b94595dd3':
            print(temp['objectState'],temp['batchId'],temp['key'])
