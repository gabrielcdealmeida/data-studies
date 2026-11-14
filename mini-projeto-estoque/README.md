# Mini projeto: controle de estoque com Python e SQLite

Meu primeiro projeto integrando Python e SQL, feito na Fase 1 do meu plano de estudos para me tornar engenheiro de dados.

## O que o projeto faz
Cria um banco de dados SQLite com uma tabela de produtos, insere produtos e consulta os dados com SELECT e WHERE.

## Tecnologias
- Python 3
- SQLite (módulo `sqlite3`, que já vem com o Python)
- SQL: CREATE TABLE, INSERT, SELECT e WHERE

## Como rodar
1. Clone este repositório.
2. Entre na pasta do projeto: `cd mini-projeto-estoque`
3. Rode os arquivos em ordem, por exemplo: `python passo1.py`, depois `python passo2.py`, e assim por diante. (No Windows, se `python` não funcionar, use `py`.)

## Resultado
Ao rodar a consulta com `WHERE preco > 50`, o programa mostra:
`[('mouse', 59.9), ('teclado', 89.9)]`

## O que aprendi
- Como o Python se conecta a um banco de dados e envia comandos SQL.
- Que o `commit()` é o que grava as mudanças feitas por INSERT.
- Como inserir vários produtos de uma vez com `executemany`.