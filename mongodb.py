from pymongo import MongoClient
import certifi
import os
from dotenv import load_dotenv

load_dotenv()

mongo_uri = os.getenv("MONGO_URI")
if not mongo_uri:
    raise RuntimeError("MONGO_URI must be set in the environment")

client = MongoClient(
    mongo_uri,
    tlsCAFile=certifi.where()
)

db = client["AgriDroneDB"]

operators = db["operators"]
farmers = db["farmers"]
bookings = db["bookings"]