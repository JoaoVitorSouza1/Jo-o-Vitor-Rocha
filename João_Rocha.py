#1. Criar um código que grave os seguintes campos (nome, disciplina, idade). Sua primeira chave será (‘segundo-periodo’) e sua segunda chave será sua matrícula (‘3918’).

#2. Poste no NEAD o algoritmo (1 ponto). Rode-o para gravar no banco (1 ponto).

import pyrebase

config = {
   "apiKey": "AIzaSyBqLBA8kfIKCjcv-h6lRHIMylQxBsStNBE",
   "authDomain": "clientes-28e4a.firebaseapp.com", 
   "databaseURL": "https://clientes-28e4a.firebaseio.com/", 
    "storageBucket": "clientes-28e4a.appspot.com"
 }
firebase = pyrebase.initialize_app(config)
db = firebase.database()

dados = {
    'Nome ':'João Vitor Souza Rocha',
    'Idade':'25 anos',
    'Disciplina': 'Programação 1',
}

db.child ('segundo-periodo').child('2021101400').set(dados)
print('foi')




