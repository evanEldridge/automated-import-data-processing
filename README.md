# Automated Import Data Processing System

A Python + SQL project that simulates a real-world data pipeline for a logistics or international trade company. It automates the processing, validation, and storage of daily import/export shipment records from CSV files into a normalized SQL Server database.

---

## Overview

This project demonstrates how to:

- Ingest and validate structured data using Python
- Normalize and insert it into a relational database (SQL Server)
- Automate daily imports using scripts and schedulers
- Handle real-world edge cases like new port entries and missing values

Inspired by backend tasks at logistics and customs brokerage firms, this system reflects the kind of internal tooling a junior developer would build or maintain in a data-heavy company.

---

## Tech Stack

- **Python 3**
  - `pandas`
  - `pyodbc`
  - `dotenv`
- **SQL Server Express** (or full SQL Server)
- **T-SQL** (stored procedures, indexing, joins)
- **Windows Task Scheduler** *(for automation)*

---

## Key Features

- ✅ Validates and processes daily import CSV files
- 🔄 Normalizes data across `Countries`, `Ports`, and `Shipments` tables
- ⚠️ Handles missing or duplicate entries gracefully
- 📅 Automates ingestion via scheduler (e.g., cron or Windows Task Scheduler)
- 📜 Logs status of processed files for auditing

---

## Database Schema

  - Countries (CountryID, CountryName)

  - Ports (PortID, PortCode, PortName, CountryID)

  - Shipments (ShipmentID, ShipmentDate, PortID, ProductCode, Quantity, Weight, ValueUSD, SourceFile, LoadTimestamp)


Each shipment is linked to a port and country. The database is normalized to avoid duplication and ensure consistency.

---

## Project Structure

    automated-imports/
    ├── data/ # Input CSV files
    ├── scripts/ # Python ETL scripts
    │ └── process_imports.py
    ├── schema/ # SQL schema and table definitions
    │ └── create_tables.sql
    ├── .env # Database credentials (not tracked in Git)
    ├── README.md # Project overview (this file)
    └── progress.md # Dev notes and daily logs


---

## How to Use

### 🧱 1. Set up the Database
- Install SQL Server Express and SSMS (SQL Server Management Studio)
- Run `schema/create_tables.sql` to initialize tables in a new database called `Imports`

### 🔑 2. Configure Environment
Create a `.env` file in the root directory:

DB_CONN_STR=Driver={ODBC Driver 17 for SQL Server};Server=localhost\SQLEXPRESS;Database=Imports;Trusted_Connection=yes;


### 📥 3. Add Data
Place your `.csv` files into the `data/` folder, e.g.:

import_data_2024_07_01.csv


### ▶️ 4. Run the ETL Script
'''bash python scripts/process_imports.py

### ⏱️ 5. Automate It

Use Windows Task Scheduler or cron to run the script on a schedule (e.g., daily at 2 AM).
💡 Sample Input Format

ShipmentDate,PortCode,PortName,Country,ProductCode,Quantity,Weight,ValueUSD
2024-07-01,LAX,Los Angeles,USA,P123,100,1500.50,250000.00
2024-07-01,SEA,Seattle,USA,P124,50,800.25,100000.00

## What I Learned

How to normalize and design relational schemas

Using Python to perform real-world ETL (Extract, Transform, Load)

Connecting Python to SQL Server using pyodbc

Writing robust, repeatable data ingestion pipelines

Logging and automation for operational reliability

## Why This Project Matters

This system mirrors internal data processing tools used in the import/export industry and is directly applicable to roles in logistics, trade compliance, and backend data operations — like the Junior Software Developer position at Geo. S. Bush & Co., Inc.

## Related Projects / Next Steps

Add Flask dashboard to upload/view records

Add unit tests for ETL functions

Extend schema to include customer or carrier data

Migrate to PostgreSQL for platform independence