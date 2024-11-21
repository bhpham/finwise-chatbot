# google_cloud_utils.py

import os
import base64
from google.cloud import storage

def initialize_google_cloud():
    # Get the base64-encoded credentials from the environment variable
    encoded_credentials = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")

    if encoded_credentials:
        # Decode and write the credentials to a temporary file
        with open("/tmp/service-account.json", "wb") as f:
            f.write(base64.b64decode(encoded_credentials))

        # Set the GOOGLE_APPLICATION_CREDENTIALS to the temp file
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/tmp/service-account.json"

    # Initialize the Google Cloud client
    client = storage.Client()
    
    # Try to access Google Cloud Storage buckets
    buckets = client.list_buckets()
    bucket_names = [bucket.name for bucket in buckets]
    return bucket_names
