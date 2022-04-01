#Criar um algoritmo capaz de calcular o faturamento de uma lista de
#produtos com suas respectivas quantidades e preço.
#Verifique a entrada dos produtos, ao digitar sair a captação se encerra.
#Calcular o faturamento com a equação:
 #faturamento = faturamento + (quantidade * preço)
#Utilize uma estrutura for para percorrer toda a lista e pegar as variáveis
#quantidade e preço
lista = []


while True:
    

    produto = input("Digite um produto: ")
    if produto == "sair":
        print("FIM DO FATURAMENTO")
        break
    
    list = []
    quantidade = float(input("Digite a quantidade: "))
    list.append(quantidade)
    mercadoria = (produto)
    lista.append(mercadoria)
            
    preço = float(input("Digite a preço: "))
    list.append(preço)
    
    for i in lista:
        faturamento = 0 
        faturamento = faturamento + (quantidade * preço)
        
    print(f'Com a venda do produto {produto}, seu faturamento foi de R${faturamento} reais')

