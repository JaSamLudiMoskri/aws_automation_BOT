import boto3
def run():
    def counter():
        n = 0
        while True:
            n += 1
            yield n

    m = counter()
        
    client = boto3.client('s3')
    for bucket in client.list_buckets()["Buckets"]:
        print(next(m),'.', bucket["Name"])
        print(bucket["CreationDate"] , '\n')

    
    
    
    
    
