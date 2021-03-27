import json
import boto3

def lambda_handler(event, context):
    # TODO implement
    s3_client= boto3.client('s3')
    response = s3_client.generate_presigned_url('get_object',
                                                    Params={'Bucket': '501852-photos',
                                                            'Key': 'itadori.jpeg'},
                                                    ExpiresIn=20)
    return response
