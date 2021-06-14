import json
import urllib.parse
import boto3
import psycopg2
import os


print('Loading function')


s3 = boto3.client('s3')


def create_conn(**kwargs):
  config = kwargs
  try:
      conn=psycopg2.connect(dbname = config['dbname'],
                            host = config['host'],
                            port = config['port'],
                            user = config['user'],
                            password = config['password'])
  except Exception as err:
      print(err.code, err)
  return conn


def lambda_handler(event, context):
    # print("Received event: " + json.dumps(event, indent=2))

    # Get the object from the event and show its content type
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')

    config = {
        "dbname":os.environ['AWS_RS_DB_NAME'],
        "host": os.environ['AWS_RS_DB_HOST'],
        "port": os.environ['AWS_RS_DB_PORT'],
        "user": os.environ['AWS_RS_DB_USER'],
        "password":os.environ['AWS_RS_DB_PASS']
    }

    aws_key = os.environ['AWS_ACCES_KEY_ID']
    aws_secret = os.environ['AWS_SECRET_ACCES_KEY']

    query = """
        copy dip_de_usach.movies
        from 's3://{}/{}'
        access_key_id '{}'
        secret_access_key '{}'
        csv
        IGNOREHEADER 1
        delimiter ','
        TRUNCATECOLUMNS;
    """.format(bucket, key, aws_key, aws_secret)

    try:
        conn = create_conn(**config)
        cur = conn.cursor();

        # Begin your transaction
        cur.execute("begin;")

        cur.execute(query)
        # Commit your transaction
        cur.execute("commit;")
        print("Copy executed fine!")

        response = s3.get_object(Bucket=bucket, Key=key)
        print("CONTENT TYPE: " + response['ContentType'])
        return response['ContentType']
    except Exception as e:
        # COPY FILE TO error/ folder
        print(e)
        print('Error in process with file {} from bucket: {}'.format(key, bucket))
        raise e
