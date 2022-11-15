import boto3

#I was using client instead of resource and kept receiving errors!
dynamodb = boto3.resource('dynamodb') 

NFL_Teams = [
    {'Cities': 'Philadelphia', 'Team-Name': 'Eagles'},
    {'Cities': 'Kansas City', 'Team-Name': 'Chiefs'},
    {'Cities': 'Minnesota', 'Team-Name': 'Vikings'},
    {'Cities': 'Miami', 'Team-Name': 'Dolphins'},
    {'Cities': 'Buffalo', 'Team-Name': 'Bills'},
    {'Cities': 'Baltimore', 'Team-Name': 'Ravens'},
    {'Cities': 'San Francisco', 'Team-Name': '49ers'},
    {'Cities': 'Dallas', 'Team-Name': 'Cowboys'},
    {'Cities': 'Tennessee', 'Team-Name': 'Titans'},
    {'Cities': 'New York', 'Team-Name': 'Jets'},
    ]

#Using resource instead of client allows us to create a variable for our table  
table = dynamodb.Table("NFL-2022")
    
#Using the list above to iterate through and add items to the DynamoDB table
with table.batch_writer() as batch:
    for Team in NFL_Teams:
        batch.put_item(Item=Team)


