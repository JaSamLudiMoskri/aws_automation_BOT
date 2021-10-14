import boto3
client = boto3.client('s3')
def run():
    filename = input("Enter full name of file that you want to upload: ")
    bucket_name = input("Please enter name of your bucket: ")
    client.upload_file(Filename=filename, Bucket = bucket_name , Key = filename)
    print(f"File {filename} successfully uploaded.")