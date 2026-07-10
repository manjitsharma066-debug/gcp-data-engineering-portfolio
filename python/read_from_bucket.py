from google.cloud import storage
import pandas as pd
from io import BytesIO

from config import *

# Create Storage Client
client = storage.Client.from_service_account_json(
    SERVICE_ACCOUNT
)

bucket = client.bucket(BUCKET_NAME)

blob = bucket.blob(BUCKET_FILE)

data = blob.download_as_bytes()

df = pd.read_csv(BytesIO(data))

print("✅ File Read Successfully From Cloud Storage\n")

print(df.head())