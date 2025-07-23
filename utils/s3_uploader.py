import boto3
import json
from datetime import datetime

def upload_to_s3(data: dict, bucket: str, prefix: str, filename: str):
    s3 = boto3.client("s3")
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    key = f"{prefix}/{timestamp}/{filename}"

    try:
        s3.put_object(
            Bucket=bucket,
            Key=key,
            Body=json.dumps(data),
            ContentType="application/json"
        )
        print(f"✅ Uploaded to s3://{bucket}/{key}")
    except Exception as e:
        print(f"❌ S3 upload failed: {e}")
