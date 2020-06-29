lista = [1,3,5,7]
listaAnimal = ['cachorro','gato','elefante']
print(type(lista))
print(lista) # pode conter tipos de dados diferentes
print(listaAnimal[0])
for x in listaAnimal: # x assume o valor na possição da lista
    print(x)

print(sum(lista))
print(max(lista))
print(min(lista))

print(min(listaAnimal)) # segue a ordem alfabetica
print(max(listaAnimal))

if 'gato' in listaAnimal:
    print("gato econtrado")

novaLista = listaAnimal*3 #cria lista com valores triplicados

#adidiocnar intem na lista dinamicamente
listaAnimal.append('lobo')
print(listaAnimal)

# retira o ultima item da lista
listaAnimal.pop()
print(listaAnimal)
#remove pela posição na lista
listaAnimal.pop(0)
print(listaAnimal)
#remove pelo valor na lista
listaAnimal.remove('gato')
print(listaAnimal)
#ordena a lista numerica ou alfabeticamente
lista.sort()
print(lista)
#reverte os valores da lista
lista.reverse()
print(lista)
print(len(lista))
# Tuplas são imutáveis, diferente da lista
print('\n\n\n\n')
tupla = (1,10,12,5,14) # lista adicionada entre parentes e não colchetes
print(tupla)
print(tupla[1])
print(len(tupla))
tuplaAnimal = tuple(listaAnimal) #converte uma tupla em uma lista

listaTupla = list(tupla)
print(tuplaAnimal)
print(listaTupla)