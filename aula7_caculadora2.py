class Calculadora:
    # def __init__(self):
    #     pass
    def soma(self,a,b):
        return a+b

    def subtracao(self,a,b):
        return a-b

    def mutiplicacao(self,a,b):
        return a*b

    def divisao(self,a,b):
        return  a/b

# print(soma(1,2))
# print (soma(3,4))
# print(subtracao(10,2))

calculadora = Calculadora()
# print(calculadora.a)
# print(calculadora.b)
print(calculadora.soma(10,2))
print(calculadora.subtracao(10,2))
print(calculadora.divisao(10,2))
print(calculadora.mutiplicacao(10,2))