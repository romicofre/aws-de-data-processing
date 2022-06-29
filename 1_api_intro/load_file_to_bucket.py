import boto3
from botocore.exceptions import ClientError
import os


def upload_file(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket
    :param file_name: Local file to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
        print("Upload OK")
    except ClientError as e:
        print(e)
        return False
    return True


# one way
s3 = boto3.client('s3')
with open("test.txt", "rb") as f:
    # f can be object only
    s3.upload_fileobj(f, "dip-de-2022", "test.txt")
    
# other way
upload_file("test.txt", "dip-de-2022")
