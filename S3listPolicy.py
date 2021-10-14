import boto3
import json
def run():  
    bucket_name = input("Enter your buckets name: ")

    client = boto3.client('s3')
    policy = client.get_bucket_policy(Bucket=bucket_name)["Policy"]
    policy = json.dumps(policy)
    print(policy)