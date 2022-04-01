#5. Faça um programa que leia e monte dois vetores de números inteiros com 20 números
#cada. Depois de montados gere um terceiro vetor formado pela diferença dos dois vetores
#lidos, um quarto vetor formado pela soma dos dois vetores lidos e por último um quinto vetor
#formado pela multiplicação dos dois vetores lidos. 


meuvet1 = []
meuvet2 = []
meuvet3 = []
meuvet4 = []
meuvet5 = []
for i in range(0,3):
    meuvet1.append(int(input('Digite um valor:')))
for i in range(0,3):
    meuvet2.append(int(input('Digite um valor:')))
for i in range(len(meuvet1)):
    if  meuvet1[i] != meuvet2[i]:

        meuvet3.append(meuvet1[i])
for i in range(len(meuvet1)):
    meuvet4.append(meuvet1[i] + meuvet2[i])
for i in range(len(meuvet1)):
    meuvet5.append(meuvet1[i] * meuvet2[i])

print(meuvet3)
print(meuvet1)
print(meuvet2)
print(meuvet4)
print(meuvet5)



