import json
import boto3
import decimal
client = boto3.client('dynamodb')

def lambda_handler(event, context):
  dynamodb = boto3.resource('dynamodb')

  table = dynamodb.Table('ResumeVisitorCounter')

  id=1

  response = table.update_item(
    Key={
        'id': id
    },
    UpdateExpression="set visitorcount = visitorcount + :val",
    ExpressionAttributeValues={
        ':val': decimal.Decimal(1)
    },
    ReturnValues="UPDATED_NEW"
  )
  
  
  return response