from db_connect import collection

sample_data = [
    {
        "table_number": 1,
        "capacity": 4,
        "location": "Window",
        "status": "Reserved",
        "customer_name": "Riya",
        "reservation_time": "2026-04-08 07:30 PM"
    },
    {
        "table_number": 2,
        "capacity": 2,
        "location": "Indoor",
        "status": "Available",
        "customer_name": None,
        "reservation_time": None
    },
    {
        "table_number": 3,
        "capacity": 6,
        "location": "Outdoor",
        "status": "Reserved",
        "customer_name": "Arjun",
        "reservation_time": "2026-04-08 08:00 PM"
    },
    {
        "table_number": 4,
        "capacity": 4,
        "location": "Rooftop",
        "status": "Available",
        "customer_name": None,
        "reservation_time": None
    }
]

for item in sample_data:
    collection.update_one(
        {"table_number": item["table_number"]},
        {"$set": item},
        upsert=True
    )

print("Sample data inserted successfully.")
