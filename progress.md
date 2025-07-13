# 📈 Project Progress Log: Automated Import Data Processing System

This log tracks my day-to-day work on the development of a Python + SQL-based import data processing system. It includes goals, challenges, fixes, and lessons learned.

---

## 🗂️ Project Summary

**Goal:**  
To build a system that automates the processing and normalization of import/export shipment data from CSV files into a SQL Server database.

**Tech Stack:**  
- Python (`pandas`, `pyodbc`, `dotenv`)
- SQL Server Express
- T-SQL
- Windows Task Scheduler (for automation)

---

## ✅ Tasks Overview

| Task | Status |
|------|--------|
| Create README.md for GitHub | ✅ Done |
| Set up local SQL Server instance | 🔄 In Progress |
| Design normalized database schema | 🔄 In Progress |
| Write SQL schema script | 🔄 In Progress |
| Create sample CSV data | 🔄 In Progress |
| Write Python script to ingest and validate data | ⬜ Not Started |
| Handle foreign key relationships in script  ⬜ Not Started |
| Add logging to track processed files | ⬜ Not Started |
| Automate script with Task Scheduler | ⬜ Not Started |
| Write tests for ETL functions | ⬜ Not Started |

---

## 🗓️ Daily Logs

### 🗓️ **7-12-2025** – Project Kickoff  
**What I did:**  
- Installed SQL Server Express + SSMS  
- Sketched out database schema  
- Created GitHub repo and project folder structure 
- Wrote schema SQL scripts and created tables in local 'Imports' database

**Challenges:**  
- Needed to verify that pyodbc driver works with SQL Server Express

**Next steps:**    
- Build sample CSV files
- Write a basic script to read a CSV and connect to the database

---

## 🛠️ TODO / Future Features

- [ ] Add a dashboard to view ingestion status
- [ ] Export daily summary reports
- [ ] Add unit tests for the ETL logic
- [ ] Support JSON input formats

---

