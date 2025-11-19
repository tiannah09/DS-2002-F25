import requests
import boto3


FILE_URL = "https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif" 
LOCAL_FILENAME = "lab8_demo.gif"       
BUCKET_NAME = "ds2002-f25-rmk8eg"      
S3_KEY = "lab8_demo.gif"            
EXPIRES_IN = 60                        



def download_file(url: str, local_path: str) -> None:
    """Download a file from the internet and save it locally."""
    print(f"Downloading file from {url} ...")
    resp = requests.get(url, stream=True)
    resp.raise_for_status()  # will throw if HTTP error

    with open(local_path, "wb") as f:
        for chunk in resp.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)

    print(f"Saved to {local_path}")


def upload_to_s3(local_path: str, bucket: str, key: str) -> None:
    """Upload a local file to S3."""
    print(f"Uploading {local_path} to s3://{bucket}/{key} ...")
    s3 = boto3.client("s3", region_name="us-east-1")
    s3.upload_file(Filename=local_path, Bucket=bucket, Key=key)
    print("Upload complete.")


def create_presigned_url(bucket: str, key: str, expires_in: int) -> str:
    """Generate a presigned URL for an S3 object."""
    s3 = boto3.client("s3", region_name="us-east-1")
    url = s3.generate_presigned_url(
        "get_object",
        Params={"Bucket": bucket, "Key": key},
        ExpiresIn=expires_in,
    )
    return url


def main():
    download_file(FILE_URL, LOCAL_FILENAME)
    upload_to_s3(LOCAL_FILENAME, BUCKET_NAME, S3_KEY)
    url = create_presigned_url(BUCKET_NAME, S3_KEY, EXPIRES_IN)
    print("\nPresigned URL (valid for", EXPIRES_IN, "seconds):")
    print(url)


if __name__ == "__main__":
    main()

