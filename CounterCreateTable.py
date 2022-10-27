import boto3

dynamodb = boto3.resource('dynamodb')


table = dynamodb.create_table(
    TableName='ResumeVisitorCounter',
    KeySchema=[
        {
            'AttributeName': 'id',
            'KeyType': 'HASH'  # Partition key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'id',
            'AttributeType': 'N'
        }
        
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
)

print('Table status:', table.table_status)

print('Waiting for', table.name, 'to complete creating...')
table.meta.client.get_waiter('table_exists').wait(TableName='ResumeVisitorCounter')
print('Table status:', dynamodb.Table('ResumeVisitorCounter').table_status)
