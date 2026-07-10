import subprocess
import sys

print("=" * 60)
print("      GCP DATA ENGINEERING ETL PIPELINE")
print("=" * 60)

steps = [
    ("ETL Process", "python/etl.py"),
    ("Upload to BigQuery", "python/upload_to_bigquery.py"),
    ("Connect to GCS", "python/gcs_connection.py"),
    ("Read from GCS", "python/read_from_bucket.py"),
]

for step_name, script in steps:
    print(f"\nRunning: {step_name}")

    result = subprocess.run([sys.executable, script])

    if result.returncode != 0:
        print(f"\n❌ Pipeline Stopped at: {step_name}")
        break
else:
    print("\n🎉 ETL Pipeline Completed Successfully!")