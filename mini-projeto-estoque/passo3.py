import sqlite3

conexao = sqlite3.connect('estoque.db')
cursor = conexao.cursor()

cursor.execute('''
    SELECT *
    FROM produtos
''')

print(cursor.fetchall())
conexao.close()
