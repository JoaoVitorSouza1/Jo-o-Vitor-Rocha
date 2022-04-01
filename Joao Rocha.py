#Usando o arquivo texto notas_estudantes.txt escreva um programa que
#imprime o nome dos alunos que têm mais de seis notas.

arquivo = open ('notas_estudantes.txt','r')
lista = arquivo.readlines()
arquivo.close()
alunos = []
for i in lista:
    i = i.split()
    if (len(i))>6:
        alunos.append(i[0])

print('Os alunos com mais de seis notas foram:',alunos)
print('-'*50)

#-----------------------------------------------------------

#Usando o arquivo texto notas_estudantes.txt escreva um programa que
#calcula a média das notas de cada estudante e imprime o nome e a
#média de cada estudante.

for i in lista :
    soma = 0
    nome = i.split()
    for j in (nome[1:]):
        
        soma +=float(j)
        
        media = soma/(len(nome)-1)
        
       
    
    print(f'A média do aluno {nome[0]} foi: {media:.2f}')
print('-'*50)
 

 

#-------------------------------------------------------
#Usando o arquivo texto notas_estudantes.txt escreva um programa que
#calcula a nota mínima e máxima de cada estudante e imprima o nome de
#cada aluno junto com a sua nota máxima e mínima.for item in conteudo:
for i in lista:
    lista = i.split()
    aluno = lista[0] 
   
    notas = []
    for j in lista[1:]:
        notas.append(j)
    
        

    print('A nota minima do(a) aluno(a)', aluno,' foi :', min(notas) ,'e a nota maxima foi:', max(notas))


       
        
        

   


