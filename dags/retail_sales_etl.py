from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import pandas as pd
import sqlite3

def run_etl():
    df = pd.read_csv('retail_sales_dataset.csv')
    df['Date'] = pd.to_datetime(df['Date'])
    df["product_id"] = df["Product Category"].astype("category").cat.codes
    df["customer_id"] = df["Customer ID"].astype("category").cat.codes
    customer_data = df[["customer_id", "Gender", "Age"]].drop_duplicates()
    product_data = df[["product_id", "Product Category"]].drop_duplicates()
    date_data = df[["Date"]].drop_duplicates()
    date_data["month"] = date_data["Date"].dt.month
    date_data["year"] = date_data["Date"].dt.year
    sales_data = df[["Transaction ID", "Date", "Total Amount", "product_id", "customer_id"]]
    conn = sqlite3.connect("warehouse.db")
    cursor = conn.cursor()
    cursor.executescript("""
        CREATE TABLE IF NOT EXISTS fact_sales (
            transaction_id INT PRIMARY KEY,
            date DATE,
            total_amount FLOAT,
            product_id INT,
            customer_id INT
        );
        CREATE TABLE IF NOT EXISTS dim_customer (
            customer_id INT PRIMARY KEY,
            gender VARCHAR,
            age INT
        );
        CREATE TABLE IF NOT EXISTS dim_product (
            product_id INT PRIMARY KEY,
            category VARCHAR
        );
        CREATE TABLE IF NOT EXISTS dim_date (
            date DATE PRIMARY KEY,
            month INT,
            year INT
        );
    """)
    customer_data.to_sql("dim_customer", conn, if_exists="append", index=False)
    product_data.to_sql("dim_product", conn, if_exists="append", index=False)
    date_data.to_sql("dim_date", conn, if_exists="append", index=False)
    sales_data.to_sql("fact_sales", conn, if_exists="append", index=False)
    conn.commit()
    conn.close()
with DAG(
    "retail_sales_etl",
    start_date=datetime(2025, 7, 12),
    schedule_interval="@daily",
    catchup=False
) as dag:
    etl_task = PythonOperator(
        task_id="run_etl_pipeline",
        python_callable=run_etl)