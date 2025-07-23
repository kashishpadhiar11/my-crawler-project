from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

with DAG(
    dag_id="daily_gnosis_dag",
    schedule_interval="@daily",
    start_date=datetime(2023, 1, 1),
    catchup=False,
    tags=["example"],
) as dag:

    def print_hello():
        print("Hello from Gnosis DAG!")

    task1 = PythonOperator(
        task_id="print_hello_task",
        python_callable=print_hello,
    )
