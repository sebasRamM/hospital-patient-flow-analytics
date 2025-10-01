# Hospital patient flow analytics

This project demonstrates a real-time data engineering pipeline for healthcare, designed to analyze patient flow across hospital departments using Azure cloud services.
The pipeline ingests streaming data, processes it in Databricks (PySpark), and stores it in Azure Synapse SQL Pool for analytics and visualization.

Data Engineering: Build the real-time ingestion + transformation pipeline.

🎯 Objectives
Collect real-time patient data via Azure Event Hub.
Process and cleanse data using Databricks (Bronze → Silver → Gold layers).
Implement a star schema in Synapse SQL Pool for efficient querying.
Enable Version Control with Git.

🛠️ Tools & Technologies
Azure Event Hub – Real-time data ingestion
Azure Databricks – PySpark-based ETL processing
Azure Data Lake Storage – Staging raw and curated data
Azure Synapse SQL Pool – Data warehouse for analytics
Python 3.9+ – Core programming
Git – Version control

📐 Data Architecture
The pipeline follows a multi-layered architecture:

Bronze Layer: Raw JSON data from Event Hub stored in ADLS.
Silver Layer: Cleaned and structured data (validated types, null handling).
Gold Layer: Aggregated and transformed data ready for BI consumption.

⭐ Star Schema Design
The Gold layer data in Synapse follows a star schema for optimized analytics:

Fact Table: FactPatientFlow (patient visits, timestamps, wait times, discharge)
Dimension Tables:
DimDepartment – Department details
DimPatient – Patient demographic info
DimTime – Date and time dimension
