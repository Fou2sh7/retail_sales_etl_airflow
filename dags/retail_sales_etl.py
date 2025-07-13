from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import logging
from etl import extract_and_transform, load_to_sqlite

def etl_main():
    logging.basicConfig(level=logging.INFO)
    logging.info("Starting ETL process...")
    
    customer_df, product_df, date_df, sales_df = extract_and_transform('retail_sales_dataset.csv')
    load_to_sqlite(customer_df, product_df, date_df, sales_df)

    logging.info("ETL process finished.")

default_args = {
    'start_date': datetime(2025, 7, 12),
    'catchup': False
}

with DAG(
    dag_id="retail_sales_etl",
    default_args=default_args,
    schedule_interval="@daily",
    description="Retail Sales ETL DAG",
    tags=["etl", "retail"]
) as dag:

    etl_task = PythonOperator(
        task_id="run_etl_pipeline",
        python_callable=etl_main
    )
