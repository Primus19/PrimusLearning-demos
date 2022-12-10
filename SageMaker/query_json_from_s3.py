import boto3

BUCKET_NAME = 'primuslearningkdemobucket' # replace with your bucket name
KEY = 'outputfile_lab.json'

s3 = boto3.client('s3')
r = s3.select_object_content(
    Bucket=BUCKET_NAME,
    Key=KEY,
    ExpressionType='SQL',
    Expression="Select * from s3Object s limit 5",
    InputSerialization={'JSON': {"Type":"Lines"}},
    OutputSerialization={'JSON':{}}
)

for event in r['Payload']:
    if 'Records' in event:
       records = event['Records']['Payload'].decode('utf-8')
       print(records)