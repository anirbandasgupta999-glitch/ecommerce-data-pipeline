from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import os

def run_etl():
    print("Running ETL process...")
    os.system("python etl/transform.py")

default_args = {
    'owner': 'anirban',
    'retries': 2,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
    dag_id='ecommerce_pipeline',
    default_args=default_args,
    description='E-commerce ETL Pipeline',
    schedule_interval='@daily',
    start_date=datetime(2025, 1, 1),
    catchup=False
) as dag:

    etl_task = PythonOperator(
        task_id='run_etl',
        python_callable=run_etl
    )

    etl_task
