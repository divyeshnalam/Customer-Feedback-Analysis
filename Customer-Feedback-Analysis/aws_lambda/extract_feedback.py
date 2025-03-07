import json
import boto3
import csv
import requests

# Salesforce API Configuration
SALESFORCE_INSTANCE = "https://your-instance.salesforce.com"
ACCESS_TOKEN = "your_salesforce_access_token"
S3_BUCKET = "salesforce-feedback-data"
FILE_NAME = "extract.csv"

# S3 Client
s3_client = boto3.client("s3")

# Fetch Data from Salesforce
def fetch_feedback_data():
    url = f"{SALESFORCE_INSTANCE}/services/data/v58.0/query"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json",
    }
    query = {
        "q": "SELECT Id, Customer_Name__c, Feedback__c, Rating__c, Name FROM Feedback__c"
    }

    response = requests.get(url, headers=headers, params=query)
    data = response.json()

    return data.get("records", [])

# Save Data to CSV
def save_to_csv(feedback_data):
    csv_file = "/tmp/" + FILE_NAME
    with open(csv_file, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Id", "Customer_Name__c", "Feedback__c", "Rating__c", "Name"])
        for record in feedback_data:
            writer.writerow([
                record.get("Id", ""),
                record.get("Customer_Name__c", ""),
                record.get("Feedback__c", ""),
                record.get("Rating__c", ""),
                record.get("Name", ""),
            ])
    return csv_file

# Upload CSV to S3
def upload_to_s3(csv_file):
    s3_client.upload_file(csv_file, S3_BUCKET, FILE_NAME)
    print(f"File {FILE_NAME} uploaded to S3 bucket {S3_BUCKET}")

def lambda_handler(event, context):
    feedback_data = fetch_feedback_data()
    if not feedback_data:
        print("No feedback data found.")
        return {"statusCode": 404, "body": "No data found"}

    csv_file = save_to_csv(feedback_data)
    upload_to_s3(csv_file)

    return {"statusCode": 200, "body": "Feedback data extracted and uploaded successfully"}
