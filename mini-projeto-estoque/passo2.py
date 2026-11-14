import sqlite3

conexao = sqlite3.connect('estoque.db')
cursor = conexao.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS produtos (
        nome TEXT, preco REAL
    )
''')

cursor.execute('''
    INSERT INTO produtos VALUES (
        'caneta', 2.50
    )
''')

conexao.commit()
conexao.close()