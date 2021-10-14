import boto3
client = boto3.client('s3')

def run():
    bucket_name = input("Please enter name of your bucket: ")
    response = client.delete_bucket_policy(Bucket=bucket_name)
    print(response)