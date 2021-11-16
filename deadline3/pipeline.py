import time
from datetime import datetime
from pprint import pprint
import re
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator, PythonVirtualenvOperator

with DAG(
    dag_id='hello_world',
    schedule_interval=None,
    start_date=datetime(2021, 11, 15),
    catchup=False,
    tags=['example'],
) as dag:

    def evaluate():
        return "OK" if float(
            re.findall(r'(\d+\.\d+)%', open("/Users/kit/SRR15859207_flagstat.txt", "r").read())[0]) > 90 else "not OK"


    indexing = BashOperator(task_id="indexing",
                                     bash_command="minimap2 -d /Users/kit/ref.mmi /Users/kit/ref.fna ")

    aln = BashOperator(task_id="alignment",
                       bash_command="minimap2 -a /Users/kit/ref.mmi /Users/kit/SRR15859207.fastq > /Users/kit/SRR15859207.sam ")

    flagstat = BashOperator(task_id="flagstat",
                            bash_command="samtools flagstat /Users/kit/SRR15859207.sam > /Users/kit/SRR15859207_flagstat.txt ")

    evaluation = PythonOperator(task_id="evaluation",
                                python_callable=evaluate)

    indexing >> aln >> flagstat >> evaluation

