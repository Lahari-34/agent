from pymongo import MongoClient
from pymongo.errors import CollectionInvalid

client = MongoClient("mongodb://localhost:27017/")
db = client["restaurant_management"]

validator = {
    "$jsonSchema": {
        "bsonType": "object",
        "required": [
            "table_number",
            "capacity",
            "location",
            "status"
        ],
        "properties": {
            "table_number": {
                "bsonType": "int",
                "description": "must be an integer and is required"
            },
            "capacity": {
                "bsonType": "int",
                "minimum": 1,
                "description": "must be an integer and is required"
            },
            "location": {
                "bsonType": "string",
                "description": "must be a string and is required"
            },
            "status": {
                "enum": ["Available", "Reserved"],
                "description": "must be Available or Reserved"
            },
            "customer_name": {
                "bsonType": ["string", "null"],
                "description": "can be string or null"
            },
            "reservation_time": {
                "bsonType": ["string", "null"],
                "description": "can be string or null"
            }
        }
    }
}

try:
    db.create_collection("restaurant_tables")
except CollectionInvalid:
    pass

db.command({
    "collMod": "restaurant_tables",
    "validator": validator,
    "validationLevel": "strict"
})

print("Schema validation applied successfully.")
