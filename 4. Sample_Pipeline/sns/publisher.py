import os
import time
from datetime import datetime

import boto3
import json

aws_access_key_id = os.environ['AWS_KEY']
aws_secret_access_key = os.environ['AWS_SECRET']
region = "us-east-2"
sns_topic_arn = "arn:aws:sns:us-east-2:605543152360:lambda-topic"

sns = boto3.client('sns', region_name=region, aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

while True:
    subject = str(datetime.now())
    body = "This message was sended at " + subject
    message = {"default": body}
    publication = sns.publish(TargetArn=sns_topic_arn, Message=json.dumps(message), MessageStructure='json')
    print(body)
    time.sleep(5)