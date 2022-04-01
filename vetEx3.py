#3. Ler um vetor de 10 elementos inteiros e positivos. Criar um segundo vetor da seguinte
#forma: os elementos de índice par receberão os respectivos elementos divididos por 2; os
#elementos de índice ímpar receberão os respectivos elementos multiplicados por 3. Imprima
#os dois vetores. 

meuvet1 = []
meuvet2= []
for i in range(0,10):
    
     meuvet1.append(int(input('Digite um numero:')))
for i in range(len(meuvet1)):     
     if i % 2==0:
          meuvet2.append(meuvet1[i] / 2)

          
          
     else:
          meuvet2.append(meuvet1[i]  * 3)
          
          
         


     
print(meuvet1)
print(meuvet2)


