import csv
import json

## Reading the CSV file
with open("items.csv", encoding="utf-8") as csv_file:
    reader = csv.DictReader(csv_file)
    total_revenue = 0
    for row in reader:
        print(row["customer_name"], row["unit_price"], row["quantity"])
        total_revenue += float(row["unit_price"]) * float(row["quantity"])
print(f'The total revenue from those sales were {total_revenue:.2f}')

## Reading the JSON file
with open("items.json", encoding="utf-8") as json_file:
    data = json.load(json_file)
    total_revenue = 0
    for row in data:
        print(row["customer_name"], row["unit_price"], row["quantity"])
        total_revenue += row["unit_price"] * row["quantity"]
print(f'The total revenue from those sales were {total_revenue:.2f}')