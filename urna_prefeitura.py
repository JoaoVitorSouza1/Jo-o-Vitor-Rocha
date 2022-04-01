#Construa um algoritmo de votação para a Prefeitura Municipal de Volta
#Redonda. Os votos serão computados da seguinte maneira:

x = 1
branco = 0
samuca = 0
neto = 0
baltazar = 0
nulo = 0
eleitores = 0

print('''OPÇÕES:
-1 -> SAIR,
0 -> Branco,
1 -> SAMUCA,
2 -> NETO,
3 -> BALTAZAR,
4 ou mais -> NULO ''')
while x > -1:
    
    candidatos = int(input("Digite um número da votação para Prefeitura Municipal: "))
    if (candidatos == -1):
        break
    elif (candidatos == 0):
        branco += 1
    elif (candidatos == 1):
        samuca += 1
    elif (candidatos == 2):
        neto += 1
    elif (candidatos == 3):
        baltazar += 1
    elif (candidatos >= 4):
        nulo += 1
    eleitores += 1
    
        
    

if samuca > (neto and baltazar) :
    print("O Vencedor foi o Samuca, candidato número 1. ")
elif neto > (samuca and baltazar):
    print("O Vencedor foi o  Neto, candidato  número 2. ")
elif baltazar > (samuca and neto):
    print("O Vencedor é o Baltazar, candidato  número 3. ")
else:
    print("Não tem vencedores. ")

print("Números de votos em branco:", branco)
print("Números de votos nulos:" ,nulo)
print("Números de eleitores:" , eleitores)
