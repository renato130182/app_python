#Lambda é uma função anonima

contador_letras = lambda lista:[len(x) for x in lista]
lista = ['cachorro','gato']
print(contador_letras(lista))

#dicionario de dados
calculadora = {
    'soma' : lambda a,b:a+b,
    'sub' : lambda a,b:a-b,
    'mult' : lambda a,b:a*b,
}
soma = calculadora['soma']
print(soma(10,5))
m = calculadora['mult']
print(m(2,2))

