# fetch_data.py
from db_connect import collection

records = collection.find({}, {"_id": 0}).sort("table_number", 1)

print("Restaurant Table Data:\n")
for row in records:
    print(row)
