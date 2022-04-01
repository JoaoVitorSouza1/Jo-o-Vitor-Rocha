#): Sabemos que a área de um retângulo é (A = l * c) e o seu Perímetro é (P = l * l * l * l), 
#  sendo l = lado, c = comprimento. Construa uma classe chamada Retângulos com dois métodos: área e perímetro:
#Lado = int(input('digite o valor do lado:'))
#comprimento = int(input('digite o valor do comprimento:'))
class retangulo:
    
        def __init__(self, lado = None  ,comprimento = None):
            self.lado = lado
        
            self.comprimento = comprimento
            area =self.lado *  self.comprimento
            perimetro = lado *lado *lado *lado 
        
    
    
    
            def __init__(self, area ,perimetro ):
                self.area = area
    
                self.perimetro = perimetro
    
    
        

    
    
         

  
x = retangulo(2,2)
print('O valor da area é ',x.area)
print('O valor do perimetro é' ,x.perimetro)

     




    
 
 
 
 
 
 

