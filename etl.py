import pandas as pd
import sqlite3
import logging

def extract_and_transform(filepath: str):
    df = pd.read_csv(filepath)
    df.drop_duplicates(inplace=True)
    df['Date'] = pd.to_datetime(df['Date'])
    
    df['product_id'] = df['Product Category'].astype('category').cat.codes
    df['customer_id'] = df['Customer ID'].astype('category').cat.codes
    
    customer_df = df[['customer_id', 'Gender', 'Age']].drop_duplicates()
    product_df = df[['product_id', 'Product Category']].drop_duplicates()
    date_df = df[['Date']].drop_duplicates()
    date_df['month'] = date_df['Date'].dt.month
    date_df['year'] = date_df['Date'].dt.year
    sales_df = df[['Transaction ID', 'Date', 'Total Amount', 'product_id', 'customer_id']].drop_duplicates()

    return customer_df, product_df, date_df, sales_df

def load_to_sqlite(customer_df, product_df, date_df, sales_df, db_path='warehouse.db'):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.executescript("""
        CREATE TABLE IF NOT EXISTS dim_customer (
            customer_id INTEGER PRIMARY KEY,
            gender TEXT,
            age INTEGER
        );
        CREATE TABLE IF NOT EXISTS dim_product (
            product_id INTEGER PRIMARY KEY,
            category TEXT
        );
        CREATE TABLE IF NOT EXISTS dim_date (
            date DATE PRIMARY KEY,
            month INTEGER,
            year INTEGER
        );
        CREATE TABLE IF NOT EXISTS fact_sales (
            transaction_id INTEGER PRIMARY KEY,
            date DATE,
            total_amount FLOAT,
            product_id INTEGER,
            customer_id INTEGER
        );
    """)

    # Overwrite for simplicity in dev mode
    customer_df.to_sql("dim_customer", conn, if_exists="replace", index=False)
    product_df.to_sql("dim_product", conn, if_exists="replace", index=False)
    date_df.to_sql("dim_date", conn, if_exists="replace", index=False)
    sales_df.to_sql("fact_sales", conn, if_exists="replace", index=False)

    conn.commit()
    conn.close()
    logging.info("Data loaded successfully.")
