import sqlite3
import pandas as pd

data = pd.read_excel('sales.xlsx')
print(data.head())

connection = sqlite3.connect('sales.db')
data.to_sql('sales',connection, if_exists='replace', index=False)
connection.close()

print('Done!')

