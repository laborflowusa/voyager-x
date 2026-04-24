import json
import os
from supabase import create_client, Client

url = "https://kwuidjidzeehevigvgwb.supabase.co"
key = "YOUR_ANON_KEY_HERE"
supabase: Client = create_client(url, key)

def handler(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps({"status": "success"})
    }