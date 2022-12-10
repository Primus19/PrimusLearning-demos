import boto3
import pandas as pd
import json
from io import StringIO

s3 = boto3.client('s3')
content = "{'name': 'JaneDoe', 'ID': '5'}"
s3.put_object(Bucket="primuslearningkdemobucket", Key = "outputfile_to_s3.csv", Body=str(content))

print("Check S3 Bucket")