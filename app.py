from pymongo import MongoClient

# Yahan wahi URI daalo jo humne finalize ki thi
uri = "mongodb+srv://dev:Sahdev1996@weighbridge.14bereq.mongodb.net/safety_video_db?retryWrites=true&w=majority"

try:
    client = MongoClient(uri)
    # Ping karke check karo ki server response de raha hai ya nahi
    client.admin.command('ping')
    print("✅ Connection Successful! Database connected.")
except Exception as e:
    print(f"❌ Connection Failed: {e}")