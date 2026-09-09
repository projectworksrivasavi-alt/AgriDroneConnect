from pymongo import MongoClient
import certifi
import os
from dotenv import load_dotenv

load_dotenv()

class LazyCollection:
    """Connect to MongoDB only when a database-backed route is used."""

    def __init__(self, name):
        self.name = name
        self._collection = None

    def _get_collection(self):
        if self._collection is None:
            mongo_uri = os.getenv("MONGO_URI")
            if not mongo_uri:
                raise RuntimeError("MONGO_URI is not configured in Vercel")
            client = MongoClient(mongo_uri, tlsCAFile=certifi.where())
            self._collection = client["AgriDroneDB"][self.name]
        return self._collection

    def __getattr__(self, attribute):
        return getattr(self._get_collection(), attribute)


operators = LazyCollection("operators")
farmers = LazyCollection("farmers")
bookings = LazyCollection("bookings")