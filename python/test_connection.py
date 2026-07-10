from google.cloud import bigquery

print("Starting connection...")

client = bigquery.Client.from_service_account_json(
    "../credentials/service-account.json"
)

print("✅ Connected Successfully")
print("Project ID:", client.project)