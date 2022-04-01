   
# 2. Ler um vetor de 10 elementos. Crie um segundo vetor, com todos os elementos na ordem
#inversa, ou seja, o último elemento passará a ser o primeiro, o penúltimo será o segundo e
#assim por diante. Imprima os dois vetores. 

meuvet = []
for i in range(10):       
    x = meuvet.append(int(input('Digite um numero:')))
    meuvet_inv= meuvet[::-1]
print(meuvet)
print(meuvet_inv)


    