import json
import boto3


## No olvidar dar el permiso para dynamoDB

def lambda_handler(event, context):
    # TODO implement
    client_dynamo=boto3.resource('dynamodb', region_name='us-east-1')
    table=client_dynamo.Table('dip-de-2022') # nombre tabla
    try:
        response=table.put_item(Item=event)
        return "Done"
    except:
        raise
        
