import sqlite3

conexao = sqlite3.connect('estoque.db')
cursor = conexao.cursor()

produtos = [
    ('caderno', 18.90),
    ('mouse', 59.90),
    ('teclado', 89.90),
]

cursor.executemany('INSERT INTO produtos VALUES (?, ?)', produtos)
conexao.commit()

cursor.execute('SELECT * FROM produtos WHERE preco > 50')
print(cursor.fetchall())
conexao.close()
