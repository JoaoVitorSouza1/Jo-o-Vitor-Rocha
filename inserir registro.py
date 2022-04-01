import sqlite3
conexao = sqlite3.connect('moleza.db')
cursor = conexao.cursor()
nome = 'João Vitor Souza Rocha'
cpf = 16419525713
sql = """
INSERT INTO moleza (nome, cpf)
VALUES (?, ?);
"""
cursor.execute(sql, (nome, cpf))
conexao.commit()
print('Inserido com sucesso')
conexao.close()