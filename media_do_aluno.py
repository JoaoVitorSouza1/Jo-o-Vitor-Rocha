

#Escreva um procedimento que recebe as 3 notas de um aluno por parâmetro e uma letra. Se a
#letra for A o procedimento calcula a média aritmética das notas do aluno, se for P, a sua média
#ponderada (pesos: 5, 3 e 2) e se for H, a sua média harmônica. A média calculada também deve
#retornar por parâmetro.

nota1= float(input("digite a primeira nota:"))
nota2 = float(input('Digite a segunda nota:'))
nota3 = float(input('Digite a terceira nota:'))
letra = input('Digite uma letra:')

if letra == 'A':
    mediaA = ((nota1 + nota2 + nota3) /3)
    print('Sua media aritimetica foi :',mediaA)
elif letra == 'P':
    mediaP = ((nota1* 3) + (nota2*3) + (nota3*2))/10
    mediaP1 = mediaP/10
    print('sua media ponderada foi:',mediaP)
elif letra == 'H':
    m = (1/nota1) + (1/nota2) + (1/nota3)
    mediaH =( 3/m)
    print(f'Sua média harmonica foi :{mediaH:.2f}')





n = int(input("Verificar numeros primos ate: "))
mult=0

for i in range(2,n):
    if (n % i == 0):
        #print("Múltiplo de",count)
        mult += 1

if(mult==0):
    print("É primo")
else:
    print("Não primo")





