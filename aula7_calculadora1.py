class Calculadora:
    def __init__(self,num1,num2):
        self.a = num1
        self.b = num2
    def soma(self):
        return self.a+self.b

    def subtracao(self):
        return self.a-self.b

    def mutiplicacao(self):
        return self.a*self.b

    def divisao(self):
        return  self.a/self.b

# print(soma(1,2))
# print (soma(3,4))
# print(subtracao(10,2))

calculadora = Calculadora(10,2)
print(calculadora.a)
print(calculadora.b)
print(calculadora.soma())
print(calculadora.subtracao())
print(calculadora.divisao())
print(calculadora.mutiplicacao())