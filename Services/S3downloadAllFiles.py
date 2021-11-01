import boto3
from botocore.exceptions import ClientError
import os

def run():
    try:
        cwd = os.getcwd()
        cwd = cwd + "/download/"
        bucket_name=input("Please enter name of your bucket: ")
        client = boto3.client('s3')

        objects = client.list_objects(Bucket=bucket_name)["Contents"]
        for object in objects:
            client.download_file(Bucket=bucket_name , Key=object["Key"] , Filename= object["Key"])
    except ClientError as e:
        print(e)