from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import sys
import os

# Adjust PYTHONPATH if needed, or place fetch_all_comments.py in your DAG folder or PYTHONPATH
sys.path.insert(0, '/path/to/your/project')  # Update this path accordingly

from fetch_all_comments import main as fetch_comments_main

default_args = {
    'owner': 'you',
    'depends_on_past': False,
    'start_date': datetime(2025, 7, 25),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    dag_id='youtube_comments_etl',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False
) as dag:

    fetch_comments = PythonOperator(
        task_id='fetch_youtube_comments',
        python_callable=fetch_comments_main
    )
