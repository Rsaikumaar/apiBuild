from pymongo import MongoClient

# MongoDB connection string
mongo_uri = "mongodb://saikumar.rokkam%40phenom.com:Rokkam9%40123@ana-mongo01.prod.phenom.local:27017,ana-mongo02.prod.phenom.local:27017,ana-mongo03.prod.phenom.local:27017/admin?authMechanism=PLAIN&authSource=%24external"

# Connect to MongoDB server
mongo_client = MongoClient(mongo_uri)

# Select database (optional)
mongo_db = mongo_client.get_database('Analytics_Pro')

# Select collection (optional)
mongo_collection = mongo_db['Apply_Configcle']
print("success")
# Define your query
# Example: Find all documents where the value of the 'field_name' field is equal to 'desired_value'
all_data=mongo_collection.find()

# Iterate over the result set and print each document
for document in all_data:
    print(document)

print("success")