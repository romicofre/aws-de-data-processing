# To upload files when triggered event in s3
'''
Requirements:
psycopg2

'''
import os # librería para leer variables del s.o.
import psycopg2 # para conectarse a la bd de redshift

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


''' Use env vars '''
config = {"dbname":os.environ['AWS_RS_DB_NAME'], 
          "host": os.environ['AWS_RS_DB_HOST'],
          "port": os.environ['AWS_RS_DB_PORT'], 
          "user": os.environ['AWS_RS_DB_USER'],
          "password":os.environ['AWS_RS_DB_PASS']}

bucket = os.environ['AWS_RS_BUCKET_NAME']
file = os.environ['AWS_RS_OBJECT_KEY']
key = os.environ['AWS_ACCES_KEY_ID']
secret = os.environ['AWS_SECRET_ACCES_KEY']


query = """
copy dip_de_usach.movies
from 's3://{}/{}'
access_key_id '{}'
secret_access_key '{}'
csv
IGNOREHEADER 1 
delimiter ','
TRUNCATECOLUMNS;
""".format(bucket, file, key, secret)

''' '''
# Crea conexion
conn = create_conn(**config)
cur = conn.cursor();

# Begin your transaction
cur.execute("begin;")

cur.execute(query_string)
# Commit your transaction
cur.execute("commit;")
print("Copy executed fine!")

conn.close() # !
