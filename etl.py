import pandas as pd
import sqlite3

df = pd.read_csv('retail_sales_dataset.csv')
print(df.head())
print(df.info())
print(df.describe())
# Check for missing values
print(df.isnull().sum())
# Check for duplicates
print(df.duplicated().sum())
# Convert 'date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'])
# make product_id as unique
df['product_id'] = df['Product Category'].astype('category').cat.codes
#  make customer_id as unique
df['customer_id'] = df['Customer ID'].astype('category').cat.codes

# prepare data to the datawarehouse
customer_df = df[['customer_id', 'Gender', 'Age']].drop_duplicates()
product_df = df[['product_id', 'Product Category']].drop_duplicates()
date_df = df[['Date']].drop_duplicates()
date_df['month'] = date_df['Date'].dt.month
date_df['year'] = date_df['Date'].dt.year
sales_df = df[['Transaction ID', 'product_id', 'Date', 'Total Amount', 'customer_id']]

print(customer_df.head())
print(product_df.head())
print(date_df.head())
print(sales_df.head())

###########################################################################################
# make the datawarehouse star schema and load the data into sqlite

conn = sqlite3.connect('warehouse.db')
cursor = conn.cursor()
cursor.executescript('''
               CREATE TABLE IF NOT EXISTS fact_sales (
                   transaction_id INTEGER PRIMARY KEY,
                   date DATE,
                   total_amount FLOAT,
                   product_id INTEGER,
                   customer_id INTEGER
                   );
                CREATE TABLE IF NOT EXISTS dim_customer (
                    customer_id INTEGER PRIMARY KEY,
                    gender TEXT,
                    age INTEGER
                    );
                CREATE TABLE IF NOT EXISTS dim_product (
                    product_id INTEGER PRIMARY KEY,
                    category VARCHAR
                    );
                CREATE TABLE IF NOT EXISTS dim_date (
                    date DATE PRIMARY KEY,
                    month INTEGER,
                    year INTEGER
                    );
                ''')

customer_df.to_sql('dim_customer', conn, if_exists='append', index=False)
product_df.to_sql('dim_product', conn, if_exists='append', index=False)
date_df.to_sql('dim_date', conn, if_exists='append', index=False)
sales_df.to_sql('fact_sales', conn, if_exists='append', index=False)
conn.commit()
conn.close()

# some visualizations
import seaborn as sns
import matplotlib.pyplot as plt
plt.figure(figsize=(10, 6))  # حجم أكبر
sns.lineplot(data=df, x="Date", y="Total Amount", hue="Product Category")
plt.title("Sales Trends by Product Category")
plt.xlabel("Date")
plt.ylabel("Total Amount")
plt.savefig("sales_trend.png")
plt.show()