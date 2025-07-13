# Retail Sales ETL Pipeline and Dashboard

## Overview
This project demonstrates a complete ETL (Extract, Transform, Load) pipeline for processing a Retail Sales dataset from Kaggle. The pipeline extracts data, transforms it into a Star Schema Data Warehouse using SQLite, and loads it for analysis. An automated workflow is implemented using Apache Airflow on Astronomer, with visualizations created using Seaborn and Power BI.

## Dataset
- **Source**: [Retail Sales Dataset](https://www.kaggle.com/datasets/mohammadtalib786/retail-sales-dataset)
- **Details**: Contains 1000+ records with columns like Transaction ID, Date, Customer ID, Gender, Age, Product Category, and Total Amount.

## Project Structure
- `etl.py`: Python script for the ETL pipeline.
- `retail_sales_etl.py`: Airflow DAG for automation.
- `warehouse.db`: SQLite Data Warehouse.
- `sales_trend.png`: Seaborn visualization of sales trends.
- `requirements.txt`: List of Python dependencies.

## Star Schema Design
- **Fact Table**: `fact_sales` (Transaction ID, Date, Total Amount, Product ID, Customer ID)
- **Dimension Tables**:
  - `dim_customer` (Customer ID, Gender, Age)
  - `dim_product` (Product ID, Product Category)
  - `dim_date` (Date, Month, Year)
- [Diagram] (Add a screenshot from draw.io if created)

## ETL Process
1. **Extract**: Read data from `retail_sales.csv` using Pandas.
2. **Transform**: Clean data (remove nulls, standardize dates) and create IDs.
3. **Load**: Store data in SQLite tables.
4. **Automate**: Schedule the pipeline with Apache Airflow on Astronomer.

## Visualizations
- **Seaborn**: `sales_trend.png` shows sales trends by product category over time.
- **Power BI**: Interactive dashboard with sales trends, customer age analysis, and product category distribution (link or screenshot to be added).

## Technologies
- **Python**: Pandas, Seaborn, Matplotlib
- **Database**: SQLite
- **Automation**: Apache Airflow (Astronomer)
- **BI**: Power BI
- **Version Control**: Git, GitHub

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone <your-repo-link># Retail Sales ETL Pipeline and Dashboard

## Overview
This project demonstrates a complete ETL (Extract, Transform, Load) pipeline for processing a Retail Sales dataset from Kaggle. The pipeline extracts data, transforms it into a Star Schema Data Warehouse using SQLite, and loads it for analysis. An automated workflow is implemented using Apache Airflow on Astronomer, with visualizations created using Seaborn and Power BI.

## Dataset
- **Source**: [Retail Sales Dataset](https://www.kaggle.com/datasets/mohammadtalib786/retail-sales-dataset)
- **Details**: Contains 1000+ records with columns like Transaction ID, Date, Customer ID, Gender, Age, Product Category, and Total Amount.

## Project Structure
- `etl.py`: Python script for the ETL pipeline.
- `retail_sales_etl.py`: Airflow DAG for automation.
- `warehouse.db`: SQLite Data Warehouse.
- `sales_trend.png`: Seaborn visualization of sales trends.
- `requirements.txt`: List of Python dependencies.

## Star Schema Design
- **Fact Table**: `fact_sales` (Transaction ID, Date, Total Amount, Product ID, Customer ID)
- **Dimension Tables**:
  - `dim_customer` (Customer ID, Gender, Age)
  - `dim_product` (Product ID, Product Category)
  - `dim_date` (Date, Month, Year)
- [Diagram] (Add a screenshot from draw.io if created)

## ETL Process
1. **Extract**: Read data from `retail_sales.csv` using Pandas.
2. **Transform**: Clean data (remove nulls, standardize dates) and create IDs.
3. **Load**: Store data in SQLite tables.
4. **Automate**: Schedule the pipeline with Apache Airflow on Astronomer.

## Visualizations
- **Seaborn**: `sales_trend.png` shows sales trends by product category over time.
- **Power BI**: Interactive dashboard with sales trends, customer age analysis, and product category distribution (link or screenshot to be added).

## Technologies
- **Python**: Pandas, Seaborn, Matplotlib
- **Database**: SQLite
- **Automation**: Apache Airflow (Astronomer)
- **BI**: Power BI
- **Version Control**: Git, GitHub

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone <your-repo-link>