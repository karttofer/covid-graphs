import boto3
from datetime import datetime, timezone
from botocore.exceptions import ClientError
from color_logs import use__logger

current_datetime = 'app-covid-files-' + str(datetime.now(timezone.utc).date())

def create_bucket_with_files(bucket_name, client_region=None):
    try:
        if client_region is None:
            use__logger().error('WE NEED A REGION')
            return 502
        else: 
            s3_client = boto3.client('s3', region_name=client_region)
            location = {'LocationConstraint': client_region}
            s3_client.create_bucket(Bucket=bucket_name,
                                    CreateBucketConfiguration=location)
            
            use__logger().debug('BUCKET CREATED')
            return 200

    except ClientError as error:
        print('SOMETHING WRONG HAPPENS', error)
        return 500

def check_bucket_exist(bucket_name, bucket_region=None):
    s3 = boto3.client('s3')
    bucket__list = s3.list_buckets()
    buckets = bucket__list['Buckets']

    if len(buckets) == 0:
        create_bucket_with_files(bucket_name, bucket_region)
    else:
        for bucket in bucket__list['Buckets']:
            if bucket['Name'] == current_datetime:
                return 409 
            