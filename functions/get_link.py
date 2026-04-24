import json
import random
import os
from supabase import create_client, Client

url = "https://kwuidjidzeehevigvgwb.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imt3dWlkamlkemVlaGV2aWd2Z3diIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzY3MjMxNzMsImV4cCI6MjA5MjI5OTE3M30.1HRlRYVgc4-Br_T70-SwlVGGluUtLZLi6-9h7SWxpb0"
supabase: Client = create_client(url, key)

def handler(event, context):
    user_id = event.get("queryStringParameters", {}).get("user_id", "anonymous")
    
    links_response = supabase.table("links").select("*").execute()
    links = links_response.data
    
    if not links:
        return {
            "statusCode": 200,
            "body": json.dumps({"affiliate_link": "https://example.com/no-links"})
        }
    
    selected = random.choice(links)
    
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps({"affiliate_link": selected["url"]})
    }