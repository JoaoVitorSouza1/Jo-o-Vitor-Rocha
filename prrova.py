class A:
    a = 1
    __b = 2

class B(A):
    __c = 3
    def __init__(self):
        print(self.a)
        print(self.__c)
    def pNome(self):
        print(self.__b)

x = B() 
x.pNome()     


