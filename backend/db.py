from motor.motor_asyncio import AsyncIOMotorClient

uri = "db uri"

# Create a new client and connect to the server
client = AsyncIOMotorClient(uri)

db= client.subjectsdb
subjects_collection = db.subjects
encodings_collection = db.encodings

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)