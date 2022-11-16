import boto3

dynamodb = boto3.client('dynamodb')
    
#Creating table
table = dynamodb.create_table(
    TableName='NFL-2022',
    KeySchema=[
        {
            'AttributeName': 'Cities',
            'KeyType': 'HASH' #Hash = Parition Key
        },
        {
            'AttributeName': 'Team-Name',
            'KeyType': 'RANGE' #Range = Sort key 
        },    
            
    ],
     AttributeDefinitions=[
        {
            'AttributeName': 'Cities',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'Team-Name',
            'AttributeType': 'S'
        },
    ],
    #RCU and WCU must be specified 
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    },
)