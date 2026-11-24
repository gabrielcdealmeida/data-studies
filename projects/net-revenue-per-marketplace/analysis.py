import csv
import json
import duckdb
import pandas as pd
from datetime import datetime

# Function to correct date formats
def correct_date(date):
    try:
        parsed_date = datetime.strptime(date, '%d/%m/%Y')
        clean_date = parsed_date.strftime('%Y-%m-%d')
        return clean_date
    except ValueError:
        pass

    try:
        parsed_date = datetime.strptime(date, '%d-%b-%Y')
        clean_date = parsed_date.strftime('%Y-%m-%d')
        return clean_date
    except ValueError:
        pass

    try:
        parsed_date = datetime.strptime(date, '%Y-%m-%d')
        clean_date = parsed_date.strftime('%Y-%m-%d')
        return clean_date
    except ValueError:
        pass


def get_revenue_report(path):

    rejected_orders = []
    valid_orders = []
    fieldnames = []
    unique_orders = set()
    marketplaces = set()
    status = set()
    report = {}

    # Data overview
    duckdb.sql(f'''
        SELECT *
        FROM '{path}'
    ''').show()

    # Reads the .csv file, cleans and stores the data
    with open(path, encoding='utf-8') as c_f:
        data = csv.DictReader(c_f)
        for row in data:

            # Rejects invalid orders - Due to quantity
            try: 
                row['quantity'] = int(row['quantity']) 
            except:
                row['reason'] = 'Incorrect quantity format'
                rejected_orders.append(row)
                #print('Invalid order added to rejected_orders list')


            # Rejects invalid orders - Due to unit_price
            row['unit_price'] = row['unit_price'].strip()

            if 'R$' in row['unit_price']:
                row['unit_price'] = row['unit_price'].replace('R$', '')

            if '.' in row['unit_price'] and ',' in row['unit_price']:
                row['unit_price'] = row['unit_price'].replace('.','').replace(',','.') 
            elif ',' in row['unit_price'] and '.' not in row['unit_price']:
                row['unit_price'] = row['unit_price'].replace(',','.')

            try:
                row['unit_price'] = round(float(row['unit_price']),2)
            except:
                if row in rejected_orders:
                    row['reason'] = 'Incorrect quantity and unit price format'

                if row not in rejected_orders:
                    row['reason'] = 'Incorrect unit price format'
                    rejected_orders.append(row)
                    #print('Invalid order added to rejected_orders list')


            # Handles the issues in the columns 'marketplace' and 'status'
            row['marketplace'] = row['marketplace'].lower().strip().title()
            row['status'] = row['status'].lower().strip().title()

            if row['status'] == 'Canceled':
                row['status'] = 'Cancelled' 

            marketplaces.add(row['marketplace'])
            status.add(row['status'])

            # Cleans the 'customer' column data
            row['customer'] = row['customer'].strip().title()

            # Corrects the date format
            row['order_date'] = correct_date(row['order_date'])

            # Adds the row to the 'valid_orders' list
            if row not in rejected_orders:
                valid_orders.append(row)
                
                # Stores the order ID
                unique_orders.add(row['order_id'])  

    df_valid = pd.DataFrame(valid_orders)
    df_rejected = pd.DataFrame(rejected_orders)

    # Clean data overview
    duckdb.sql('''
        SELECT *
        FROM df_valid
    ''').show()

    # What is the net revenue and quantity of orders per marketplace? (Cancelled orders are not included)
    revenue_orders = duckdb.sql('''
        SELECT marketplace, COUNT(*) AS orders, SUM(quantity * unit_price) AS revenue
        FROM df_valid
        WHERE status != 'Cancelled'
        GROUP BY marketplace
    ''').fetchall()

    # Creates a dictionary of quantity of orders and revenue per marketplace, and creates a .json file from it
    for marketplace in revenue_orders: 
        report[marketplace[0]] = {'orders': marketplace[1], 'revenue': marketplace[2]}

    with open('revenue_report.json', 'w', encoding='utf-8') as j_f:
        json.dump(report, j_f, indent=4)

    # Creates a .csv file for the rejected orders
    for r_order in rejected_orders:
        for header in r_order:
            if header not in fieldnames:
                fieldnames.append(header)

    with open('rejected_orders.csv', mode="w", newline="", encoding="utf-8") as c_f_2:
        writer = csv.DictWriter(c_f_2, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(rejected_orders)

    return report

# Runs the function
if __name__ == "__main__":
    report = get_revenue_report('orders.csv')


