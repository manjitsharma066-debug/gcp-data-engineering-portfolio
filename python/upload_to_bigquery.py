from config import *
from google.cloud import bigquery

print("Step 1: Starting...")

client = bigquery.Client.from_service_account_json(
    SERVICE_ACCOUNT
)

print("Step 2: Client Connected")


table_ref = f"{PROJECT_ID}.{DATASET_ID}.{TABLE_ID}"

print("Step 3:", table_ref)

job_config = bigquery.LoadJobConfig(
    source_format=bigquery.SourceFormat.CSV,
    skip_leading_rows=1,
    autodetect=True,
    write_disposition="WRITE_TRUNCATE"
)

print("Step 4: Loading File...")

with open(CLEANED_FILE, "rb") as source_file:
    load_job = client.load_table_from_file(
    source_file,
    table_ref,
    location="asia-south1",
    job_config=job_config
)

print("Step 5: Waiting for Job...")
load_job.result()

print("Step 6: Job Completed")

table = client.get_table(table_ref)

print("✅ Data Loaded Successfully!")
print(f"Rows Loaded : {table.num_rows}")
print(f"Table Name  : {table.table_id}")