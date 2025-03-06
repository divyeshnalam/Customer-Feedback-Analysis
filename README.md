# Customer-Feedback-Analysis

# Customer Feedback Analysis System

## Overview
The **Customer Feedback Analysis System** integrates **Salesforce, AWS, and SQL** to store, process, and analyze customer feedback data. This project extracts feedback from Salesforce, stores it in **Amazon S3**, loads it into **Amazon RDS (MySQL/PostgreSQL)**, and visualizes insights using **Salesforce Reports**.

---

## Tech Stack
- **Salesforce:** Stores customer feedback using a **custom object**.
- **AWS Lambda & S3:** Extracts feedback from Salesforce and stores it in **Amazon S3**.
- **Amazon RDS (MySQL/PostgreSQL):** Stores and analyzes feedback using SQL queries.
- **GitHub:** Showcases the project code and SQL queries.

---

## Architecture
```
📦 Customer-Feedback-Analysis
 ┣ 📂 aws_lambda
 ┃ ┣ 📜 extract_feedback.py  # Fetch from Salesforce & save to S3
 ┃ ┣ 📜 load_to_rds.py       # Move data from S3 to RDS
 ┣ 📂 sql_queries
 ┃ ┣ 📜 create_tables.sql    # SQL script for table setup
 ┃ ┣ 📜 analysis_queries.sql # Queries to find trends
 ┣ 📜 README.md              # Project documentation
 ┗ 📜 architecture.png        # Project architecture diagram
```

---

## Implementation Steps

### 1️⃣ Setup Salesforce for Feedback Collection
1. **Create a Salesforce Custom Object** – `Customer_Feedback__c`
   - Fields: `Customer Name`, `Email`, `Feedback`, `Rating`, `Date`
2. **Enable Salesforce REST API** to allow AWS Lambda to access data.

### 2️⃣ AWS Lambda & S3 for Data Extraction
1. **Write a Python AWS Lambda function** to:
   - Connect to Salesforce API
   - Extract feedback data
   - Store it as a JSON file in **Amazon S3**
2. **Deploy the Lambda function** and set it to trigger daily using **AWS EventBridge**.

### 3️⃣ Store Data in Amazon RDS (SQL)
1. **Create a MySQL/PostgreSQL database** in Amazon RDS.
2. **Write an AWS Lambda function** to:
   - Read the JSON file from **S3**
   - Insert feedback into the **SQL database**
   - Run SQL queries to analyze sentiment & trends

### 4️⃣ Analyze Feedback in Salesforce Reports
1. **Connect Amazon RDS to Salesforce using External Data Sources**.
2. **Create Salesforce Reports & Dashboards** to visualize trends (e.g., average rating over time).

---

## Setup & Deployment
### Prerequisites
- **Salesforce Developer Account** with API access
- **AWS Account** with IAM permissions
- **MySQL/PostgreSQL Database** in Amazon RDS

### Steps
1. **Clone this repository**
   ```sh
   git clone https://github.com/yourusername/Customer-Feedback-Analysis.git
   ```
2. **Set up Salesforce API credentials** in AWS Secrets Manager.
3. **Deploy AWS Lambda functions** to extract and load data.
4. **Create tables in Amazon RDS** using `create_tables.sql`.
5. **Run SQL queries** to analyze feedback trends.
6. **Connect RDS to Salesforce** and create Reports/Dashboards.

---

## Sample SQL Queries
### Create Table
```sql
CREATE TABLE customer_feedback (
    id SERIAL PRIMARY KEY,
    customer_name VARCHAR(255),
    email VARCHAR(255),
    feedback TEXT,
    rating INT,
    feedback_date DATE
);
```
### Analyze Average Rating
```sql
SELECT AVG(rating) AS avg_rating, feedback_date
FROM customer_feedback
GROUP BY feedback_date
ORDER BY feedback_date DESC;
```

---

## Contributing
Feel free to contribute to this project by submitting pull requests or reporting issues.
