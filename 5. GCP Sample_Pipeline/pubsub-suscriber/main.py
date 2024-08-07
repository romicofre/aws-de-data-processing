from concurrent.futures import TimeoutError
from google.cloud import pubsub_v1
import os
import time
import sys

project_id = "nombre-projecto"
subscription_id = "TEST_GKE"
# Number of seconds the subscriber should listen for messages
timeout = int(os.environ["TIMEOUT"])

subscriber = pubsub_v1.SubscriberClient()
# The `subscription_path` method creates a fully qualified identifier
# in the form `projects/{project_id}/subscriptions/{subscription_id}`
subscription_path = subscriber.subscription_path(project_id, subscription_id)

def callback(message: pubsub_v1.subscriber.message.Message) -> None:
    print(f"Received {message}.")
    message.ack()
    sys.stdout.flush()

streaming_pull_future = subscriber.subscribe(subscription_path, callback=callback)
print(f"Listening for messages on {subscription_path}..\n")

with subscriber:
    try:
        # El bucle se ejecutará indefinidamente hasta que se produzca una excepción
        while True:
            time.sleep(1)
    except Exception as e:
        print(f"An error occurred: {e}")