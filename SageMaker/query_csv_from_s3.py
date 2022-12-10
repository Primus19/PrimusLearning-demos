import boto3

BUCKET_NAME = 'primuslearningkdemobucket' # replace with your bucket name
KEY = 'transactions_history_2022-02-15T17_12_12.875Z.csv'

s3 = boto3.client('s3')
r = s3.select_object_content(
    Bucket=BUCKET_NAME,
    Key=KEY,
    ExpressionType='SQL',
    Expression="Select * from s3Object s limit 5 ",
    InputSerialization={'CSV': {"FileHeaderInfo": "Use"}},
    OutputSerialization={'CSV':{}}
)

for event in r['Payload']:
    if 'Records' in event:
        records = event['Records']['Payload'].decode('utf-8')
        print(records)