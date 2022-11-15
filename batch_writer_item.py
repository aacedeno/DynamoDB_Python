import boto3

dynamodb = boto3.client('dynamodb')

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
    
    #Using the list above to iterate through and add items to the DynamoDB table
    with table.batch_writer() as batch:
        for Team in NFL_Teams:
            batch.put_item(Item={'Cities'})


