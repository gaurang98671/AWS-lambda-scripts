from __future__ import print_function

import json

print('Loading function')


def lambda_handler(event, context):
    # print("Received event: " + json.dumps(event, indent=2))
    message = json.loads(event['Records'][0]['Sns']['Message'])
    print(message["email"])
    # Send email by SES

    return message
