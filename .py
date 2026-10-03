# 📊 Customer Churn Analysis & Insights

## 📌 Project Overview
This portfolio project focuses on analyzing customer metrics and subscription data to identify behavioral patterns associated with customer churn. The objective is to leverage data cleaning, structural querying, and exploratory data analysis (EDA) to provide actionable, data-driven business insights aimed at improving customer retention.

## 🛠️ Data Architecture & Toolkit
* **Languages & Analytics:** Python, Structured Query Language (SQL)
* **Libraries Utilized:** Pandas, NumPy (Exploratory Data Analysis & Data Cleaning)
* **Database Management:** MySQL (Relational Schema Design & Segment Aggregation)

## 🗂️ Data Ingestion & Relational Schema
To manage the customer transactional data efficiently, a relational schema was structured containing critical analytical attributes:
* **Customer Profile Data:** `CustomerID` (Primary Key), `Demographics`, `TenureMonths`, `ContractType`.
* **Usage & Behavior Metrics:** `MonthlyCharges`, `TotalCharges`, `SupportTicketsRaised`, `ChurnStatus` (Target Metric).

## 🔍 Analytical Methodology

### 1. Data Cleaning & Structured Preparation (Python / Pandas)
* Handled missing values within transactional records (e.g., standardizing incomplete `TotalCharges` fields).
* Filtered anomalous outliers in usage metrics to ensure precise distribution reporting.
* Segmented continuous demographic arrays into discrete behavioral categories.

### 2. Exploratory Data Analysis & Segmentation
* Aggregated core retention metrics utilizing SQL `GROUP BY` clauses to contrast churn rates against variables like contract types.
* Evaluated the correlation between monthly billing values and customer flight risk.
* Identified distinct inflection points where increased customer support tickets strongly correlated with an immediate drop in brand loyalty.

## 📈 Strategic Business Insights Uncovered
* **Contract Vulnerability:** Customers on short-term Month-to-Month contracts exhibited a significantly higher churn velocity compared to long-term structured agreements.
* **Support Ticket Threshold:** Retention rates drop sharply once a user account logs more than 3 unresolved customer support interactions.
* **High-Value Risk:** High-tier financial accounts show distinct behavioral warning signs (e.g., sudden drop in platform usage spikes) roughly 30 days prior to canceling services.
