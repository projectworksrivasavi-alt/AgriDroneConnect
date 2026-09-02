from pymongo import MongoClient
import certifi

client = MongoClient(
    "mongodb+srv://projectworksrivasavi_db_user:Projectwork%405177@cluster0.lmisrad.mongodb.net/AgriDroneDB?retryWrites=true&w=majority&appName=Cluster0",
    tlsCAFile=certifi.where()
)

db = client["AgriDroneDB"]

operators = db["operators"]
farmers = db["farmers"]
bookings = db["bookings"]

print("MongoDB Connected Successfully")
print(client.admin.command("ping"))