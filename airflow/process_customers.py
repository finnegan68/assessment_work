from airflow import DAG
from airflow.providers.amazon.aws.operators.glue import AwsGlueJobOperator
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'retries': 1,
}

with DAG(
    dag_id='customers_etl_pipeline',
    description='ETL pipeline for customers: raw → bronze → silver',
    default_args=default_args,
    start_date=datetime(2025, 6, 18),
    schedule_interval=None,  
    catchup=False,
) as dag:

    raw_to_bronze = AwsGlueJobOperator(
        task_id='customers_raw_to_bronze',
        job_name='customers raw-bronze',      
        aws_conn_id='aws_default',        
        region_name='eu-north-1',       
        wait_for_completion=True,
        verbose=True,
    )

    bronze_to_silver = AwsGlueJobOperator(
        task_id='customers_bronze_to_silver',
        job_name='customers bronze-silver',   
        aws_conn_id='aws_default',
        region_name='eu-central-1',
        wait_for_completion=True,
        verbose=True,
    )

    raw_to_bronze >> bronze_to_silver
