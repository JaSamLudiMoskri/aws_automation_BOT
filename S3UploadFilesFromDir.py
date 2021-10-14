import boto3
import glob
def run():
    your_os = input("Please enter on waht OS you are working on. Example (Windows , Linux): ")
    if your_os == 'Windows':
        client = boto3.client('s3')
        bucket_name = input("Please enter name of your bucket.")
        file_type =input("Please enter right type of your file (example= txt , png , jpeg , pdf): ")

        if file_type == 'txt':
            full_path = input("Please enter full path to your directory.")
            files = glob.glob(full_path+"\*.txt")
            for file in files:
                client.upload_file(Filename=file , Bucket=bucket_name, Key=file.split("\\")[-1])
        elif file_type == 'png':
            full_path = input("Please enter full path to your directory.")
            files = glob.glob(full_path+"\*.png")
            for file in files:
                client.upload_file(Filename=file , Bucket=bucket_name, Key=file.split("\\")[-1])
        elif file_type == '.jpeg':
            full_path = input("Please enter full path to your directory.")
            files = glob.glob(full_path+"\*.jpeg")
            for file in files:
                client.upload_file(Filename=file , Bucket=bucket_name, Key=file.split("\\")[-1])
        elif file_type == '.pdf':
            full_path = input("Please enter full path to your directory.")
            files = glob.glob(full_path+"\*.pdf")
            for file in files:
                client.upload_file(Filename=file , Bucket=bucket_name, Key=file.split("\\")[-1])
        else:
            print("We dont support that kind of format.")
    elif your_os == 'Linux':
        client = boto3.client('s3')
        bucket_name = input("Please enter name of your bucket.")
        file_type =input("Please enter right type of your file (example= txt , png , jpeg , pdf): ")

        if file_type == 'txt':
            full_path = input("Please enter full path to your directory.")
            files = glob.glob(full_path+"/*.txt")
            for file in files:
                client.upload_file(Filename=file , Bucket=bucket_name, Key=file.split("/")[-1])
        elif file_type == 'png':
            full_path = input("Please enter full path to your directory.")
            files = glob.glob(full_path+"/*.png")
            for file in files:
                client.upload_file(Filename=file , Bucket=bucket_name, Key=file.split("/")[-1])
        elif file_type == '.jpeg':
            full_path = input("Please enter full path to your directory.")
            files = glob.glob(full_path+"/*.jpeg")
            for file in files:
                client.upload_file(Filename=file , Bucket=bucket_name, Key=file.split("/")[-1])
        elif file_type == '.pdf':
            full_path = input("Please enter full path to your directory.")
            files = glob.glob(full_path+"/*.pdf")
            for file in files:
                client.upload_file(Filename=file , Bucket=bucket_name, Key=file.split("/")[-1])
        else:
            print("We dont support that kind of format.")
    else:
        print("Please enter correct type of os")