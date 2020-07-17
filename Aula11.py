lista = [1,10]

try:
    divisao = 10/0
    #numero = lista[3]
    #x=a
except ZeroDivisionError:
    print('Divisão por zero')
except IndexError:
    print('indice invalido da lista')
except Exception as ex:
    print('Erro desconhecido. Erro: {}' .format(ex))
else:
    print('executa quando não ocorre exeção')
finally:
    print('sempre executa')
