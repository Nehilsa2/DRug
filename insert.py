import pymongo
import random
from datetime import datetime

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["Drug_Detection"]  # Replace with your database name
interaction_collection = db["interaction"]  # Replace with your interaction collection name

# List of 5 sample users
users = ["user_1", "user_2", "user_3", "user_4", "user_5"]

# Generate interactions
interactions = []
interaction_count = 10  # Adjust as needed for the number of interactions

for i in range(interaction_count):
    members = random.sample(users, 2)  # Pick 2 random users for interaction
    interaction = {
        "_id": f"interaction_{i + 1}",  # Unique ID for each interaction
        "members": members,
        "createdAt": datetime.utcnow().isoformat(),
        "updatedAt": datetime.utcnow().isoformat()
    }
    interactions.append(interaction)

# Insert generated interactions into the MongoDB collection
interaction_collection.insert_many(interactions)

print(f"Inserted {len(interactions)} interactions into the collection.")
