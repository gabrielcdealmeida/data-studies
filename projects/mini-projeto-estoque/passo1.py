import sqlite3

conexao = sqlite3.connect('estoque.db')
print('Conectei!')
conexao.close()