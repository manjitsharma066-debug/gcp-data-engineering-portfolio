from google.cloud import storage

print("Step 1: Starting...")

from config import *

client = storage.Client.from_service_account_json(
    SERVICE_ACCOUNT
)

print("Step 2: Connected to Cloud Storage")

buckets = client.list_buckets()

print("\nAvailable Buckets:\n")

for bucket in buckets:
    print(bucket.name)

print("\nDone!")