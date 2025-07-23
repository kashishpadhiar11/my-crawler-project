from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from crawlers.gnosis import crawl_gnosis
from utils.s3_uploader import upload_to_s3
from dotenv import load_dotenv

load_dotenv()

def run_gnosis_task():
    data = crawl_gnosis()
    upload_to_s3(
        data=data,
        bucket="kashish-crawler-data",
        prefix="raw/gnosis",
        filename="gnosis_crawl_from_airflow.json"
    )

default_args = {
    "start_date": datetime(2024, 1, 1),
    "catchup": False,
}

with DAG(
    dag_id="gnosis_crawl_dag",
    schedule_interval="@daily",
    default_args=default_args,
    tags=["gnosis", "web-crawl"],
) as dag:

    crawl = PythonOperator(
        task_id="crawl_and_upload_gnosis",
        python_callable=run_gnosis_task
    )
