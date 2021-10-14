import boto3
def run():
    aws_resource=boto3.resource('s3')
    name_of_bucket=input("Please enter name of your bucket: ")
    bucket = aws_resource.Bucket(name_of_bucket)
    response = bucket.create(
        ACL='public-read',
        CreateBucketConfiguration= {
        'LocationConstraint':'eu-central-1'
        },
    )
    print(response)





