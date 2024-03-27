import pymongo

# Connection URI
uri = "mongodb://saikumar.rokkam%40phenom.com@qa-mongo09.aws.phenom.local:27017,qa-mongo08.aws.phenom.local:27017/?authMechanism=PLAIN&authSource=%24external"

# Connect to the MongoDB server
client = pymongo.MongoClient(uri)

# Specify the database name
db = []
db=client.list_database_names()
print(db)
# Now you can perform operations on the collection
