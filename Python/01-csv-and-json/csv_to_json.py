import csv
import json

orders = []
with open("items.csv", encoding='utf-8') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        row["quantity"] = int(row["quantity"])
        row["order_id"] = int(row["order_id"])
        row["product_id"] = int(row["product_id"])
        row["unit_price"] = float(row["unit_price"])
        orders.append(row)

with open("items_from_csv.json", "w", encoding="utf-8") as json_file:
    json.dump(orders, json_file, indent=4)
