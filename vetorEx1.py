#1. Faça um programa que lê 10 números inteiros do teclado e armazene em um vetor. Ao final
#imprima o vetor armazenado nos dois sentidos

meuvet = []
for i in range(0,10):       
    x = meuvet.append(int(input('Digite um numero:')))
    meuvet_inv= meuvet[::-1]
print(meuvet)
print(meuvet_inv)


    
