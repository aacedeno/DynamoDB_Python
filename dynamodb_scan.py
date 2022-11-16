import boto3

dynamodb = boto3.client('dynamodb')

response = client.scan(
    TableName='NFL-2022',
    IndexName='string',
    AttributesToGet=[
        'string',
    ],
    
    
for i in response['Items']:
    