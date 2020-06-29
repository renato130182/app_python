conjunto = {2,3,4,5} # não aceita elementos duplicados
print(type(conjunto))
print(conjunto)
conjunto.add(6)
print(conjunto)
conjunto.discard(3)
#conjunto.remove(2)
print(conjunto)
#
# conjunto2 = {4,10,11,12}
# conjuntoUniao = conjunto.union(conjunto2) # discarta elementos duplicados
# print(conjuntoUniao)
#
# conjuntoIntersection = conjunto.intersection(conjunto2) # apenas o que existe nos dois
# print(conjuntoIntersection)
#
# print('\n\n\nDiferenças')
# print(conjunto)
# conjunto3 = {3,4,5,6}
# print(conjunto3)
# conjuntoDiferenca = conjunto.difference(conjunto3)  # o que tiver em conjunto mas não em conjunto 3
# print(conjuntoDiferenca)
# conjuntoDiferencaINV = conjunto3.difference(conjunto) # o que tiver e, conjunto3 e não em conjunto
# print(conjuntoDiferencaINV)
# conjuntoDiferencaSimetrica = conjunto.symmetric_difference(conjunto3);
# print(conjuntoDiferencaSimetrica)
# #
# # print('\n\n\n Subconjuntos')
# # c_a = {1,2,3,4,5,6}
# # c_b = {2,3,4}
# # c_subConjuntoA = c_a.issubset(c_b) # A esta contido em B? False
# # print(c_subConjuntoA)
# # c_subConjuntoB = c_b.issubset(c_a) # b esta contido em a? True
# # print(c_subConjuntoB)
# #
# # c_superSet = c_a.issuperset(c_b) # A contem todos os itens de B? True
# # print(c_superSet)
# #
# # print('\n\n\n Conversões')
# # listaConv = ['a','a','b','c']
# # print(listaConv)
# # c_conv = set(listaConv) # converte e remove a duplicidade
# # print(c_conv)