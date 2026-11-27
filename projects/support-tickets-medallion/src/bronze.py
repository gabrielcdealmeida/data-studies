import csv
from pathlib import Path

class ColumnsError(Exception):
    pass

def read_files():
    ## Sets the file path
    file_root = Path(__file__).resolve().parent.parent
    file_path = file_root / 'data' / 'raw'
    
    files = [
        file_path / 'customers.csv',
        file_path / 'equipment.csv',
        file_path / 'tickets.csv'
    ]

    ## Lists the desired columns for each file
    expected_columns = {
        'customers': ['customer_id', 'name', 'city', 'email'],
        'equipment': ['equipment_id', 'model', 'customer_id', 'install_date'],
        'tickets': ['ticket_id', 'equipment_id', 'opened_at', 'closed_at', 'status']
    }

    ## Initializes the missing columns dictionary
    missing_columns = {}

    ## Opens and verifies the existence of the desired files
    for file in files:
        table_name = file.stem
        try:
            with file.open('r', encoding='utf-8-sig', newline='') as table:
                data = csv.reader(table)

                ## Gets the table's header
                header = next(data, [])

                #for row in data:
                #    print(row)

            print('\n')

        except FileNotFoundError:
            print(f'Error: File "{file}" not found!')
            return

        else:
            ## Verifies if the expected columns exist in the header
            expected = expected_columns.get(table_name, [])
            missing = [col for col in expected if col not in header]  
            missing_columns[table_name] = missing  

            if not any(missing_columns.values()):
                print(f'No columns missing in {table_name}') 
            else:
                print(f'Columns {missing} missing in {table_name}')
    
    print('Files successfully read!')

## Start
read_files()
        
        


