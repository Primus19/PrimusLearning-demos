import botocore
import json

BUCKET_NAME = 'primuslearningkdemobucket' # replace with your bucket name
KEY = 'students-list-2020-09-14-edited.csv' # replace with your object key

s3 = boto3.resource('s3')

try:
    s3.Bucket(BUCKET_NAME).download_file(KEY, 'downloaded_from_s3.csv') #replace with your object name
except botocore.exceptions.ClientError as e:
    if e.response['Error']['Code'] == "404":
        print("The object does not exist.")
    else:
        raise