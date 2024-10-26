import pymongo

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["Drug_Detection"]
flagged_user_collection = db["FlaggedUsers"]

def add_flagged_user(user_id, suspicious_word_count, classes, suspicious_words, image_file_link):
    # Determine the tag based on the suspicious word count and classes
    tag = "red" if suspicious_word_count >= 3 or len(classes) > 2 else "yellow"
    
    # Create the flagged user document
    flagged_user = {
        "user_id": user_id,
        "tag": tag,
        "classes": classes,
        "suspicious_word_count": suspicious_word_count,
        "suspicious_words": suspicious_words,
        "image_file_link": image_file_link
    }
    
    # Insert the flagged user document into the collection
    flagged_user_collection.insert_one(flagged_user)
    print(f"Added flagged user: {flagged_user}")

# Dummy data for 8 flagged users
dummy_data = [
    {"user_id": "user1", "suspicious_word_count": 7, "classes": ["opioids", "stimulants"], "suspicious_words": ["meth", "crack", "oxy"], "image_file_link": "http://example.com/image1.jpg"},
    {"user_id": "user2", "suspicious_word_count": 2, "classes": ["hallucinogens"], "suspicious_words": ["lsd", "shrooms"], "image_file_link": "http://example.com/image2.jpg"},
    {"user_id": "user3", "suspicious_word_count": 6, "classes": ["cannabis", "stimulants", "opioids"], "suspicious_words": ["weed", "heroin", "cocaine"], "image_file_link": "http://example.com/image3.jpg"},
    {"user_id": "user4", "suspicious_word_count": 4, "classes": ["stimulants"], "suspicious_words": ["speed", "uppers"], "image_file_link": "http://example.com/image4.jpg"},
    {"user_id": "user5", "suspicious_word_count": 10, "classes": ["opioids", "sedatives"], "suspicious_words": ["fentanyl", "valium"], "image_file_link": "http://example.com/image5.jpg"},
    {"user_id": "user6", "suspicious_word_count": 3, "classes": ["hallucinogens"], "suspicious_words": ["dmt", "ayahuasca"], "image_file_link": "http://example.com/image6.jpg"},
    {"user_id": "user7", "suspicious_word_count": 8, "classes": ["cannabis", "stimulants"], "suspicious_words": ["pot", "meth", "ecstasy"], "image_file_link": "http://example.com/image7.jpg"},
    {"user_id": "user8", "suspicious_word_count": 1, "classes": ["none"], "suspicious_words": [], "image_file_link": "http://example.com/image8.jpg"},
]

# Add the dummy data to the flagged users collection
for data in dummy_data:
    add_flagged_user(data["user_id"], data["suspicious_word_count"], data["classes"], data["suspicious_words"], data["image_file_link"])
