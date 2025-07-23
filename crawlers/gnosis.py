import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import requests
from bs4 import BeautifulSoup
from utils.s3_uploader import upload_to_s3
from dotenv import load_dotenv

load_dotenv()  # Load your .env credentials

def crawl_gnosis():
    url = "https://www.gnosisfreight.com"
    headers = {"User-Agent": "Mozilla/5.0"}
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")
    
    return {
        "url": url,
        "title": soup.title.string if soup.title else "",
        "text": soup.get_text()
    }

if __name__ == "__main__":
    data = crawl_gnosis()

    print("Title:", data["title"])
    print("Sample text:", data["text"][:500])

    # S3 Setup
    AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY_ID")
    AWS_SECRET_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
    BUCKET_NAME = "kashish-crawler-data"  # Replace with your actual bucket

    if AWS_ACCESS_KEY and AWS_SECRET_KEY:
        import boto3

        session = boto3.Session(
            aws_access_key_id=AWS_ACCESS_KEY,
            aws_secret_access_key=AWS_SECRET_KEY
        )

        s3 = session.client("s3")

        upload_to_s3(
            data=data,
            bucket=BUCKET_NAME,
            prefix="raw/gnosis",
            filename="gnosis_crawl.json"
        )
    else:
        print("❌ AWS credentials not found. Skipping upload.")
