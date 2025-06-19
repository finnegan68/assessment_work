from airflow import DAG
from airflow.providers.amazon.aws.operators.glue import AwsGlueJobOperator
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'retries': 1,
}

with DAG(
    dag_id='user_profiles_etl_pipeline',
    description='ETL pipeline for user_profiles: raw → silver',
    default_args=default_args,
    start_date=datetime(2025, 6, 18),
    schedule_interval=None,  
    catchup=False,
) as dag:

    raw_to_silver = AwsGlueJobOperator(
        task_id='user_profiles_raw_to_silver',
        job_name='user_profiles raw-silver',      
        aws_conn_id='aws_default',        
        region_name='eu-north-1',       
        wait_for_completion=True,
        verbose=True,
    )

    raw_to_silver 
