import boto3
import os

aws_access_key_id = os.environ['AWS_KEY']
aws_secret_access_key = os.environ['AWS_SECRET']
region = "us-east-2"


# Get the service resource
sqs = boto3.resource('sqs', region_name=region, aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

# Get the queue
queue = sqs.get_queue_by_name(QueueName='clase-4')

while True:
    # Process messages by printing out body
    for message in queue.receive_messages():
        print(message.body)
        # Let the queue know that the message is processed
        message.delete()  ## ack acknoledge

