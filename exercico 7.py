#Bancos de dados ou bases de dados são conjuntos de arquivos relacionados entre si com registros sobre pessoas
# , lugares ou coisas. São coleções organizadas de dados que se relacionam de forma a criar algum sentido (Informação) e 
# dá mais eficiência durante uma pesquisa ou estudo. Crie uma aplicação python que possa gerar um banco de dados em Sqlite3
#  com o nome de ‘moleza.db’ e criar uma tabela com o nome de ‘pessoas’ com os seguintes campos abaixo:

import sqlite3
conexao = sqlite3.connect('moleza.db')
cursor = conexao.cursor()
sql = """
 CREATE TABLE IF NOT EXISTS moleza (
 id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
 nome TEXT NOT NULL,
 cpf INTEGER
 );
"""
cursor.execute(sql)
print('Tabela criada com sucesso')
conexao.close()
