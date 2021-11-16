import time
from datetime import datetime
from pprint import pprint

from airflow import DAG
from airflow.operators.python import PythonOperator, PythonVirtualenvOperator

with DAG(
    dag_id='hello_world',
    schedule_interval=None,
    start_date=datetime(2021, 11, 15),
    catchup=False,
    tags=['example'],
) as dag:

    def print_hello():
        return 'Hello world'

    run_this = PythonOperator(
        task_id='print_hello',
        python_callable=print_hello,
    )

    def print_excl():
        return '!'

    for i in range(5):
        task = PythonOperator(
            task_id='print_excl' + str(i),
            python_callable=print_excl,
        )

        run_this >> task
