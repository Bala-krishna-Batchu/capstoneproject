import json
import json
import boto3
import csv
import io
import pandas as pd
from datetime import datetime,timedelta
import requests

def lambda_handler(event, context):
    bucket='openaq-api-data'
    #url = 'https://api.openaq.org/v2/measurements?country=US&date_from=2022-09-01&date_to=2023-10-01'
    r1=requests.get("https://api.openaq.org/v2/measurements?country=US&date_from=2022-09-01&date_to=2023-10-01&limit=3500")
    r1.json()
    r1.json()['results']
    final=pd.DataFrame(r1.json()['results'])
    s3_client=boto3.client('s3',region_name='us-east-1')
    s3 = boto3.resource(
    's3',
    region_name='us-east-1',
    aws_access_key_id=AKIAW5UG2YBFJU2MC2YR,
    aws_secret_access_key=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
)
#content="String content to write to a new S3 file"
#client = boto3.client('s3')
s3.Object('s3://aws-openaq-airquality-county/temp/', 'openaqapi.json').put(Body=final)

#s3_client.put_object(Body=data,Bucket='open-api-data',Key='openaqapi1.csv')
#s3 = boto3.resource('s3')
#s3.meta.client.upload_file('source_file_name.html', 'my.bucket.com', 'aws_file_name.html', ExtraArgs={'ContentType': "application/json", 'ACL': "public-read"} )
#transfer.upload_file(file, bucket.name, key)
#s3 = boto3.client('s3', aws_access_key_id = AWS_ACCESS_KEY_ID, aws_secret_access_key = AWS_SECRET_ACCESS_KEY, region_name = "us-east-1")
    
#s3.upload_file(file_path, s3_bucket, file_name, ExtraArgs={'ContentType': "application/json"})

#client = boto3.client('s3')
client.put_object(Body=more_binary_data, Bucket='my_bucket_name', Key='my/key/including/anotherfilename.txt')
  return data

#print(data)
#from botocore.vendored import requests
s3=boto3.client('s3')
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
