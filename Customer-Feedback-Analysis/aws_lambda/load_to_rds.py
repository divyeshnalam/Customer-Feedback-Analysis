import json
import boto3
import io
import pymysql
import csv

# AWS S3 and RDS Configuration
S3_BUCKET = "salesforce-feedback-data"
FILE_NAME = "extract.csv"
RDS_HOST = "your-rds-endpoint.amazonaws.com"
RDS_USER = "admin"
RDS_PASSWORD = "your-password"
RDS_DB = "salesforce_feedback"

# S3 Client
s3_client = boto3.client("s3")

def lambda_handler(event, context):
    try:
        # Download file from S3
        file_obj = s3_client.get_object(Bucket=S3_BUCKET, Key=FILE_NAME)
        file_content = file_obj["Body"].read().decode("utf-8")
        csv_reader = csv.reader(io.StringIO(file_content)) 
        feedback_data = list(csv_reader)

        # Remove header row
        headers = feedback_data[0]
        data_rows = feedback_data[1:]

        # Connect to RDS
        conn = pymysql.connect(
            host=RDS_HOST, user=RDS_USER, password=RDS_PASSWORD, database=RDS_DB
        )
        cursor = conn.cursor()

        for row in data_rows:
            sql = """INSERT INTO feedback (customer_name, feedback_text, rating, customer_id, comments) 
                     VALUES (%s, %s, %s, %s, %s)"""
            cursor.execute(sql, (row[1], row[2], row[3] if row[3] else None, row[0], row[4]))

        conn.commit()
        cursor.close()
        conn.close()
        print("Data inserted successfully!")

    except Exception as e:
        print(f"Error: {e}")

    return {"statusCode": 200, "body": json.dumps("Processing Complete")}
