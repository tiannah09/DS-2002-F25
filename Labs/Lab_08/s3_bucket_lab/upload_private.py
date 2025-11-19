import boto3

# Create S3 client
s3 = boto3.client("s3", region_name="us-east-1")

bucket = "ds2002-f25-rmk8eg"
local_file = "vuelta.jpg"
s3_key = "vuelta_private.jpg"  # name/path in S3

with open(local_file, "rb") as data:
    s3.put_object(
        Bucket=bucket,
        Key=s3_key,
        Body=data
    )

print("Uploaded privately:", s3_key)
