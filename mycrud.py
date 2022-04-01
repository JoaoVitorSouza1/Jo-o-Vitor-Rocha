from sqlite3.dbapi2 import Cursor


class MyCrud:
    import sqlite3
    conexao =sqlite3.connect('cliente.db')
    cursor = conexao.cursor()
    