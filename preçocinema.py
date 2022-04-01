domingo = 1
segunda = 2
terça  = 3
quarta =4
quinta= 5
sexta = 6
sabado= 7
preçoint = 20
preçom= 0



idade  = int(input('Digite sua idade :'))
diasem = int(input('Digite o dia da semana:'))

if diasem == 3 and idade > 15:
    preçom=preçoint/2
elif diasem ==3 and idade <=14:
    preçom=preçoint/4
elif idade<=14:
    preçom=preçoint/2

elif diasem !=3 and idade> 14:
    preçom=preçoint


print('Pessoa com ',idade,'anos pagara ',preçom,'reais')

    

