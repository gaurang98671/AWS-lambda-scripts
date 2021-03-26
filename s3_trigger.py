import json
import boto3
from uuid import uuid4


def lambda_handler(event, context):
    # TODO implement
    print("501852-Gaurang Pawar")
    # bucket_name, object key, size, event name, event_time
    record = event["Records"][0]

    # fetching details
    bucket_name = record['s3']['bucket']['name']
    object_key = record['s3']['object']['key']
    size = record['s3']['object']['size']
    event_name = record['eventName']
    event_time = record['eventTime']

    # inserting into dynamo db
    db_table = boto3.resource('dynamodb').Table('metadata')
    db_table.put_item(
        Item={
            'id': str(uuid4()),
            'bucket_name': bucket_name,
            'object_key': object_key,
            'size': size,
            'event_name': event_name,
            'eventTime': event_time
        })

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
