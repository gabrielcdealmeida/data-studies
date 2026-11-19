import json
import csv

fieldnames = []

with open("items.json", encoding="utf-8") as json_file:
    data = json.load(json_file)

    for row in data:
        # Extracts the 'headers' from the json file
        for key in row:
            if key not in fieldnames:
                fieldnames.append(key)


with open("items_from_json.csv", mode="w", newline="", encoding="utf-8") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(data)