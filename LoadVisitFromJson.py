import decimal
import json

import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('ResumeVisitorCounter')

with open("counter.json") as json_file:
    numVisitor = json.load(json_file, parse_float=decimal.Decimal)
    for vCount in numVisitor:
        id = int(vCount['id'])
        visitorcount=int(vCount['visitorcount'])
        print("Adding visit count:", visitorcount)

        table.put_item(
            Item={
                'id': id,
                'visitorcount': visitorcount
            }
        )
