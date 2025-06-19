from airflow import DAG
from airflow.providers.amazon.aws.operators.glue import AwsGlueJobOperator
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'retries': 1,
}

with DAG(
    dag_id='enrich_user_profiles_etl_pipeline',
    description='ETL pipeline for enriching customers with user_profiles',
    default_args=default_args,
    start_date=datetime(2025, 6, 18),
    schedule_interval=None,  
    catchup=False,
) as dag:

    enrich = AwsGlueJobOperator(
        task_id='enrich_customers',
        job_name='customers silver-gold',      
        aws_conn_id='aws_default',        
        region_name='eu-north-1',       
        wait_for_completion=True,
        verbose=True,
    )

    enrich 
