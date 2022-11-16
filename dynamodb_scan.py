import boto3
import json

dynamodb = boto3.client('dynamodb')

response = dynamodb.scan(
    TableName='NFL-2022'
)
    
 #This for loop will parse the scan items in dynamodb tabe and output it into json format   
for i in response['Items']:
    print(json.dumps(i))
    